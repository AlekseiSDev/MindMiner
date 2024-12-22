---
Связи:
Теги: #Dev #Testing
---
Во первых ссылка на доку - https://docs.pytest.org/en/7.1.x/how-to/writing_hook_functions.html
В [[Pytest]] Хуки - это типо выполняемый пайтестом код, который позволяет ранить всякое перед (или в процессе) работы тестов. Работает в сочитании с [[Плагины в Pytest]], вероятно в плагинах пишется код.
Цитата
_Hooks are a key part of pytest’s plugin system and are used by plugins and by pytest itself to extend the functionality of pytest. Hooks allow plugins to register custom code to be run at specific points during the execution of pytest, such as before and after tests are run, or when exceptions are raised. They provide a flexible way to customize the behavior of pytest and to extend its functionality._
https://paragkamble.medium.com/understanding-hooks-in-pytest-892e91edbdb7#:~:text=Hooks%20are%20a%20key%20part%20of%20pytest's%20plugin%20system%20and,or%20when%20exceptions%20are%20raised.
- Пример 1 - хук, загружающий из файла тесты
![[Pasted image 20230731232238.png]]
![[Pasted image 20230731232228.png]]![[Pasted image 20230731232327.png]]