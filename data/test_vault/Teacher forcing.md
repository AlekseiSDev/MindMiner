---
Связи: 
tags:
  - DL
  - Tricks
links:
---
Одна из техник для улучшения задач с [[Attention (DL)]] (вроде бы)

## Abstract
Заключается в том, чтоб подсовывать декодеру как прошлое слово чето адекватное, а сгенерированное им прошлое слово

## Problem
- Пока наша модель не обучена, мы будем предиктикить очень тупые предикты 
- А т.к. некст слово зависит от предыдущего - то все некст слова поплывут

## Decision
- Чтоб фиксануть, используем ground truth для decoder input(t), вместо decoder output(t-1)
![[Pasted image 20230926192341.png]]![[Pasted image 20230926192428.png]]


## Read
https://towardsdatascience.com/what-is-teacher-forcing-3da6217fed1c