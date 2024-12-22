---
Связи: 
Теги: 
tags:
  - DL
  - NLP
  - LLM
---
Популярная архитектура [[neural network]], основанная на механизме [[Attention (DL)]]. 

Предложена гуглом в статье [[Attention is all wee need(2017)]]
На ней базируются примерно все [[LLM  - Large Language Models]]
Особую популярность имеют в [[NLP]], где на подобной архитектуре строятся почти все современные модели, однако есть и трансформеры для задач [[Computer Vision]]

## Overview
Суть - у нас есть чисто слои [[Embeddings]] и [[Attention (DL)]]. И все епта
- Предложена в https://arxiv.org/abs/1706.03762
- Использует [[Multi-Head Attention]], которая из себя представляет кучу [[Scaled Dot-Product Attention]] + [[Dense(Linear or Fully-connected or FC) layer]] рис 1
- Классика из пейпера базируется на [[Encoder (nn)]] - [[Decoder (nn)]] архитектуре
	- Encoder рис 2 - куча блоков с атеншенами и нормализациями
		- В оригинале таких 6
	- Decoder
![[Pasted image 20230928112140.png]]
![[Pasted image 20230929221955.png]]![[Pasted image 20230929222044.png]]


### Positional Encoding
Positional encoding can be learned or fixed. 
This has the word embeddings. 
For instance, let's suppose you want to translate from the French race over here, you have [inaudible], and then you want to capture the sequential information. 
The transformers uses a positional encoding to retain the position of the input sequence. 
The positional encoding has values that are added to the embeddings, so that for every inputs word, you have information about its order and position. 
In this case, a positional encoding vector for each word

![[Pasted image 20230929222221.png]]


## Complexity
В ванильном варианте с [[Scaled Dot-Product Attention]] это O(n^2)
![[Pasted image 20230930202540.png]]