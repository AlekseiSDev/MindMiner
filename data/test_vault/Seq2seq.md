---
Связи: 
tags:
  - NLP
  - DL
links:
---
Тип [[Deep Learning]] архитектур, преимущество в [[NLP]]. Были популярны в задаче [[Machine translation]]

- [[#Abstract|Abstract]]
	- [[#Abstract#Encoder|Encoder]]
	- [[#Abstract#Decoder|Decoder]]
	- [[#Abstract#Information bottleneck|Information bottleneck]]
		- [[#Information bottleneck#Trick to aviod|Trick to aviod]]
	- [[#Abstract#Attention|Attention]]


## Abstract
- Предложена гуглом в 2014
- Обычно сосстоит из [[Encoder (nn)]] and [[Decoder (nn)]] архитектуры

![[Pasted image 20230926140453.png]]![[Pasted image 20230926140518.png]]

### Encoder

![[Pasted image 20230926140602.png]]

### Decoder
![[Pasted image 20230926140635.png]]


### Information bottleneck
- Длинные последовательности проблематичны, т.к. из декодера в энкодер идет не оч много инфы
![[Pasted image 20230926140709.png]]![[Pasted image 20230926140742.png]]

#### Trick to aviod
- Использовать все внутренние состояния вместо 1го
- Но тут можно потерять много контекста
![[Pasted image 20230926140834.png]]

### Attention
- На помощь приходит [[Attention (DL)]]

![[Pasted image 20230926140906.png]]


Pros and cons
- Плохо в параллельных вычислениях - т.к. RNNки(или LSTMки) лежащие под капотом принимают на вход аутпут предыдущего этапа
- Чтоб предсказать перевод (или некст слово) после T слов, нужно пройтись по всем T словам и только потом начинаем генерацию
	- Что может вести к потере информации и [[Vanishing gradients problem]]


![[Pasted image 20230928111303.png]]