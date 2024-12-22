---
tags:
  - ChatGpt
  - "#LLM"
  - "#Prompts"
links:
---

Prompt engineering is the iterative process of developing a prompt by modifying or changing the prompting technique that you are using.
Summary of all existing prompt techniques: [https://arxiv.org/pdf/2406.06608](https://www.google.com/url?q=https%3A%2F%2Farxiv.org%2Fpdf%2F2406.06608).
## Best Practice


Основные короткие и полезные гайды по созданию [[Prompt]] к [[LLM  - Large Language Models|LLMкам]]

1. Четкая формулировка задач - в чем задание, что ты хочешь как ответ
	- указывай, что именно нужно - "хочу результат с примерами, где будут указаны"
	- проси формат аутпута четко - можно попросить csv или json
 2.   Разбиение задачи на шаги
 3. Отделяй свою инфу от цитаты/исходного текста/кода на редактировании
	- У меня есть код: """code""", исправь все ошибки и добавь комментарии
4. Используй роли при запросе к api
	- system - самый важный систем промпт. user, asistant - пользователь и LLMка в диалоге
5. Использй few-shot - предоставление примеров решений задач
	- вот так пишешь код обычно ("""code""")
- Запрос структурированного вывода: Запрос вывода в определенном формате (например, JSON или HTML) облегчает обработку ответа модели.
- Проверка условий: Рекомендуется указывать модели проверять, выполнены ли определенные условия, прежде чем выполнять задачу. Это повышает точность и релевантность вывода.
- Self-consistency - Evaluates the problem multiple times to ensure the answer is consistent across different evaluations.
- **Дополнительные методы:** Prefill (частичное заполнение ответа)
![[Pasted image 20241027160957.png]]

## Advance methods
- [[Chain of thoughts]] - Одна из базовых техник промпт инженеринга, заключается в том, что попросить модель действовать шаг за шагом


## Halucination reduction
