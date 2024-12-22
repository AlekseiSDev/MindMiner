---
Связи: 
tags:
  - DL
links:
---
Что такое Trax - фреймворк поверх TensorFlow


- [[#First look|First look]]
- [[#History|History]]
- [[#Лаконичность trax|Лаконичность trax]]


## First look

![[Pasted image 20230921115849.png]]![[Pasted image 20230921115904.png]]![[Pasted image 20230921115918.png]]![[Pasted image 20230921120159.png]]![[Pasted image 20230921120233.png]]


## History
- Google released TF
- Лукас работал в гугле над Машинным переводом, у них было все ок, но с ТФ было невозможно работать не гуглу из-за маштабов(??)
- Они релизнули Tensor2Tensor либу, которая была намного быстрее?
- Но она была сложноватой для рисерчеров
- И они решили выпустить чето новое - более понятное, но такое же быстрое или быстрее
- Чем Trax хорошо - скрин

![[Pasted image 20230921120406.png]]
![[Pasted image 20230921120530.png]]![[Pasted image 20230921120748.png]]![[Pasted image 20230921120906.png]]


## Benefits
### Лаконичность trax
- Код Адам оптимайзера на [PyTorch] и [[TensorFlow]]
- Код Адам на Тракс

![[Pasted image 20230921225528.png]]![[Pasted image 20230921225603.png]]

### Speed
Построенный поверх JAX и TF челами из гугла, он типо работает супер быстро. Наверное.

## Layers

### Serial Layers
Композиция кучки лееров, ведущая себя как один слой. Удобная асбтракция
![[Pasted image 20230921233909.png]]



## Training 
- Конечно имеет автоградиенты
- На практике выглядит так
![[Pasted image 20230921235437.png]]
![[Pasted image 20230921235509.png]]



## Docs and links
Official Trax documentation maintained by the Google Brain team:

[https://trax-ml.readthedocs.io/en/latest/](https://trax-ml.readthedocs.io/en/latest/ "trax-ml")

Trax source code on GitHub:

[https://github.com/google/trax](https://github.com/google/trax "trax")

JAX library:

[https://jax.readthedocs.io/en/latest/index.html](https://jax.readthedocs.io/en/latest/index.html "JAX")

