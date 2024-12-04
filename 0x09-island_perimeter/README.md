# Island Perimeter

This project focuses on solving the "Island Perimeter" problem using Python. The goal is to calculate the perimeter of an island represented in a 2D grid.

## Table of Contents

- [Introduction](#introduction)
- [Concepts and Skills](#concepts-and-skills)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Resources](#resources)
- [Author](#author)

## Introduction

The problem involves calculating the perimeter of a single island in a grid, where:

- **0** represents water.
- **1** represents land.
- Each cell is a square with a side length of 1.
- Cells are connected horizontally or vertically (not diagonally).

**Assumptions**:

- The grid is completely surrounded by water.
- There is only one island without any lakes (internal water).

---

## Concepts and Skills

### Key Topics Covered

1. **2D Arrays (Matrices)**:
   - Navigating and iterating through grids.
   - Accessing adjacent cells horizontally and vertically.

2. **Conditional Logic**:
   - Identifying when a cell contributes to the perimeter.

3. **Algorithm Development**:
   - Breaking down the problem into smaller tasks:
     - Identifying land cells.
     - Calculating their contribution to the perimeter.

4. **Python Programming**:
   - Utilizing nested loops and conditional statements.
   - Following PEP 8 guidelines for code style.

---

## Requirements

### General

- **Allowed editors**: `vi`, `vim`, `emacs`.
- Code will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3.4.3.
- Adhere to the **PEP 8 style guide**.
- No external module imports allowed.
- All files should:
  - End with a new line.
  - Be executable.
  - Include proper documentation for modules and functions.

### Repository Structure

- **GitHub repository**: [alx-interview](https://github.com/Tariq5mo/alx-interview)
- **Directory**: `0x09-island_perimeter`
- **File**: `0-island_perimeter.py`

---

## Project Tasks

### **0. Island Perimeter**

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

#### Input Constraints

- `grid` is a list of lists of integers.
- Width and height of the grid do not exceed 100.

#### Output

The perimeter of the island.

#### Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
```

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Tariq5mo/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x09-island_perimeter
   ```

3. Run the example script:

   ```bash
   ./0-main.py
   ```

---

## Resources

- **[Python Official Documentation](https://docs.python.org/3/tutorial/)**:
  - Nested lists.
- **GeeksforGeeks**:
  - Multi-dimensional arrays in Python.
- **TutorialsPoint**:
  - Python lists and their manipulation.
- **YouTube**:
  - Tutorials on 2D arrays and grid traversal.

---

## Author

This project was completed by **Tariq Omer**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/Tariq5mo).
