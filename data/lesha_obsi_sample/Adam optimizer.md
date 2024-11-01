---
Связи: 
tags:
  - DL
  - Math
links:
---
Один из самых популярных оптимизаторов[[Optimizers]].

## Суть
**Adam** is an adaptive learning rate optimization algorithm that utilises both momentum and scaling, combining the benefits of [RMSProp](https://paperswithcode.com/method/rmsprop) and [SGD w/th Momentum](https://paperswithcode.com/method/sgd-with-momentum). The optimizer is designed to be appropriate for non-stationary objectives and problems with very noisy and/or sparse gradients.

The weight updates are performed as:
![[Pasted image 20230921225335.png]]
![[Pasted image 20230921225405.png]]

## Материалы

- Paper https://arxiv.org/abs/1412.6980
- Simple explanation https://paperswithcode.com/method/adam
