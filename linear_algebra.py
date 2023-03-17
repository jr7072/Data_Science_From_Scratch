from typing import List, Tuple, Callable
import math


'''
    VECTOR SECTION
'''


# define vector type
Vector = List[float]


# assert length of vectors
def assert_vector_length(*vectors: Vector) -> None:
    '''
        asserts that all vectors passed are of equal length

        vectors: unpacking of vectors

        returns None
    '''

    length_set = set([len(vector) for vector in vectors])

    assert len(length_set) == 1, "Vectors are fnot the same length"


# add vectors
def add(v: Vector, w: Vector) -> Vector:
    '''
        performs vector addition

        v (Vector): first vector
        w (Vector): second vector

        returns (Vector): sum of v and w
    '''

    assert_vector_length(v, w)

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

# subtract vectors
def subtract(v: Vector, w: Vector) -> Vector:
    '''
        performs vector subtraction

        v (Vector): first vector
        w (Vector): second vector

        returns (Vector): difference of v and w
    '''

    assert_vector_length(v, w)

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]


# vector sum
def vector_sum(vectors: List[Vector]) -> Vector:
    '''
        performs compenentwise addition
        on a list of vectors

        vectors (Vector): list of vectors of the same length

        returns (Vector): sum of all vectors (componentwise)
    '''

    assert_vector_length(*vectors)
    
    vector_length = len(vectors[0])
    vector_sum  = []

    for i in range(vector_length):
        
        component_sum = sum(vector[i] for vector in vectors)
        vector_sum.append(component_sum)

    return vector_sum

assert vector_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [12, 15, 18]


# scaler multiplication
def scaler_multiply(c: float, v: Vector) -> Vector:
    '''
        Multiplies vector by a scaler

        c (float): scaler to multiply vector with
        
        v (Vector): vector to perform multiplication on

        returns (Vector): Product of vector v and scaler c
    '''

    return [c * v_i for v_i in v]

assert scaler_multiply(2, [1, 2, 3]) == [2, 4, 6]

# vector means
def vector_mean(vectors: List[Vector]) -> Vector:
    '''
        returns componentwise means of a list of vectors

        vectors (List[Vector]): list of vectors of the same length

        returns (Vector): Vector with componentwise means
    '''

    n = len(vectors)
    sum_vector = vector_sum(vectors)
    mean_vector = scaler_multiply(1 / n, sum_vector)

    return mean_vector

assert vector_mean([[1, 2, 5], [1, 6, 5]]) == [1, 4, 5]


# dot product
def dot(v: Vector, w: Vector) -> float:

    '''
        dot product of vector v and w

        v (Vector): first vector

        w (Vector): second vector

        return (float): dot product of v and w
    '''

    assert_vector_length(v, w)

    dot_product = sum(v_i * w_i for v_i, w_i in zip(v, w))

    return dot_product

assert dot([1, 2, 3], [4, 5, 6]) == 32

# sum of squares
def sum_of_squares(v: Vector) -> float:

    '''
        returns sum of squares of a vector

        v (Vector): vector to get sum of squares from

        returns (float): sum of sqaures of the vector
    '''

    return dot(v, v)

assert sum_of_squares([1, 2]) == 5


# vector magnitude
def magnitude(v: Vector) -> float:

    '''
        returns magnitude of a vector

        v (Vector): vector to get magnitude from

        returns (float): magnitude of the vector
    '''

    vector_ss = sum_of_squares(v)
    return math.sqrt(vector_ss)

assert magnitude([2, 2]) == math.sqrt(8)


# distance of two vectors
def distance(v: Vector, w: Vector) -> float:
    '''
        computes distance of two vectors

        v (Vector): first vector

        w (Vector): second vector

        returns (float): the distance of v and w 
    '''

    difference_vector = subtract(v, w)
    return magnitude(difference_vector)


assert distance([1, 2], [3, 4]) == math.sqrt(8)


'''
    MATRIX SECTION
'''


# defining Matrix type
Matrix = List[List[float]] 


# shape of the matrix
def shape(A: Matrix) -> Tuple[int]:
    '''
        calculates the shape of a matrix

        A (Matrix): Input Matrix

        returns (Tuple[int]): tuple that represents the shape of
        the matrix (rows, col)
    '''

    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1],[2]]) == (2, 1)


# get row of a matrix
def get_row(A: Matrix, i: int) -> Vector:
    '''
        gets a row vector from a matrix given index

        A (Matrix): Input matrix 
 
        i (int): index of the row to get

        returns (Vector): The row vector of the matrix
        at index i
    ''' 

    row_vector = A[i]
    return row_vector

assert get_row([[1], [2]], 0) == [1]


# get column of a matrix
def get_column(A: Matrix, i: int) -> Vector:
    '''
        gets the columns vector of Matrix given an
        index

        A (Matrix): input matrix

        i (int): column index of the desired column vector

        returns (Vector): The columns Vector of matrix A at
        position i
    '''

    column_vector = [A_i[i] for A_i in A]
    return column_vector

assert get_column([[1, 2], [1, 3]], 1) == [2, 3]


# matrix generation
def make_matrix(shape: Tuple[int],
                    entry_fn: Callable[[int, int], float]) -> Matrix:
    
    '''
        Creates a matrix given a shape and an entry funtion

        shape (Tuple[int]): shape of the desired matrix (n_rows, n_cols)

        entry_fn (Callable[[int, int], float]): funciton to calculate value 
        given row index and row column.

        returns (Matrix): Matrix generated 
    '''

    n_rows, n_cols = shape
    
    matrix = []

    for row_index in range(n_rows):

        matrix_row = [entry_fn(row_index, col_index) 
                        for col_index in range(n_cols)]
        
        matrix.append(matrix_row)
    
    return matrix

def test(a, b) -> int:
    return a + b

assert make_matrix((2, 1), test) == [[0], [1]]


# identity matrix
def identity_matrix(n: int) -> Matrix:
    '''
        returns identity matrix of size n * n

        n (int): size that that will be used to create
        a n * n matrix

        return (Matrix): n * n identity matrix
    '''

    shape = (n, n)
    identity_func = lambda x, y: 1 if x == y else 0
    return make_matrix(shape, identity_func)

assert identity_matrix(2) == [[1, 0],[0, 1]]