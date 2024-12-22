---
Связи: 
tags:
  - Math
links:
---
Правило о том, как оптимизировать [[Gradient]] последовательно.
Очень помогает в нейросетях.


## Formula
![[Pasted image 20230917122645.png]]
Пусть даны функции, определённые в окрестностях на числовой прямой, ,![{\displaystyle f:U(x_{0})\to V(y_{0}),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9c64926a774a81cf98f136c0db36ff4c19143db8) где ![{\displaystyle y_{0}=f(x_{0}),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c96d5caf1af039a51aa8c1c103c2bc4ac02e7ab) и ![{\displaystyle g:V(y_{0})\to \mathbb {R} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/e325c3d9b07fa84248c6ea104ab1187a4bd861fe) Пусть также эти функции дифференцируемы: ![{\displaystyle f\in {\mathcal {D}}(x_{0}),\;g\in {\mathcal {D}}(y_{0}).}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d265d143408070b03d25d07c57c063ed6415822d) Тогда их композиция также дифференцируема: ![{\displaystyle h=g\circ f\in {\mathcal {D}}(x_{0}),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5888b7bcbe2970f7fe335d919dd3bb9a25396c67) и её производная имеет вид:

![{\displaystyle h'(x_{0})=g'{\bigl (}f(x_{0}){\bigr )}\cdot f'(x_{0}).}](https://wikimedia.org/api/rest_v1/media/math/render/svg/058dc8f2f843e0d9a7750915f7383e439e11315e)
![[Pasted image 20230917122450.png]]

![[Pasted image 20230917122433.png]]