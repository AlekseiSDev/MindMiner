---
tags:
  - LLM
---
Large Language Model - Модели [[neural network]] в домене [[NLP]], базирующиеся на архитектуре [[Transformer Architecture]]
Обладают огромным количеством параметров и многие из них умеют решать сразу кучу задач
Ответ языковых моделей, как правило, последовательность слов, который они генерируют слово за словом.
Саммари-обзор лекции Яндекса тут https://300.ya.ru/v_lwCMTKUN?t=963

## History
- Ну сначала Марков там чето генерил [[Markov chains]]
- Потом поехали модельки вероятностные, всякие [[N-gram Language Model]]
- Дальше уже подоспели [[Transformer Architecture]]
- Ну и сейчас их развитие - [[ChatGPT]]-like модели


## Architecture
- Базируются в том или ином виде все на [[Transformer Architecture]]
- Переводят слова в токены, и прогоняют их через множества


## Train
- Принято выделять несколько стадий: [[LLM Pretrain]] и [[LLM Finetuning]]
- Обучение с подкреплением, во время фазы файнтюнинга, может уменьшить [[LLM Hallucinations]]


## Inference and using
