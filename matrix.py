import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
       
        
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        dt=0
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        if self.h == 1 :
            dt.append(slef.g[0][0])
        elif self.h == 2 :
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                
                raise ValueError('The determinant is zero .')
            else:
                a=self.g[0][0]
                b=self.g[0][1]
                c=self.g[1][0]
                d=self.g[1][1]
                
                dt= a*d-b*c
        return Matrix(dt)
        
        
    def trace(self):
        
        
        #if not self.is_square():
            
            #raise (ValueError ,"Cannot calculate the trace of a non-square matrix.")
        #if self.h > 2:
            #raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        tr_s=0
        for i in range(self.h):
            for j in range(self.w):
                
                tr_s=tr_s+self.g[i][j]
                
        return tr_s

        
        
                    

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inv= []
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1 :
            
            inv.append([1 / self.g[0][0]])
            
        elif self.h == 2 :
            
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                
                raise ValueError('The matrix is not invertible.')
                
            else:
                a=self.g[0][0]
                b=self.g[0][1]
                c=self.g[1][0]
                d=self.g[1][1]
                
                f = 1 /(a * d - b*c)
                
                inv = [[d,-b],[-c,a]]
                
                for i in range(len(inv)):
                    new_row=[]
                    for j in range(len(inv[0])):
                        inv[i][j]= f*inv[i][j]
                                       
        
        return Matrix(inv)    

    def T(self):
                            
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose=[]
        for c in range(self.w):
            new_row = []
            for r in range(self.h):
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
    
        return Matrix(matrix_transpose)                               
                                       

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        result=[]                              
        for i in range(self.h):
                                       
            new_row=[]
                                       
            for j in range(self.w):
                                       
                                       
                new_row.append(self.g[i][j]+other.g[i][j])
                                       
            result.append(new_row)
                                       
        return Matrix(result)
                                       
    def __neg__(self):
                                       
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        result=[]                               
        for i in range(self.h):
            new_row=[]
            for j in range(self.w):
                new_row.append(-self.g[i][j])
            result.append(new_row)
                                       
                                       
        return Matrix(result)                                   

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
       
                                       
        return (self + -other)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        
        def dot_product(vectorA, vectorB):
            result = 0
    
            for i in range(len(vectorA)):
                result += vectorA[i] * vectorB[i]
        
            return result
        
        def transpose(matrix):
            matrix_transpose = []
            for c in range(len(matrix[0])):
                new_row = []
                for r in range(len(matrix)):
                    new_row.append(matrix[r][c])
                matrix_transpose.append(new_row)
    
            return matrix_transpose 
        product = []

        transposeB =transpose(other.g)

        for r1 in range(len(self.g)):
            new_row = []
            for r2 in range(len(transposeB)):
                dp = dot_product(self.g[r1], transposeB[r2])
                new_row.append(dp)
            product.append(new_row)

        return Matrix(product)                               

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        result=[]
        for i in range(self.h):
            rm=[]
            for j in range(self.w):
               
                if  isinstance(other, numbers.Number):
                    rm.append(self.g[i][j]*other)
            result.append(rm)
        return Matrix(result)
            
        
        
        
           
        
          
        
            