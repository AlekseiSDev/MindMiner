---
Связи:
Теги: #Dev #Testing
---
В [[Pytest]] есть инструменты, чтоб не менять после себя состояние окружение. Вернее, чтоб поднменить его в процессе тестов, и вернуться к прошлому (чистому) состоянию после.
- Например в чем проблема кода на рис 2? Он изменяет значение в переменной среды
- Чел даже написал плагин о том, чтоб проверять такие кейсы рис 3
- Правильно делать как на рис 4 - там вызывается специальный Path, который по факту [[Фикстуры]] и после себя чистит


![[Pasted image 20230731235520.png]]

![[Pasted image 20230731235759.png]]
![[Pasted image 20230731235744.png]]
![[Pasted image 20230731235922.png]]