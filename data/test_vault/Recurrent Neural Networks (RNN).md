---
Связи: 
tags:
  - NLP
links:
---
Один из видов [[neural network]], для задач [[NLP]]

- [[#Abstract|Abstract]]
- [[#Applications|Applications]]
- [[#Summary|Summary]]


## Abstract
Пробрасывает инфу с начала приложения и до конца, слово за словом
Все, что мы обучаем - это матричку весов Wx, матричку весов Wh и матричку Wout.
Каждое слово идет на вход Wx, 
- НЕТОЧНО! полученный результат проходит через Whidden и складывается с Whidden прошлого слова
- На вход матричку Wout идет сумма всех слов, каждое из которыз прощуено через Wx и Wh 

![[Pasted image 20230922134422.png]]![[Pasted image 20230922134450.png]]


## Math
- Вся матеша рис 1
- Конкретная матеша в ячейке рис 2
- Посути мы учим 2 матрички весов - для входа и для скрытого слоя и выдаем аутпут

![[Pasted image 20230924093557.png]]
![[Pasted image 20230924093904.png]]

### Cost function
[[Cross-entropy loss]]
![[Pasted image 20230924095018.png]]

## Applications
- РННка для предикта победителя группы по счету. Юзелес
- One-2-many - берем чето одно(фотку) и преобразуем к кучке
- Many2one - берем предложение, предсказываем класс
- Many2Many - machine translation e.g.
	- Часто использует архитектуру Encoder-Decore


![[Pasted image 20230922134936.png]]
![[Pasted image 20230922135016.png]]
![[Pasted image 20230922135031.png]]
![[Pasted image 20230922135130.png]]

## Implementations
- Например для tf вот так норм

![[Pasted image 20230924095239.png]]




## Summary

![[Pasted image 20230922134759.png]]