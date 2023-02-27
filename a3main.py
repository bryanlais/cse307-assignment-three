import sys
import tpg

class AnalError(Exception):
    """Class of exceptions raised when an error occurs during analysis."""


# These are the classes of nodes of our abstract syntax trees (ASTs).

class Node(object):
    """Base class of AST nodes."""

    # For each class of nodes, store names of the fields for children nodes.
    fields = []

    def __init__(self, *args):
        """Populate fields named in "fields" with values in *args."""
        assert(len(self.fields) == len(args))
        for f, a in zip(self.fields, args): setattr(self, f, a)
    

# subclasses of Node for expressions

class Var(Node):
    """Class of nodes representing accesses of variable."""
    fields = ['name']
    
class Int(Node):
    """Class of nodes representing integer literals."""
    fields = ['value']
    
class String(Node):
    """Class of nodes representing string literals."""
    fields = ['value']
    
class Array(Node):
    """Class of nodes representing array literals."""
    fields = ['elements']

class Index(Node):
    """Class of nodes representing indexed accesses of arrays or strings."""
    fields = ['indexable','index']

class BinOpExp(Node):
    """Class of nodes representing binary-operation expressions."""
    fields = ['left', 'op', 'right']
    
class UniOpExp(Node):
    """Class of nodes representing unary-operation expressions."""
    fields = ['op', 'arg']


# subclasses of Node for statements

class Print(Node):
    """Class of nodes representing print statements."""
    fields = ['exp']

class Assign(Node):
    """Class of nodes representing assignment statements."""
    fields = ['left', 'right']
    
class Block(Node):
    """Class of nodes representing block statements."""
    fields = ['stmts']

class If(Node):
    """Class of nodes representing if statements."""
    fields = ['exp', 'stmt']

class While(Node):
    """Class of nodes representing while statements."""
    fields = ['exp', 'stmt']

class Def(Node):
    """Class of nodes representing procedure definitions."""
    fields = ['name', 'params', 'body']

class Call(Node):
    """Class of nodes representing precedure calls."""
    fields = ['name', 'args']


# This is the parser using TPG for parsing MustScript and building an AST.
class Parser(tpg.Parser):
    r"""
    token int:         '\d+' ;
    token string:      '\"[^\"]*\"' ;
    token ident:       '[a-zA-Z_][\w]*' ;
    separator spaces:  '\s+' ;
    separator comment: '#.*' ;

    START/s -> Stmt/s ;

    Stmt/s ->
    ( 'print' Exp/e ';'                                     $ s = Print(e) $
    | Exp/l '=(?!=)' Exp/r ';'                              $ s = Assign(l, r) $
    | '\{'  $ s=[] $  ( Stmt/s2  $ s.append(s2) $  )* '\}'  $ s = Block(s) $
    | 'if' '\(' Exp/e '\)' Stmt/s                           $ s = If(e, s) $
    | 'while' '\(' Exp/e '\)' Stmt/s                        $ s = While(e, s) $
    | 'def' ident/f '\('  $ l=[] $  ( ident/i  $ l.append(i) $
                                    ( ',' ident/i  $ l.append(i) $  )*)? '\)'
      Stmt/s2                                               $ s = Def(f,l,s2) $
    | ident/f '\('  $ l=[] $  ( Exp/e  $ l.append(e) $
                              ( ',' Exp/e  $ l.append(e) $  )*)? '\)' ';'
                                                            $ s = Call(f,l) $
    ) ;

    Exp/e -> Or/e ;
    Or/e  -> And/e ( 'or'  And/e2  $ e = BinOpExp(e,'or', e2) $  )* ;
    And/e -> Not/e ( 'and' Not/e2  $ e = BinOpExp(e,'and',e2) $  )* ;
    Not/e -> 'not' Not/e  $ e = UniOpExp('not', e) $  | Cmp/e ;
    Cmp/e -> Add/e ( CmpOp Add/e2  $ e = BinOpExp(e,CmpOp,e2) $  )* ;
    Add/e -> Mul/e ( AddOp Mul/e2  $ e = BinOpExp(e,AddOp,e2) $  )* ; 
    Mul/e -> Index/e ( MulOp Index/e2  $ e = BinOpExp(e,MulOp,e2) $  )* ;
    Index/e -> Atom/e ( '\[' Exp/e2 '\]'  $ e = Index(e,e2) $  )* ;
    Atom/e -> '\(' Exp/e '\)'
    | int/i     $ e = Int(int(i)) $
    | string/s  $ e = String(s[1:-1]) $
    | '\['  $ e = [] $  ( Exp  $e.append(Exp)$  ( ',' Exp  $e.append(Exp)$  )*)?
      '\]'  $ e = Array(e) $
    | ident     $ e = Var(ident) $
    ;
    CmpOp/r -> '=='/r | '<'/r | '>'/r ;
    AddOp/r -> '\+'/r | '-'/r ;
    MulOp/r -> '\*'/r | '/'/r ;
    """

def parse(code):
    # This makes a parser object, which acts as a parsing function.
    parser = Parser()
    return parser(code)


# Below is the driver code, which parses a given MustScript program
# and analyzes the definitions and uses of procedures and variables

# Open the input file, and read in the input program.
prog = open(sys.argv[1]).read()

try:
    # Try to parse the program.
    print('Parsing...')
    node = parse(prog)

    # Try to analyze the program.
    print('Analyzing...')

    # ... set up and call method for analyzing procedures here

    # ... set up and call method for analyzing variables here

# If an exception is rasied, print the appropriate error.
except tpg.Error:
    print('Parsing Error')

    # Uncomment the next line to re-raise the parsing error,
    # displaying where the error occurs.  Comment it for submission.

    # raise

except AnalError as e:
    print('Analysis Error')

    # Uncomment the next line to re-raise the evaluation error, 
    # displaying where the error occurs.  Comment it for submission.

    # raise
