---
tags:
  - Math
  - Calculus
links:
---
Исследование [[function|функции]] — это процесс определения её ключевых свойств и поведения на всей [[Domain (область определения)|области определения]]. Этот анализ позволяет понять, как функция ведёт себя графически и математически, что важно в различных областях математики и прикладных наук. Основные этапы исследования функции включают:

![[Pasted image 20241025232051.png]]
![[Pasted image 20241025232106.png]]
// TODO: пофиксить формулки, добавить ссылки
- **Область определения (Domain):**
    
    - **Определение:** Набор всех допустимых значений переменной xxx, для которых функция f(x)f(x)f(x) существует.
    - **Пример:** Для функции f(x)=2x+1f(x) = \sqrt{2x + 1}f(x)=2x+1​ область определения 2x+1≥0⇒x≥−122x + 1 \geq 0 \Rightarrow x \geq -\frac{1}{2}2x+1≥0⇒x≥−21​.
- **Пределы и непрерывность (Limits and Continuity):**
    
    - **Пределы:** Изучение поведения функции при приближении xxx к определённым точкам или бесконечности.
    - **Непрерывность:** Функция называется непрерывной в точке, если предел функции при x→cx \to cx→c равен значению функции в этой точке.
    - **Пример:** Функция f(x)=1xf(x) = \frac{1}{x}f(x)=x1​ имеет разрыв в точке x=0x = 0x=0.
- **Производная и монотонность (Derivative and Monotonicity):**
    
    - **Первая производная f′(x)f'(x)f′(x):** Определяет скорость изменения функции. Позволяет определить интервалы возрастания и убывания.
    - **Монотонность:**
        - Если f′(x)>0f'(x) > 0f′(x)>0 на интервале, функция возрастает.
        - Если f′(x)<0f'(x) < 0f′(x)<0 на интервале, функция убывает.
    - **Пример:** Для f(x)=x3f(x) = x^3f(x)=x3, f′(x)=3x2≥0f'(x) = 3x^2 \geq 0f′(x)=3x2≥0, функция возрастает на всей области определения.
- **Критические точки и экстремумы (Critical Points and Extrema):**
    
    - **Критические точки:** Точки, где f′(x)=0f'(x) = 0f′(x)=0 или f′(x)f'(x)f′(x) не существует.
    - **Локальные экстремумы:** Максимумы и минимумы функции в окрестности точки.
    - **Глобальные экстремумы:** Абсолютные максимумы и минимумы на всей области определения.
    - **Пример:** Для f(x)=x2f(x) = x^2f(x)=x2, f′(x)=2xf'(x) = 2xf′(x)=2x. Критическая точка x=0x = 0x=0 — глобальный минимум.
- **Вторая производная и выпуклость (Second Derivative and Concavity):**
    
    - **Вторая производная f′′(x)f''(x)f′′(x):** Определяет выпуклость или вогнутость функции.
        - Если f′′(x)>0f''(x) > 0f′′(x)>0, функция выпуклая вверх.
        - Если f′′(x)<0f''(x) < 0f′′(x)<0, функция выпуклая вниз.
    - **Точки перегиба:** Точки, где функция меняет выпуклость (f′′(x)=0f''(x) = 0f′′(x)=0 и меняет знак).
    - **Пример:** Для f(x)=x3f(x) = x^3f(x)=x3, f′′(x)=6xf''(x) = 6xf′′(x)=6x. Точка перегиба в x=0x = 0x=0.
- **Ассимптоты и поведение в бесконечности (Asymptotes and End Behavior):**
    
    - **Вертикальные ассимптоты:** Линии x=ax = ax=a, к которым функция стремится при x→ax \to ax→a.
    - **Горизонтальные ассимптоты:** Линии y=by = by=b, к которым функция стремится при x→±∞x \to \pm\inftyx→±∞.
    - **Наклонные ассимптоты:** Линии вида y=kx+my = kx + my=kx+m, к которым функция стремится при x→±∞x \to \pm\inftyx→±∞.
    - **Пример:** Для f(x)=2x+3x−1f(x) = \frac{2x + 3}{x - 1}f(x)=x−12x+3​ вертикальная ассимптота x=1x = 1x=1, наклонная ассимптота y=2+5x−1y = 2 + \frac{5}{x - 1}y=2+x−15​, при x→∞x \to \inftyx→∞ стремится к y=2x+…y = 2x + \dotsy=2x+….
- **Промежутки возрастания и убывания, выпуклости и вогнутости:**
    
    - **Комплексный анализ:** Объединение информации о производных для определения, где функция возрастает/убывает и где она выпуклая/вогнутая.
    - **Пример:** Функция f(x)=x3−3xf(x) = x^3 - 3xf(x)=x3−3x возрастает на (−∞,−1)(-\infty, -1)(−∞,−1) и (1,∞)(1, \infty)(1,∞), убывает на (−1,1)(-1, 1)(−1,1); выпуклая вверх на (−∞,0)(-\infty, 0)(−∞,0) и вниз на (0,∞)(0, \infty)(0,∞).
- **Дополнительные свойства:**
    
    - **Периодичность:** Функция повторяет свои значения через определённые интервалы.
    - **Чётность и нечётность:** Функция чётная, если f(−x)=f(x)f(-x) = f(x)f(−x)=f(x); нечётная, если f(−x)=−f(x)f(-x) = -f(x)f(−x)=−f(x).
    - **Симметрия графика:** Отражение относительно осей или начала координат.