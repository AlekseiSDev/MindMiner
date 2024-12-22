---
Связи:
  - - Text representation
Теги: "#Math"
tags:
  - "#Math"
wte: 
links: "[[vector (вектор)]]"
---
[[vector space (векторное пространство)]], куда переносятся тексты

- [[#Основные типы:|Основные типы:]]
- [[#Why?|Why?]]
- [[#Word by Word|Word by Word]]
- [[#Word by Document Design|Word by Document Design]]
- [[#Manipulating vector space|Manipulating vector space]]
- [[#Transforming word vectors|Transforming word vectors]]



## Основные типы:
- whole text embedings - получаем представление всего текста так или иначе. Не известно, есть ли методы, которые без sentence и word эмбедов строят это так, будето можно обртиться к более мелким частям
- sentence embedings - эмбеды предложений
- words embedings - эмбеды слов

## Why? 
От контекста и последовательности слов, у предложений может быть принципиально разное значение
![[Pasted image 20230831125734.png]]
![[Pasted image 20230831125835.png]]


## Word by Word
1) We can create coocurance matrix and word data now have (2, 1, 1, 0) vector representation. k=2 means distance between them (its why I = 0 for data)
![[Pasted image 20230831131241.png]]



## Word by Document Design
- We also can find representation words as vector via Document Design
![[Pasted image 20230831132121.png]]
![[Pasted image 20230831132205.png]]


## Manipulating vector space
- Мы можем найти столиц РФ, знаю столицу США и США и отношение между векторами.
- Это буквально работает, я нашел столицу Египта лол
![[Pasted image 20230831230830.png]]


## Transforming word vectors
