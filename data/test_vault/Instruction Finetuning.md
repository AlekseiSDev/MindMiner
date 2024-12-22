---
tags:
  - LLM
---
Инстракшен файнтюнинг - тип [[LLM Finetuning]], который использовался для преобразования ГПТ3 в ЧатГпт например.

- [[#Что такое инстракшен файнтюниг|Что такое инстракшен файнтюниг]]
- [[#Данные для Instruction finetuning|Данные для Instruction finetuning]]
- [[#What kind of data|What kind of data]]
- [[#Steps to prepare your data|Steps to prepare your data]]
	- [[#Steps to prepare your data#Tokenizing|Tokenizing]]
		- [[#Tokenizing#Padding and Truncation|Padding and Truncation]]
	- [[#Steps to prepare your data#Prepare dataset|Prepare dataset]]
		- [[#Prepare dataset#Tokenize prepared dataset|Tokenize prepared dataset]]
		- [[#Prepare dataset#example of datasets|example of datasets]]
	- [[#Steps to prepare your data#Train-test|Train-test]]



## Что такое инстракшен файнтюниг
- Позволяет дотюнить, обычно на конкретные ответы
- Для моделей, общающихся лайк чат, возможна переносимость этого подхода - например, никто не учил ChatGPT отвечать в стиле чата вопросами про код - просто она перенесла этот подход на имеющиеся у нее знания
- Жизненный цикл - дата подготовка, трена, оцена. Повторить
![[Pasted image 20230827093920.png]]
![[Pasted image 20230827094453.png]]
![[Pasted image 20230827094513.png]]

## Данные для Instruction finetuning
- Часть данных готова сразу для инструкций
- Можно использовать другие ЛЛМки, чтоб конвертнуть инфу в соотв данные
	- Например чуваки из Стенфорда представили технику Alpaca for ChatGPT

![[Pasted image 20230827094038.png]]![[Pasted image 20230827094137.png]]


Файнтюнинг
- Датасетик можно выкачать и посмотреть


![[Pasted image 20230827095556.png]]
![[Pasted image 20230827095707.png]]


# Data preparation
## What kind of data
- ~1k examples can be enough
![[Pasted image 20230827103800.png]]


## Steps to prepare your data

![[Pasted image 20230827103935.png]]

### Tokenizing
- Choose tokenizer associated with model
- HG very helpfull
![[Pasted image 20230827104010.png]]
![[Pasted image 20230827104158.png]]
#### Padding and Truncation
- Usually using both
- size of truncation and padding depends on model
![[Pasted image 20230827104339.png]]

### Prepare dataset
![[Pasted image 20230827104717.png]]

#### Tokenize prepared dataset
![[Pasted image 20230827104922.png]]
![[Pasted image 20230827105000.png]]![[Pasted image 20230827105034.png]]
#### example of datasets
![[Pasted image 20230827105342.png]]

### Train-test

![[Pasted image 20230827105412.png]]


# Training Process

![[Pasted image 20230827110718.png]]