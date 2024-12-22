---
tags:
  - NLP
  - LLM
links:
---
Концепция [[Attention (DL)]] в [[Transformer Architecture]], предложена в [[Attention is all wee need(2017)]]
Self-attention - this is exactly concept for particular implementation (like [[Scaled Dot-Product Attention]] or [[Multi-Head Attention]]). Self - because of он обращает внимание на позиции (токены) и сравнивает с другими позициями в одной и той же последовательности (входе) для генерации новой последовательности (Q, K, V - один и тот же вектор, поэтому данная операция зовется self-attention)


- **Self-Attention (Общее название подхода):**
    
    - Это концепция или механизм, который позволяет каждому элементу входной последовательности взаимодействовать с другими элементами этой же последовательности.
    - Пример: в задаче обработки текста self-attention позволяет каждому слову учитывать значение других слов в предложении.
- **Scaled Dot-Product Attention (Конкретная реализация механизма):**
    
    - Это способ реализации self-attention, который используется для вычисления вниманий через матричное умножение QQQ и KKK, масштабирование и применение softmax.
    - Scaled Dot-Product Attention — это строительный блок, который часто используется как часть более сложных механизмов, например, multi-head attention.
- **Multi-Head Attention (Конкретный слой нейросети):**
    
    - Это расширенная версия Scaled Dot-Product Attention.
    - Реализует self-attention с разделением на несколько "голов" для параллельного изучения различных аспектов данных.
    - Multi-Head Attention — это полноценный слой в трансформерах, таких как BERT или GPT.