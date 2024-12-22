---
Связи:
Теги: #Math #ML #NLP
---
Косинусное расстояние
[[function]] для определения расстояния между векторами. Обычно означает косинус угла между векторами и очень популярная мера похожести векторов

- [[#Problem with [[Euclidean Distance]]|Problem with [[Euclidean Distance]]]]
- [[#Finding Cosine Similarity|Finding Cosine Similarity]]
- [[#Properties of Cosine Similarity|Properties of Cosine Similarity]]
- [[#Python Implementation|Python Implementation]]

## Problem with [[Euclidean Distance]]

- По евклиду, расстояние между Агрикульторами и Историей меньше, чем между Агрокультурами и Едой, что не круто
- А вот если померить расстояние между внутренними углами, то будет лучше
 ![[Pasted image 20230831133749.png]]
 ![[Pasted image 20230831133903.png]]

## Finding Cosine Similarity
- review algebra of [[vector (вектор)]] norm and dot product of vectors
- cosine similarity formula pic 2


![[Pasted image 20230831134126.png]]
![[Pasted image 20230831134320.png]]
![[Pasted image 20230831134408.png]]


## Properties of Cosine Similarity
- Когда вектора далеко, угол будет 90, а косинусное расстояние - около -1
- Когда вектора оч похожи, угол будет 0, а расстояние стремиться к 1
- Таким образом это мера похожести, распределенная от -1 до 1, где 0 оч непохожие, а 1 оч похожие вектора
![[Pasted image 20230831134507.png]]


## Python Implementation
![[Pasted image 20230831134802.png]]![[Pasted image 20230831134813.png]]