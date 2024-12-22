---
Связи:
Теги: #Math
---

Вспомним инференс в [[Naive Bayes]]


![[Pasted image 20230829234757.png]]
we can estimate ratio
![[Pasted image 20230829234853.png]]

Однако для инференса Байеса нам надо душное перемножение юзать. А если там получатся 0 - то везде будут 0.
Можем воспользоваться трюком, что log(a*b) = log(a) + log(b) и провести подмену
![[Pasted image 20230829235648.png]]
Example
Add lambda column to our table and calculate it
![[Pasted image 20230830000503.png]]

## Inference Naive Bayes via LogLikelihood
- Считаем loglikelihood
- Считаем слово положительным, если ЛЛ > 0
![[Pasted image 20230830000655.png]]
![[Pasted image 20230830000747.png]]