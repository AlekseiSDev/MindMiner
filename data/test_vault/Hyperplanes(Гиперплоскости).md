---
tags:
  - Math
  - LinAlg
links:
---
Гиперплоскости — это обобщение плоскостей в пространствах размерности выше двух. В [[Euclidian Vector Space (Евклидово векторное пространствно)|евклидовом пространстве ]] R^n, гиперплоскость определяется уравнением:

![[Pasted image 20240925152033.png]]
как минимум одна wi != 0

Уравнение можно записать в компактной форме через [[dot product (скалярное произведение векторов)]]:

(w,x)+b=0

где w— нормальный [[vector (вектор)]], а x — вектор координат точки в пространстве.

Примеры:
![[Pasted image 20240925152256.png]]


Уравнение гиперплоскости - посутим, координаты нормали к ней
![[Pasted image 20240925152442.png]]


### Пример в машинном обучении:

В машинном обучении гиперплоскости часто используются в качестве разделителей классов в задачах классификации. Например, линейный классификатор определяет гиперплоскость, которая делит пространство на два класса — объекты "выше" гиперплоскости относятся к одному классу, а объекты "ниже" к другому. Формализовать это можно следующим образом:

- Объекты выше гиперплоскости удовлетворяют условию (w,x)+b>0(w, x) + b > 0(w,x)+b>0,
- Объекты ниже гиперплоскости: (w,x)+b<0(w, x) + b < 0(w,x)+b<0.

Таким образом, гиперплоскости являются ключевыми элементами в таких методах, как метод опорных векторов (SVM).

![[Pasted image 20240925152618.png]]