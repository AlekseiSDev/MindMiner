---
Связи: 
tags:
  - NLP
links:
---
Одна из моделей [[Word embedding (vectors)]]

- [[#Abstract|Abstract]]
- [[#Preprocess and preparations|Preprocess and preparations]]
	- [[#Preprocess and preparations#Python code|Python code]]
	- [[#Preprocess and preparations#Sliding Window|Sliding Window]]
	- [[#Preprocess and preparations#First w2v transform|First w2v transform]]
- [[#Architecture of the CBOW Model|Architecture of the CBOW Model]]
	- [[#Architecture of the CBOW Model#Dimensions|Dimensions]]
	- [[#Architecture of the CBOW Model#Activations|Activations]]


## Abstract
- Цель модели - предсказать слово используя контекст
- Параметры модели - С - размер контекста слева и справа
- Вход модели - контекст, выход - предсказание аут слова
- Мы тренируем матрицу весов получается
	- Подавая ей на вход оч наивное векторное представление контекста
- 


![[Pasted image 20230916180443.png]]![[Pasted image 20230916180522.png]]![[Pasted image 20230916180551.png]]

## Preprocess and preparations
![[Pasted image 20230916180904.png]]
### Python code
![[Pasted image 20230916180926.png]]

### Sliding Window
![[Pasted image 20230916181044.png]]


### First w2v transform
- center представялем тупо как ohe
- контекст - как сумму ohe его участников, деленное на длину
![[Pasted image 20230916181231.png]]![[Pasted image 20230916181933.png]]![[Pasted image 20230916181957.png]]


## Architecture of the CBOW Model
- Простая FNNка
![[Pasted image 20230916191210.png]]

### Dimensions
- Напоминание о размерностях слоя в FNN
- Размерности в CBOW
![[Pasted image 20230916191807.png]]![[Pasted image 20230916191856.png]]![[Pasted image 20230916191932.png]]

### Activations
- [[Rectified Linear Unit (ReLU)]] на внутреннем слое
- [[Softmax]] перед аутпутом


### Cost function
- [[Cross-entropy loss]]


## Training
- make forward propogation
- get loss
### Forward 
- Просто засунем 
![[Pasted image 20230917120041.png]]


### Backpropagation and GD
- Считаем производные после нахождения лосса, начиная с последнего слоя
- Используем chain rule и градиентный спуск ![[Pasted image 20230917122737.png]]![[Pasted image 20230917122921.png]]![[Pasted image 20230917123024.png]]


## Extracting embedings
1) можно взять соответсвующую трейн корпусу колонку из матрицы W1
2)  Или соответсвующую строку из матрицы W2
3) А можно усреднить их

![[Pasted image 20230917123213.png]]![[Pasted image 20230917123308.png]]![[Pasted image 20230917123347.png]]


## Evaluations
### Intrinsic evaluation
- Проверять отношения между словами
	- Иметь ввиду, что часто допустимы неоднозначности
- Есть пейпер Intinsic and extrinsic avluations
![[Pasted image 20230917123550.png]]![[Pasted image 20230917123658.png]]![[Pasted image 20230917123802.png]]

### Extrinsic evaluation
- Протестировать систему, для которой мы готовим эмбеды
![[Pasted image 20230917123949.png]]