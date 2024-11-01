---
Связи: 
tags:
  - DL
  - NLP
  - Metric
links:
---
Это [[Evaluation metric]] для задачи [[Machine translation]]

Распределено от 0 до 1, чем ближе к 1 тем лучше

## Vanila
- Просто считаем кол-во слов из кандидата в reference и инкрементируем счетчик, затем делим на длину кандидата
- Мб 1 с дерьмовым переводом с рис 1
![[Pasted image 20230927104855.png]]![[Pasted image 20230927105037.png]]


## Modified version
- Убираем слово из reference если уже его посчитали

![[Pasted image 20230927105134.png]]![[Pasted image 20230927105147.png]]


## Pros and cons
![[Pasted image 20230927105224.png]]