---
Связи: 
tags:
  - Math
  - Algo
  - "#ToP"
---
Один из важных концептов в [[Theory of Probability]]
Обозначает систему, в которой состояния элемента определяется только предыдущим состоянием

- [[#Simple example|Simple example]]
- [[#Hidden Markov Model|Hidden Markov Model]]
	- [[#Hidden Markov Model#Emission probabilities|Emission probabilities]]
	- [[#Hidden Markov Model#Populating Transition matrix|Populating Transition matrix]]

## Simple example
Как пример можно привести использование их для задачи [[Part of Speech Tagging]]
В этой моделе вероятность каждого следующего слова зависит от предыдущего - в английском предложения структурированы

![[Pasted image 20230908234206.png]]


## Hidden Markov Model
- Однако состояния могут быть скрыты - потому-что не наблюдаются напрямую
- Например в вышеупомянутой модели - мы не знаем точные части речи у слов - ибо немало слов есть, которые 

![[Pasted image 20230908234952.png]]


### Emission probabilities
- Когда мы не видим Transition probabilities, у нас есть emission probabilities - матчинг от скрытых состояний к реальным наблюдениям
- Мы можем построить также матричку перехода от скрытого состояния к наблюдениями (рис 2, 3)
	- У этой матрички в строках будут скрытые состояния, и сумма строки будет всегда 1 (на скрине ошибка - он выходит за 1, что является ошибкой лекции)

![[Pasted image 20230908235617.png]]![[Pasted image 20230908235818.png]]![[Pasted image 20230908235936.png]]

### Populating Transition matrix
- Вычислим их на трейн-корпусе, который размечен. Просто как отношение перехода от части_речи_1 к части_речи_2 к общему кол-ву переходов из этой части речи
- Потом мо

![[Pasted image 20230909000406.png]]![[Pasted image 20230909000434.png]]![[Pasted image 20230908232714.png]]![[Pasted image 20230908232902.png]]![[Pasted image 20230908232947.png]]


#### Populating emission probabilities
- Слово you появилось 2 раза, а синий тег (часть речи местоимение?) - 3 раза. Т.е. вероятность слова You при скрытом состоянии синий = 2/3
- Общая формулка на изображении 2

![[Pasted image 20230909110957.png]]
![[Pasted image 20230909111103.png]]