---
Связи: 
tags:
  - Math
  - "#Algo"
---
Популярная [[Data structures]] фомата {key: value}
Мы можем запихнуть в нее любую пару ключ-значение, и потом получим значение по ключу за O(1)
Основные элементы - ключи, [[Hash function]] и массив значений
- Ключи должны быть уникальными, это любой уникальный неизменяемый тип
- Массив значений - некоторый массив в памяти, куда складываются элементы Values
- Хэш-функция - функция, по key получающая числовой сдвиг, который используется как индекс массива. Т.е. мы можем мнгновенно по key получить индекс и вернуть по нему value из массива значений


- [[#Hash function|Hash function]]
	- [[#Hash function#Very simple hash table|Very simple hash table]]
	- [[#Hash function#Hash function by location|Hash function by location]]
- [[#Locality Sensitive Hashing|Locality Sensitive Hashing]]
	- [[#Locality Sensitive Hashing#Which side of the plane?|Which side of the plane?]]
	- [[#Locality Sensitive Hashing#Python Implementatuin|Python Implementatuin]]

## Смешные бесполезные картинки 
![[Pasted image 20230901103028.png]]![[Pasted image 20230901103037.png]]

## Hash function
![[Pasted image 20230901103149.png]]


### Very simple hash table
![[Pasted image 20230901103149.png]]
![[Pasted image 20230901103725.png]]


### Hash function by location
![[Pasted image 20230901103828.png]]


