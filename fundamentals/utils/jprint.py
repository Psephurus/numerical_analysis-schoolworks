"""
Title: jprint.py
Description: custom function to print numpy array mimics Julia style.
Author: Psephurus
Created: 15-01-2024 19:41
Last Modified: 17-01-2024 14:28
Version: 1.2.5
"""

import numpy as np


def numpy_type_to_julia(numpy_type: type) -> str:
    """Converts a NumPy data type to its Julia equivalent."""
    
    type_str = str(numpy_type)
    
    # Find the type name and bit size (if any)
    if numpy_type is np.float_:
        julia_type = 'Float'
    elif numpy_type is np.int_:
        julia_type = 'Int'
    elif numpy_type is np.complex_:
        julia_type = 'Complex'
    elif numpy_type == np.bool_:
        return 'Bool'
    elif "uint" in type_str:
        julia_type = "UInt"
    elif numpy_type == np.str_:
        return 'String'
    else:
        return 'Any'
    
    # Extract the bit size
    bits = ''.join(filter(str.isdigit, type_str))
    
    return julia_type + bits

    
def format_complex_number(complex_element: complex) -> str:
    """Formats a complex number in Julia style."""
    real: float = complex_element.real
    imag: float = complex_element.imag
    return f"{real} + {imag}im" if imag >= 0 else f"{real} - {-imag}im"


def format_element(element: object) -> str:
    """Formats an element based on its type (complex or not)."""
    if isinstance(element, complex):
        return format_complex_number(element)
    return str(element)


def format_array(array: np.ndarray, shape: tuple, julia_type: str) -> str:
    """Formats the array into a string with Julia-like syntax."""
    indent = "  "   # Indentation at the beginning of each line
    is_complex = 'Complex' in julia_type
    
    if len(shape) == 1:  # Vector
        elements = "\n".join(indent + format_element(e) for e in array)
        return (f"{shape[0]}-element Vector{{{julia_type}}}:\n"
                f"{elements}\n")

    elif len(shape) == 2:  # Matrix
        rows = "\n".join(indent + "\t".join(format_element(e) for e in row) for row in array)
        return (f"{shape[0]}×{shape[1]} Matrix{{{julia_type}}}:\n"
                f"{rows}\n")
        
    elif len(shape) > 2:  # Higher dimensions
        result = f"{'×'.join(map(str, shape))} Array{{{julia_type}, {len(shape)}}}:\n"
        indices = np.ndindex(shape[:-2])
        for index in indices:
            index_str = ", ".join(map(str, (i+1 for i in index)))
            result += f"\n[:, :, {index_str}]:\n"
            slice_ = array[index]
            slice_str = "\n".join("\t".join(indent + format_element(e) 
                          for e in row) for row in slice_)
            result += f"{slice_str}\n"
        return result

    else:  # Scalar
        element = format_element(array.item())
        return f"0-dimensional Array{{{julia_type}, 0}}:\n{indent}{element}\n"
    

def jprint(array: np.ndarray) -> None:
    """Prints the array in a Julia-like format.
    
    Parameters
    ----------
    array : `numpy.ndarray`
        The NumPy array to print.
            
    Note
    -----
        Only support numerical data types!
        
    Examples
    --------
    >>> import numpy as np
    >>> y = np.array([10, 20, 30], dtype=np.int32)
    >>> jprint(y)
    3-element Vector{Int32}:
      10
      20
      30
    
    >>> X = np.array([[10, 20, 30, 0.1]], dtype=np.float64)
    >>> jprint(X)
    1×4 Matrix{Float64}:
      10    20    30    0.1
    
    >>> A = np.array([[-1, 0.26, 0.74], [0.09, -1, 0.26], [1, 1, 1]], dtype=np.float64)
    >>> jprint(A)
    3×3 Matrix{Float64}:
      -1      0.26    0.74
      0.09   -1       0.26
      1       1       1
    """
    shape = array.shape
    julia_type = numpy_type_to_julia(array.dtype.type)
    formatted_str = format_array(array, shape, julia_type)
    print(formatted_str)

if __name__ == "__main__":

    # Test the function
    # column vector
    vector = np.array([10, 20, 30])
    print(f"Original Python Style:{vector}")
    print("Julia Style:")
    jprint(vector)

    # row vector
    row_vector = np.array([[10, 20, 30, 0.1]])
    print(f"Original Python Style:\n{row_vector}\n")
    print("Julia Style:")
    jprint(row_vector)

    # matrix
    matrix_a = np.array([[-1, 0.26, 0.74], [0.09, -1, 0.26], [1, 1, 1]])
    print(f"Original Python Style:\n{matrix_a}\n")
    print("Julia Style:")
    jprint(matrix_a)

    # higher dimensions array
    array_3d = np.arange(1, 28).reshape(3, 3, 3)
    print(f"Original Python Style:\n{array_3d}\n")
    print("Julia Style:")
    jprint(array_3d)

    array_4d = np.ones((3, 4, 2, 2))
    print(f"Original Python Style:\n{array_4d}\n")
    print("Julia Style:")
    jprint(array_4d)

    # scalar
    array_0d = np.array(42)
    print(f"Original Python Style:\n{array_0d}\n")
    print("Julia Style:")
    jprint(array_0d)

    # complex
    complex_array = np.array([1+2j, 3+4j, 5+6j])
    print(f"Original Python Style:\n{complex_array}\n")
    print("Julia Style:")
    jprint(complex_array)
    
    mixed_array = np.array([1, 2j, 3+4j, 5, 6])
    print(f"Original Python Style:\n{mixed_array}\n")
    print("Julia Style:")
    jprint(mixed_array)
    
    # 3D complex
    complex_array_3d = np.random.rand(3, 4, 2) + 1j * np.random.rand(3, 4, 2)
    print(f"Original Python Style:\n{complex_array_3d}\n")
    print("Julia Style:")
    jprint(complex_array_3d)
    
    # unsigned 
    uint_array = np.array([1, 2, 3], dtype=np.uint8)
    print(f"Original Python Style:{uint_array}")
    print("Julia Style:")
    jprint(uint_array)

    
    # others
    str_array = np.array(['Hello', 'World'])
    print(f"Original Python Style:\n{str_array}\n")
    print("Julia Style:")
    jprint(str_array)
    
    tuple_array = np.array(([1, 'H'], [3, 'F']))
    print(f"Original Python Style:\n{tuple_array}\n")
    print("Julia Style:")
    jprint(tuple_array)
