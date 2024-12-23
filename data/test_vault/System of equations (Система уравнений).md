---
tags:
  - "#LinAlg"
  - "#Math"
links: "[[Linear Algebra (Линейная алгебра, линал)]]"
---

## Basics
СУ - Одно из базовых понятий [[Linear Algebra (Линейная алгебра, линал)|Линала]]
Набор уравнений, где есть левая часть с переменными и правая с ответами
![[Pasted image 20240227102343.png]]


### Solution properties 
- Unique solution
- Infinite solutions
- No solution
![[Pasted image 20240227102519.png]]

### Связь систем линейных уравнений с [[Matrix (матрица)|матрицами]] и матричным умножением

1. **Системы линейных уравнений и матрицы**: Систему линейных уравнений можно записать в матричной форме. Рассмотрим систему из m уравнений с n неизвестными:
   
   $$
   \begin{cases}
   a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
   a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
   \vdots \\
   a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
   \end{cases}
   $$
   
   Эту систему можно представить в виде матричного уравнения:
   $$A \vec{x} = \vec{b}$$
   где:
   - A — матрица коэффициентов размером m*n, содержащая элементы $(a_{ij})$.
   - $\vec{x}$ — вектор неизвестных $[x_1, x_2, \dots, x_n]^T$.
   - $\vec{b}$ — вектор свободных членов $[b_1, b_2, \dots, b_m]^T$.

2. **Матричное умножение**: В матричном уравнении \(A \vec{x} = \vec{b}\) используется матричное умножение для вычисления левой части уравнения. Элемент \(i\)-й строки произведения \(A \vec{x}\) представляет собой линейную комбинацию элементов строки матрицы \(A\) с компонентами вектора \(\vec{x}\). Таким образом, каждое уравнение системы соответствует одной строке матрицы \(A\) и одному элементу вектора \(\vec{b}\).

## Связь с базисом
### Связь систем линейных уравнений с матрицами, матричным умножением и базисами

1. **Системы линейных уравнений и матрицы**: Систему линейных уравнений можно записать в матричной форме. Рассмотрим систему из $m$ уравнений с $n$ неизвестными:

   $$
   \begin{cases}
   a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
   a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
   \vdots \\
   a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
   \end{cases}
   $$

   Эту систему можно представить в виде матричного уравнения:
   $$A \vec{x} = \vec{b}$$
   где:
   - $A$ — матрица коэффициентов размером $m \times n$, содержащая элементы $a_{ij}$.
   - $\vec{x}$ — вектор неизвестных $[x_1, x_2, \dots, x_n]^T$.
   - $ec{b}$ — вектор свободных членов $[b_1, b_2, \dots, b_m]^T$.

2. **Матричное умножение**: В матричном уравнении $A \vec{x} = \vec{b}$ используется матричное умножение для вычисления левой части уравнения. Элемент $i$-й строки произведения $A \vec{x}$ представляет собой линейную комбинацию элементов строки матрицы $A$ с компонентами вектора $ec{x}$. Таким образом, каждое уравнение системы соответствует одной строке матрицы $A$ и одному элементу вектора $ec{b}$.

3. **Базисы и линейные комбинации**: Решение системы линейных уравнений связано с понятием базиса и линейной комбинации векторов. Столбцы матрицы $A$ можно рассматривать как векторы в пространстве размерности $m$. Если вектор $ec{b}$ лежит в линейной оболочке столбцов матрицы $A$, то система имеет решение. В этом случае вектор $ec{b}$ можно выразить как линейную комбинацию столбцов матрицы $A$, а коэффициенты этой линейной комбинации и будут компонентами вектора $ec{x}$.




