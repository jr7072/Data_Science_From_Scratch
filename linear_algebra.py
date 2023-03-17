from typing import List
import math


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