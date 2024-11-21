# 0x07. Rotate 2D Matrix

## Overview

This project is part of the ALX Software Engineering Program. It's designed to help me understand and implement an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. By the end of this project, I should be able to explain various concepts related to matrix manipulation and in-place operations without needing to look them up.

## Learning Objectives

By completing this project, I aim to understand:

- Matrix representation in Python
- In-place operations
- Matrix transposition
- Reversing rows in a matrix
- Nested loops

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file is mandatory
- Code should use the `pycodestyle` style (version 2.8.0)
- You are not allowed to import any module
- All modules and functions must be documented
- All files must be executable

## Key Concepts for Rotate 2D Matrix

### Matrix Representation in Python

Understanding how 2D matrices are represented using lists of lists in Python and how to access and modify elements in a 2D matrix.

### In-place Operations

Performing operations on data without creating a copy of the data structure. Minimizing space complexity by modifying the matrix in place.

### Matrix Transposition

Understanding the concept of transposing a matrix (swapping rows and columns) and implementing matrix transposition as a step in the rotation process.

### Reversing Rows in a Matrix

Manipulating rows of a matrix by reversing their order as part of the rotation process.

### Nested Loops

Using nested loops to iterate through 2D data structures like matrices and modifying elements within nested loops to achieve the desired rotation.

## Resources

- Python Official Documentation:
  - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- GeeksforGeeks Articles:
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- TutorialsPoint:
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Tasks

### 0. Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

- **Prototype:** `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

Example:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

Expected output:

```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```
