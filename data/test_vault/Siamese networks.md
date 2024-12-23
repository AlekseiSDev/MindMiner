---
Связи: 
tags:
  - DL
links:
---
Типо [[neural network]], который выглядит как 2 сети близнеца, с одинаковой архитектурой.
Используется для задачи [[Duplication identification task]]

## Abstract
- Учим посути 2 LSTMки так, чтоб [[Cosine Similarity]] между похожими ответами было максимально близким
	- Сравниваем близость с трешхолдом и решаем, одна ли у нас фраза
- Набор параметров един, т.е. веса общие

![[Pasted image 20230925174622.png]]


## Training

### Preparing batches
- Матрица n\*2, где в строках дубли, в колонках - нет
- Можно это рассматривать также как 2 разных батчка
![[Pasted image 20230926091339.png]]

### Computing cost
- Берем 1ю часть батча - пропускаем чрез начало сетки - получается матричка n\*m
	- где n - кол-во элементов в батче, m - размер эмбеда для элементов
- Повторяем точно также с 2й патчей батча рис 2
- В матрице V1 нет дупликатов, но v1_1 дупликат v2_1
- Строим матричку похожести (с помощью [[Cosine Similarity]] например) - как похожи v1_1 и v2_1 и остальные. 
	- По диагонале матрицы у нас дубли - ьам должны быть самые высокие чиселки
- Теперь, чтоб посчитать лосс, мы можем подсчитать loss каждый пары c помощью [[Triplet Loss]] и сложить, чтоб получить лосс сеточки
	- Получается типо количество полуматрица с кол-вом комбинаций
		-  4+3+2+1 в нашем примере
![[Pasted image 20230926091921.png]]![[Pasted image 20230926092000.png]]![[Pasted image 20230926092447.png]]

### Advanced batching and cost
#### Mean negative
- Просто среднее всех недиагональных значений в строке
- В примере будет просто mean(-0.8, 0.3, -0.5) = 1/3
- Формулка для тренировки в таком случае принимает вид рис 2
- Это почистит шум
![[Pasted image 20230926093813.png]]
![[Pasted image 20230926094138.png]]

#### Closest negative
- Взять не-диагональное значение, которое наиболее близко к диагональному в каждой строке. В первой строке будет 0.3
	- Значит, что этот пример самый ценный с т.з. обучения
- Лосс в таком случае будет L2
- Мы учим модельку на наиболее сложных примерах
![[Pasted image 20230926094424.png]]

#### Result

![[Pasted image 20230926094526.png]]