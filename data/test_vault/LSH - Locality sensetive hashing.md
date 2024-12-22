---
Связи: 
tags: 
links:
---
Вид [[Hash function]] и использующей ее [[Hash table]], чтоб пространство внутри дикта было хорошо поделено на батчи, где внутри одного кея - батч, и между членами батча какая-то похожесть

## Basics
- Идея: давайте подберем такую [[Hash function]], чтоб было много коллизий (т.е. разные key мапились в одно место) 
- Кроме этого, надо чтоб коллизили не рандомные key, а похожие
- Тогда получается, что dict делит наше пространство на n бакетов, в каждом из которых хранятся похожие друг на друга value
- И чтоб найти похожих - достаточно по кею получить его бакет - и вот список наиболее похожих соседей у нас в руках
- Инфа по теме https://habr.com/ru/amp/publications/726012/ (немного), 
	- Подробнее почитать про LSH в простом изложении и с кодом можно в [посте James Briggs](https://www.pinecone.io/learn/locality-sensitive-hashing/) (иллюстрация выше как раз из него) и cтатье [Matti Lyra](https://mattilyra.github.io/2017/05/23/document-deduplication-with-lsh.html).
![[Pasted image 20230901120211.png]]![[Pasted image 20230901120250.png]]

### Which side of the plane?


![[Pasted image 20230901120520.png]]![[Pasted image 20230901120614.png]]![[Pasted image 20230901120654.png]]![[Pasted image 20230901120634.png]]![[Pasted image 20230901121531.png]]

### Python Implementatuin
![[Pasted image 20230901121637.png]]

