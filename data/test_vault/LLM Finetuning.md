---
tags:
  - LLM
---
Finetuning - process of additional training model to solve your tasks.
Here we will speak about finetuning [[LLM  - Large Language Models]]
Based on course by Andrew Ng https://learn.deeplearning.ai/finetuning-large-language-models


- [[#What does finetuning do for the model|What does finetuning do for the model]]
	- [[#LLM Prompting vs Finetuning|LLM Prompting vs Finetuning]]
	- [[#Benefits of finetuning LLM|Benefits of finetuning LLM]]
	- [[#Finetuned vs non-finetuned examples|Finetuned vs non-finetuned examples]]


# What is finetuning 
it's process of additional training model to solve your tasks.
![[Pasted image 20230826191315.png]]

## What does finetuning do for the model
Он позволяет засунуть в модель больше данных, чем в промпте. Подталкивает модель выучить эти данные, а не просто получить к ним доступ
![[Pasted image 20230826191719.png]]
![[Pasted image 20230826192036.png]]


## LLM Prompting vs Finetuning
[[LLM Prompting vs Finetuning]]

## Benefits of finetuning LLM

![[Pasted image 20230826192719.png]]


## Finetuned vs non-finetuned examples
non-finetuned examle
![[Pasted image 20230826193050.png]]
finetuned model
![[Pasted image 20230826193315.png]]


# Where finetuning fits in

## Pretraining - review
![[Pasted image 20230826210909.png]]![[Pasted image 20230826210938.png]]
![[Pasted image 20230826211006.png]]
![[Pasted image 20230826211207.png]]

## More about what is finetuning
![[Pasted image 20230826211730.png]]![[Pasted image 20230826211902.png]]

## Tasks to finetune (Задачи, подходящие на файнтюн)
Ключевое при файнтюнинге - ясно представлять задачу и как ей научить. 
![[Pasted image 20230826212028.png]]

## Чек-лист 1го файнтюнинга
- Определиться с задачей играясь с большой (ЧатГПТ) моделькой
- Найти задачи, которые она обрабатывает неплохо. Неплохо, но не более
- Выбрать 1 задачу
- Набрать датасет из ~1000 примеров, с лучшим аутпутом чем ок
- Зафайнтюнить небольшую ЛЛМ на эту датку

![[Pasted image 20230826212348.png]]


## Шаблоны для файнтюнинга
- Часто в форме вопрос-ответ
- В зависимости от АПИ файнтюнинга, их подают 
	- либо напрямую (вот вопрос, вот ответ)
	- либо как единый текст, где выделены и помечены текстом Question and Answeer
	- Подробнее в лабе по Where finetunin fits in
![[Pasted image 20230826213714.png]]
![[Pasted image 20230826213730.png]]
![[Pasted image 20230826213958.png]]
![[Pasted image 20230826213808.png]]