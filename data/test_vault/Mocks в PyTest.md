---
Связи:
Теги: #Dev #Testing
---
Мок - инструменты для создания заглушек, нужного безусловного значения.
 

Виды моков в UnitTest рис 1
- Отличие между 1 и 2 - в магических методах (их наличии)
- Отличие 3го - отсуствие call
Примеры использования моков рис 3

Моки в [[Pytest]] - плагин вокруг пакета Mock, вот его дока
https://pytest-mock.readthedocs.io/en/latest/
установка https://pypi.org/project/pytest-mock/


Как правильно оформлять моки?
- Через create_autospec - это лучше, чем использовать чистые моки [pic 4](obsidian://open?vault=Obsidian&file=Pasted%20image%2020230801225906.png)
- seal - запечатывает моки рис 5
-  Ну а лучший способ - использовать пайт-тест моки https://github.com/pytest-dev/pytest-mock. Как моки выглядят при этом, видно на рис 6. Из плюсов - он фикстура, откатывает свои изменения
	- spy - позволяет проверить, как и сколько раз был выполнен код например, но не изменяет поведение (полумок) рис 7 - хорошо
	- stub - не юзает даже никита: рис 8
	- https://github.com/gabrielfalcao/httpretty - топчик, мокает Http вызовы



![[Pasted image 20230801224511.png]]

![[Pasted image 20230801224834.png]]
![[Pasted image 20230801225637.png]]
![[Pasted image 20230801225906.png]]![[Pasted image 20230801230508.png]]![[Pasted image 20230801230750.png]]![[Pasted image 20230801231002.png]]![[Pasted image 20230801231044.png]]