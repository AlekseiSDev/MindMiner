---
Связи: 
tags:
  - NLP
---
Нграмм - одно из фундаментальных понятий [[NLP]]. Представляет из себя какое-то последовательное сочитание слов (2-gramm(bigramm), 3-gramm) и его вероятность появиться.
Использовался для решения задачи [[Auto-complete]] в эпоху до [[LLM  - Large Language Models]]

## Examples
![[Pasted image 20230911093830.png]]




 Notation

## Applications
- Auto complete
- Speech reco
- Spelling correctuin
- Augmentative communication(S. Hoking)
- ![[Pasted image 20230911090254.png]]
![[Pasted image 20230911090332.png]]


## N-gramm and probabilities
- Unigram
- Bigram
- Trigram
- N-gram

![[Pasted image 20230911094938.png]]![[Pasted image 20230911095035.png]]![[Pasted image 20230911095148.png]]![[Pasted image 20230911095243.png]]


## Probability of sentence
- Вероятность предложения равно перемножению вероятностей, что все составляющие его части (ungiramm, 2gram, 3gram..) появятся в корпусе. Рис 1, 2
- Однако по факту, часто предложение не разу не появляется в корпусе 
	- Давайте пойдем на хитрость, не будем считать фулл вероятность, а концовку предложения будем считать зависимой только от прошлого 1-2 слов
	- Это предположение Маркова, что 
- 
![[Pasted image 20230911095709.png]]![[Pasted image 20230911095738.png]]![[Pasted image 20230911095833.png]]![[Pasted image 20230911100124.png]]![[Pasted image 20230911100225.png]]