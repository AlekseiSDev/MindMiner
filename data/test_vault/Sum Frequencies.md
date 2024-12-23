---
Связи:
Теги: #ML #NLP
---
Подход [[Feature Engineering]], при котором считается количество вхождений исходных фич(слов в кейс НЛП) в тот или иной класс.
Например есть набор твитов, и задача их классификации на позитивные/негативные.
Мы берем позитивные твиты, идем по их словам, и составляем словарь, где добавляем каждому слову, сколько раз оно было встречено в позитивных твитах.
После, мы можем для каждого твита посчитать 2 новых фичи - сколько в нем позитивных слов, и сколько негативных
![[Pasted image 20230824140850.png]]
![[Pasted image 20230824140754.png]]