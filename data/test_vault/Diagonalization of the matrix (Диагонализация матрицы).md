---
tags:
  - Math
  - LinAlg
links:
---
# Диагонализация матрицы

**Диагонализация** [[Matrix (матрица)|матрицы]] — это представление квадратной матрицы $A$ в виде произведения:
$$
A = P D P^{-1}
$$
где $P$ — матрица, состоящая из [[Eigenvectors (собственные вектора матрицы)|собственных векторов]] матрицы $A$, а $D$ — диагональная матрица, элементы которой — [[Eigenvalues (собственные значения матрицы)|собственные значения]] матрицы $A$. Диагонализация позволяет упростить вычисления, связанные с матрицей, например, возведение в степень.

## Возможность диагонализации

Матрица $A$ может быть диагонализируема, если она имеет достаточно **линейно независимых собственных векторов**. В частности, $n \times n$ матрица $A$ диагонализируема тогда и только тогда, когда она имеет $n$ линейно независимых собственных векторов, то есть ее **алгебраическая кратность** собственных значений совпадает с их **геометрической кратностью**.

- **Простые собственные значения**: Если все собственные значения матрицы различны, то матрица гарантированно диагонализируема.
- **Невырожденная матрица собственных векторов**: Если матрица собственных векторов $P$ невырожденная (определитель $\det(P) \neq 0$), то $A$ диагонализируема.

## Свойства диагонализируемых матриц

- **Простота вычислений**: Диагонализированные матрицы удобны для вычислений, например, для возведения в степень: если $A = P D P^{-1}$, то
  $$
  A^k = P D^k P^{-1}
  $$
  где $D^k$ — это диагональная матрица, полученная возведением собственных значений в степень $k$.
- **Собственные значения**: Элементы диагональной матрицы $D$ являются собственными значениями матрицы $A$.
- **Применимость к симметричным матрицам**: Любая симметричная матрица над полем вещественных чисел диагонализируема, и ее собственные значения вещественные, а собственные векторы ортогональны.

## Нахождение диагонализированной матрицы

1. **Нахождение собственных значений**: Найдите **собственные значения** матрицы $A$, решив характеристическое уравнение:
   $$
   \det(A - \lambda I) = 0
   $$
   где $\lambda$ — собственные значения матрицы $A$.

2. **Нахождение собственных векторов**: Для каждого собственного значения $\lambda_i$ найдите соответствующий **собственный вектор**, решая систему линейных уравнений:
   $$
   (A - \lambda_i I) \mathbf{v} = 0
   $$

3. **Построение матрицы $P$**: Составьте матрицу $P$ из найденных собственных векторов как из столбцов. Если матрица $A$ имеет $n$ линейно независимых собственных векторов, то $P$ невырожденная.

4. **Построение диагональной матрицы $D$**: Составьте диагональную матрицу $D$, на главной диагонали которой находятся собственные значения матрицы $A$.

5. **Проверка диагонализации**: Убедитесь, что $A = P D P^{-1}$. Если данное равенство выполняется, то матрица успешно диагонализирована.

Диагонализация является мощным инструментом в линейной алгебре, упрощая вычисления и анализ поведения линейных операторов, особенно в задачах, связанных с возведением матриц в степень и решением систем дифференциальных уравнений.

