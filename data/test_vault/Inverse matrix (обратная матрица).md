---
tags:
  - Math
  - LinAlg
links:
---


An **inverse matrix** of a square [[Second brain/main/Matrix (матрица)|Matrix]] $A$ is denoted as $A^{-1}$, and it is defined such that:

$$
A A^{-1} = A^{-1} A = I_n
$$

where $I_n$ is the [[Identity matrix (единичная матрица)|identity matrix]] of the same size as $A$. The inverse matrix exists only if $A$ is a **non-singular** (or **invertible**) matrix, meaning that its determinant is non-zero ($\det(A) \neq 0$).

## Properties of Inverse Matrices

- **Uniqueness**: If a matrix $A$ is invertible, its inverse $A^{-1}$ is unique.
- **Product Inverse**: The inverse of a product of two matrices $A$ and $B$ is given by:
  $$
  (AB)^{-1} = B^{-1} A^{-1}
  $$
- **Transpose Inverse**: The inverse of the transpose of a matrix is the transpose of the inverse:
  $$
  (A^T)^{-1} = (A^{-1})^T
  $$
- **Inverse of an Inverse**: The inverse of the inverse of a matrix is the original matrix:
  $$
  (A^{-1})^{-1} = A
  $$

## Finding the Inverse

To find the inverse of a matrix $A$, several methods can be used:

1. **Gaussian Elimination**: Augment the matrix $A$ with the identity matrix and use row operations to reduce $A$ to the identity matrix, which will transform the identity matrix into $A^{-1}$.

2. **Adjoint Method**: The inverse can be found using the formula:
   $$
   A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
   $$
   where $\text{adj}(A)$ is the adjugate of $A$.

3. **LU Decomposition**: Factorize the matrix into a product of a lower triangular matrix $L$ and an upper triangular matrix $U$, and then solve for the inverse using forward and backward substitution.

Note that not all matrices are invertible. A matrix that is not invertible is called **singular**.

