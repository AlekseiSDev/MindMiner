---
Связи: 
tags: 
links:
---
Один из видов [[Attention (DL)]]
Предложенный в [[Attention is all wee need(2017)]] Vaswani et all., 2017


## Steps and math
Выглядит как схемка слево, или мат-формулка справа, шаги:
- Умножаем вектора Q \*K  и получаем матричку. Это набор оценок внимания.
- Нормируем на размер вектора ключей K, это делается для стабилизации градиентов
- Берем [[Softmax]] (делаем распределение 0-1 с суммой 1), это преобразует оценки в вероятности, сумма которых равна 1, позволяет распределить внимание
- Умножаем на вектор Values, это дает взвешенную сумму, которая представляет выход внимания.
Всего 2 матричных умножения и нет дополнительно встроенного полносвязного слоя


![[Pasted image 20230926180119.png]]
![[Pasted image 20230926180129.png]]![[Pasted image 20230926180320.png]]


## Code

```python
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    """
    Computes scaled dot-product attention.

    Args:
        q (torch.Tensor): Query tensor of shape (batch_size, seq_len, d_model).
        k (torch.Tensor): Key tensor of shape (batch_size, seq_len, d_model).
        v (torch.Tensor): Value tensor of shape (batch_size, seq_len, d_model).

    Returns:
        torch.Tensor: Attention output tensor of shape (batch_size, seq_len, d_model).
    """
    # Step 1: Compute the raw similarity scores between queries and keys
    # Output shape: (batch_size, seq_len, seq_len)
    raw_scores = torch.matmul(q, k.transpose(-2, -1))

    # Step 2: Scale the similarity scores by the square root of d_model
    # Output shape remains: (batch_size, seq_len, seq_len)
    d_model = q.size(-1)
    scaled_scores = raw_scores / torch.sqrt(torch.tensor(d_model, dtype=torch.float32))

    # Step 3: Apply softmax to obtain attention weights
    # Output shape: (batch_size, seq_len, seq_len)
    attn_weights = F.softmax(scaled_scores, dim=-1)

    # Step 4: Multiply attention weights with values to get the final attention output
    # Output shape: (batch_size, seq_len, d_model)
    attention_output = torch.matmul(attn_weights, v)

    return attention_output
```


