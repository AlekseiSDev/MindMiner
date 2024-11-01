---
Связи: 
tags: 
links:
---
Это [[Loss(Cost) Function]], часто используемая в нейронках на задачах классификации.
Обобщение [[LogLoss]] для задачи многоклассовой классификации.

## Formula
![[Pasted image 20230917115321.png]]

### Cost function
- [[Cross-entropy loss][
![[Pasted image 20230924094936.png]]]


## Example
- На первом корректный, на втором - нет, предикт
![[Pasted image 20230917115340.png]]![[Pasted image 20230917115436.png]]

## Intuition
- близок к 0, 
	- когда у нас y = y^ = 1, т.к. log1 ~ 0 => 1 * 0 = 0
	- когда y = y^ = 0, т.к. множитель y ~0 => 0 * 1 = 0
![[Pasted image 20230917115513.png]]