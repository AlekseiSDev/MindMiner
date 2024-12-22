---
tags:
  - Math
  - LinAlg
links:
---

Ортогональная проекция [[vector (вектор)|вектора]] u на вектор v — это проекция  u на v, которая "сбрасывает" все компоненты вектора u, перпендикулярные v.
Ортогональная - значит, что отбрасываем части базиса, которорые [[Orthogonality (Ортогональность)|ортогональны]] к вектору, на который проецируем
![[Pasted image 20240925143038.png]]


## Calculating projection of a vector

Сначала найдем длину проекции. Рассмотрим картинку выше
У нас прямоугольный треугольник, и |u'(v)| - один из катетов, его длину можно расчитать из длины гипотенузы и угла между u и v
В свою очередь, угол выражается через [[dot product (скалярное произведение векторов)|скалярное произведение]]

|u'| = |u|\*cos(u^v), 
$$
\cos(\alpha_{\mathbf{u}, \mathbf{v}}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{|\mathbf{u}| |\mathbf{v}|}
$$

Имея это на руках, мы можем заметить, что 
$$
\mathbf{P}_{\mathbf{v}}(\mathbf{u}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{|\mathbf{v}| } 
$$
The projection of a vector $u$ onto $v$ is denoted as $u_v'$ and is calculated using the following formula:

$$
    \vec{u_v'} = \frac{\langle u, v \rangle}{\langle v, v \rangle} \vec{v}
$$

where:

- $\langle u, v \rangle$ — the dot product of vectors $u$ and $v$,
- $\langle v, v \rangle$ — the squared norm of vector $v$.
- $\vec{v}$ is the vector onto which the projection is made.

Это можно расписать на бумаге так:
![[Pasted image 20241028193604.png]]


### Расписано от ЧатГпт
![[Pasted image 20240925144159.png]]
![[Pasted image 20240925144212.png]]![[Pasted image 20240925144249.png]]