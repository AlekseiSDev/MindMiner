---
tags:
  - Algo
  - "#CodingInterview"
links: "[[Coding Interview]]"
---
Нотация для обозначения сложности алгоритмов 
Имеется ввиду насколько (линейно, квадратично, логарифмически или как еще) вырастает сложность алгоритма в зависимости от размера входа
Есть 2 вида сложности, нотация большой О используется для обоих
- time complexety
- memory complexity

Table of content
- [[#Main terms|Main terms]]
- [[#Big O notation|Big O notation]]
- [[#Names and graphs of many funcs|Names and graphs of many funcs]]
- [[#Other Common Asymptotic|Other Common Asymptotic]]
	- [[#Other Common Asymptotic#Big omega  Ω(.)|Big omega  Ω(.)]]
	- [[#Other Common Asymptotic#Big ‘Theta’ - Θ(.)|Big ‘Theta’ - Θ(.)]]
	- [[#Other Common Asymptotic#Little ‘o’ - o(.)|Little ‘o’ - o(.)]]
	- [[#Other Common Asymptotic#Little ‘omega’ - o(.)|Little ‘omega’ - o(.)]]
- [[#Examples and tips|Examples and tips]]
	- [[#Examples and tips#O(n)|O(n)]]
	- [[#Examples and tips#O(n**2), O(n*m)|O(n**2), O(n*m)]]




## Main terms
- Asymptotic analysis - идет из математической asymptotic notation, котора предназначена для сравнения роста функций, скажем f(n) и g(n) на больших значениях n

## Big O notation 
Big O notation - One of the asymptotic notations
Функция f(n) принадлежит O(g(n)), читается как О большое от g(n), если существует такая позитивная реальная константа c, и число n0 >= 0 такие, что следующее уравнение выполняется для всех n >= n0
	f(n) <= c*g(n)
Т.е. если у нас есть функция f(n) и мы хотим найти для нее O(n) - то мы ищем такую функцию, которая при домножении на константу после определенного n всегда будет больше-равна f(n), или будет расти не медленее f(n)


![[Pasted image 20231121124955.png]]


## Names and graphs of many funcs
![[Pasted image 20231121142827.png]]



## Other Common Asymptotic
https://www.educative.io/module/page/8q5JgjuQREjpzD9gq/10370001/6244455909949440/5370588928671744
Есть еще популярные виды асимптотик
### Big omega  Ω(.)
Обозначает нижнюю границу скорости работы функции, посути ее лучший случай.
Описывается математически, как
- Можно найти константу c такую, что для любого n > n0, будет верно
	- f(n) >= c*g(n), т.е. функция будет расти не медленее, чем ее Биг омега
![[Pasted image 20231127122405.png]]


### Big ‘Theta’ - Θ(.)
Это наиболее точное описание сложности, функция, которая является для текущего алгоритма и биг О и биг Омегой одновременно
Математически:
Можно найти такие константы c и c2, что для любого n > n0, будет верно
	- c2*g(n) >= f(n) >= c1*g(n), т.е. функция будет расти не медленее,  и не быстрее, чем ее Биг Тетта
![[Pasted image 20231127125327.png]]


### Little ‘o’ - o(.)
Это когда мы находим функцию, которая строго больше нашей для всех n>n0

### Little ‘omega’ - o(.)
Это когда мы находим функцию, которая строго меньше нашей для всех n>n0



## Examples and tips
1. Every time a list or array gets iterated over ×length times, it is most likely in O(n) time.
2. When you see a problem where the number of elements in the problem space gets halved each time, that will most probably be in O(logn) runtime.
3. Whenever you have a singly nested loop, the problem is most likely in quadratic time.

### O(n)
**Simple for loop**
**Running time complexity** n = O(n)
![[Pasted image 20231127130150.png]]


**For loop with increments**
**Running time complexity** floor(n/k​) = O(n)
![[Pasted image 20231127130250.png]]



### O(n**2), O(n*m)

**Simple nested for loop**
**Running time complexity** n×m=O(nm)![[Pasted image 20231127130657.png]]


**Nested for loop with dependant variables**
![[Pasted image 20231127131123.png]]
![[Pasted image 20231127131211.png]]
![[Pasted image 20231127130741.png]]


 **Nested for loop with index modification**
**Running time complexity** n*(n−1)=n\*\*2−n=O(n\*\*2)
![[Pasted image 20231127130818.png]]


### log(n)
![[Pasted image 20231127131019.png]]
**Running time complexity** = logk​(n) = O(logk​(n))



### Hard cases

O(n) 
![[Pasted image 20231127132125.png]]![[Pasted image 20231127132308.png]]![[Pasted image 20231127132318.png]]