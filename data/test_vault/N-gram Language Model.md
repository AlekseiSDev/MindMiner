---
Связи: "[[N-Grams]]"
tags:
  - NLP
---
Языковая модель, позволяющая предсказывать следующее слово на основе алгоса [[N-Grams]]. 

База - расчитать вероятности разных слов на основе корпуса.
Затем подать контекст и продолжить для него наиболее вероятное слово.

- [[#Start and end of sentences|Start and end of sentences]]
- [[#LM based on N-gram|LM based on N-gram]]
	- [[#LM based on N-gram#Count matrix|Count matrix]]
	- [[#LM based on N-gram#Probability matrix|Probability matrix]]
	- [[#LM based on N-gram#Language model|Language model]]
	- [[#LM based on N-gram#Log probability trick|Log probability trick]]
- [[#Generative LM|Generative LM]]


## Start and end of sentences 
- Мы просто добавляем токены \<s> и \</s>

![[Pasted image 20230911114258.png]]![[Pasted image 20230911114325.png]]![[Pasted image 20230911114514.png]]
![[Pasted image 20230911114705.png]]

## LM based on N-gram

![[Pasted image 20230911130457.png]]

### Count matrix
![[Pasted image 20230911130558.png]]

### Probability matrix
![[Pasted image 20230911130717.png]]

### Language model
- We can predict sentence probability
- or create new 
![[Pasted image 20230911130805.png]]


### Log probability trick
![[Pasted image 20230911130859.png]]


## Generative LM
![[Pasted image 20230911131006.png]]


## Restrictions
- При небольшом корпусе очень сложно верно оценить вероятности
- Нужно считать много вероятностей
	- И хранить очень много комбинаций 
![[Pasted image 20230922133845.png]]![[Pasted image 20230922133946.png]]