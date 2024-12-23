---
tags:
  - Math
  - LinAlg
links:
---
# Метод Гаусса для решения систем уравнений

**Метод Гаусса** (или метод исключения Гаусса) — это алгоритм для решения [[System of equations (Система уравнений)|систем линейных уравнений]], нахождения ранга [[Matrix (матрица)|матрицы]] и вычисления [[Inverse matrix (обратная матрица)|обратной матрицы]]. Метод основан на последовательном преобразовании системы уравнений в эквивалентную треугольную или ступенчатую форму, что позволяет легко найти решение.

## Принципы метода Гаусса

Метод Гаусса заключается в применении **элементарных операций** над строками системы, которые включают:

1. Перестановку двух строк.
2. Умножение строки на ненулевой скаляр.
3. Прибавление к одной строке другой строки, умноженной на некоторый коэффициент.

Цель метода — привести систему уравнений к **ступенчатому виду**, чтобы затем с легкостью найти значения неизвестных, начиная с последнего уравнения.

## Алгоритм метода Гаусса

1. **Прямой ход**:
   - Начните с первой строки и используйте ее для исключения переменной в последующих строках.
   - Перейдите к следующей строке и повторите процесс, исключая следующую переменную в оставшихся строках.
   - Продолжайте, пока система не будет приведена к треугольной форме, где каждое последующее уравнение содержит на одну переменную меньше.

2. **Обратный ход**:
   - После получения треугольной формы начните с последнего уравнения и найдите значение последней переменной.
   - Подставьте найденное значение в предыдущее уравнение и найдите следующую переменную.
   - Повторяйте процесс, пока не будут найдены все переменные.

## Пример для системы уравнений

Рассмотрим систему линейных уравнений:
$$
\begin{cases}
2x + 3y - z = 5 \\
x - y + 2z = 3 \\
3x + y + z = 4
\end{cases}
$$

Запишем систему в матричной форме $A \mathbf{x} = \mathbf{b}$:
$$
A = \begin{bmatrix} 2 & 3 & -1 \\ 1 & -1 & 2 \\ 3 & 1 & 1 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 5 \\ 3 \\ 4 \end{bmatrix}
$$

Соединим $A$ и $\mathbf{b}$ в расширенную матрицу $[A|\mathbf{b}]$:
$$
[A|\mathbf{b}] = \begin{bmatrix} 2 & 3 & -1 & | & 5 \\
1 & -1 & 2 & | & 3 \\
3 & 1 & 1 & | & 4 \end{bmatrix}
$$

### Прямой ход

1. Используем первую строку для исключения $x$ из второй и третьей строк.

   Для этого умножим первую строку на $\frac{1}{2}$ и вычтем из второй строки:
   $$
   R_2 = R_2 - \frac{1}{2} R_1
   $$
   Новая матрица выглядит так:
   $$
   \begin{bmatrix} 2 & 3 & -1 & | & 5 \\
   0 & -\frac{5}{2} & \frac{5}{2} & | & \frac{1}{2} \\
   3 & 1 & 1 & | & 4 \end{bmatrix}
   $$

   Теперь используем первую строку для исключения $x$ из третьей строки. Умножим первую строку на $\frac{3}{2}$ и вычтем из третьей строки:
   $$
   R_3 = R_3 - \frac{3}{2} R_1
   $$
   Новая матрица:
   $$
   \begin{bmatrix} 2 & 3 & -1 & | & 5 \\
   0 & -\frac{5}{2} & \frac{5}{2} & | & \frac{1}{2} \\
   0 & -\frac{7}{2} & \frac{5}{2} & | & -\frac{7}{2} \end{bmatrix}
   $$

2. Переходим ко второй строке и используем ее для исключения $y$ из третьей строки. Для этого умножим вторую строку на $\frac{7}{5}$ и прибавим к третьей строке:
   $$
   R_3 = R_3 + \frac{7}{5} R_2
   $$
   Новая матрица:
   $$
   \begin{bmatrix} 2 & 3 & -1 & | & 5 \\
   0 & -\frac{5}{2} & \frac{5}{2} & | & \frac{1}{2} \\
   0 & 0 & -\frac{1}{5} & | & -1 \end{bmatrix}
   $$

### Обратный ход

1. Начнем с последней строки, где $-\frac{1}{5}z = -1$:
   $$
   z = 5
   $$

2. Подставим $z = 5$ во вторую строку:
   $$
   -\frac{5}{2}y + \frac{5}{2} \cdot 5 = \frac{1}{2}
   $$
   $$
   -\frac{5}{2}y + \frac{25}{2} = \frac{1}{2}
   $$
   $$
   -\frac{5}{2}y = \frac{1}{2} - \frac{25}{2} = -12
   $$
   $$
   y = \frac{24}{5} = 4.8
   $$

3. Подставим $y = 4.8$ и $z = 5$ в первую строку:
   $$
   2x + 3 \cdot 4.8 - 5 = 5
   $$
   $$
   2x + 14.4 - 5 = 5
   $$
   $$
   2x = 5 - 14.4 + 5 = -4.4
   $$
   $$
   x = -2.2
   $$

Итак, решение системы:
$$
\begin{cases}
x = -2.2 \\
y = 4.8 \\
z = 5
\end{cases}
$$

