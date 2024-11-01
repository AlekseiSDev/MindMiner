---
Связи: 
tags:
  - Tricks
  - ML
links:
---
Популярная фишка в [[machine learning]], 
Короче говоря, мы генерируем слова в генеративных модельках (или [[Machine translation]]) не выбирая жадно на каждом шагу, а прикидывая вероятность такого предложения эт ол.

## Basics
- Есть параметр B -  какую длину последовательности мы рассматриваем
![[Pasted image 20230927120953.png]]


## Example
Рассматрим Beam search B = 2
- На первом шаге запоминаем 2 наиболее вероятных слов
- Делаем второй шаг 
- Процесс останавливается, когда модель предиктит EOS токен для всех наиболее вероятных последовательностей
![[Pasted image 20230927121042.png]]![[Pasted image 20230927121151.png]]![[Pasted image 20230927121251.png]]![[Pasted image 20230927121438.png]]


## Problems
![[Pasted image 20230927121514.png]]