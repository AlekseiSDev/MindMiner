---
Связи: 
tags:
  - LLM
links:
---
Один из важнейших концептов в текущем [[Deep Learning]]

- [[#Base|Base]]
- [[#Idea|Idea]]

## Base
Представлено в 
![[Pasted image 20230926141014.png]]


Насколько накинуло модельке [[Seq2seq]]
![[Pasted image 20230926141220.png]]


## Idea
- Ванила seq2seq предполагает одно финальное состояние h, которое кидается в [[Decoder (nn)]]
- Мы можем кинуть вместо этого все состояния, сконкатенировав их например. Но тогда декодер путается - слишком много контекста
- Но мы можем брать состояния декодера, и смотря на них, решать, какие веса каким частям энкодера дать. Это и является механизмом аттеншена
	- Внутри посути некоторый [[Dense(Linear or Fully-connected or FC) layer]], который для каждого скрытого состояния энкодера получает на вход веса декодера, и пропуская их через себя, отдает веса, с которыми нужно смотреть на состояние энкодера
![[Pasted image 20230926154730.png]]![[Pasted image 20230926154914.png]]![[Pasted image 20230926155022.png]]![[Pasted image 20230926155442.png]]


## Queries, Keys, Values attention

![[Pasted image 20230926175820.png]]![[Pasted image 20230926175851.png]]

### Some math
Выглядит как схемка слево, или мат-формулка справа
- Сначала мы умножаем Q \*K  и получаем матричку
- Нормируем на размер вектора ключей K
- Берем [[Softmax]] (делаем распределение 0-1 с суммой 1)
- Умножаем на вектор Values
- Всего 2 матричных умножения и нет дополнительно встроенного полносвязного слоя


![[Pasted image 20230926180119.png]]
![[Pasted image 20230926180129.png]]![[Pasted image 20230926180320.png]]


## Alignment Weights
- Во время трены модель учит, какое слово представляет какое на другом языке и энкодит эту инфу в key-value вектор
- Выучить такие алайменты позволяет моделькам строить хорошие представления

![[Pasted image 20230926181750.png]]
![[Pasted image 20230926181931.png]]



## No O(n^2)
5 статей о том, как уйти от квадратичной сложности
![[Pasted image 20231206123158.png]]



## Materials
### - [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) (Raffel et al, 2019)

### - [Reformer: The Efficient Transformer](https://arxiv.org/abs/2001.04451) (Kitaev et al, 2020)

### - [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al, 2017)

### - [Deep contextualized word representations](https://arxiv.org/pdf/1802.05365.pdf) (Peters et al, 2018)

### - [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) (Alammar, 2018)

### - [The Illustrated GPT-2 (Visualizing Transformer Language Models)](http://jalammar.github.io/illustrated-gpt2/) (Alammar, 2019)

### - [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) (Devlin et al, 2018)

### - [How GPT3 Works - Visualizations and Animations](http://jalammar.github.io/how-gpt3-works-visualizations-animations/) (Alammar, 2020)