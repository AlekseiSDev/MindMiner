---
Связи: 
tags: 
links:
---
Вид [[Attention (DL)]] предложенный в [[Attention is all wee need(2017)]]
Включает в себя [[Scaled Dot-Product Attention]] и [[Dense(Linear or Fully-connected or FC) layer]]?

Посути - некст версия Scaled Dot-Product атеншена, где мы входную последователньость разбиваем на доп измерение (скажем, 1\*512 => 1\*8\*64), считаем меньшие аттеншены параллельно, затем конкатенируем и прогоняем через линейный слой


Авторы говорят, что так лучше работает
![[Pasted image 20230928112140.png]]
## Code
```python
import torch
import torch.nn.functional as F

class MultiHeadAttention:
    def __init__(self, d_model: int, num_heads: int):
        """
        Initializes the Multi-Head Attention module.

        Args:
            d_model (int): Dimension of the model.
            num_heads (int): Number of attention heads.
        """
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model
        self.num_heads = num_heads
        self.dim_head = d_model // num_heads

        # Define linear layers for projecting Q, K, V
        self.w_q = torch.nn.Linear(d_model, d_model)
        self.w_k = torch.nn.Linear(d_model, d_model)
        self.w_v = torch.nn.Linear(d_model, d_model)

        # Linear layer to combine multi-head outputs
        self.w_out = torch.nn.Linear(d_model, d_model)

    def scaled_dot_product_attention(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        """
        Computes scaled dot-product attention.

        Args:
            q (torch.Tensor): Query tensor of shape (batch_size, num_heads, seq_len, dim_head).
            k (torch.Tensor): Key tensor of shape (batch_size, num_heads, seq_len, dim_head).
            v (torch.Tensor): Value tensor of shape (batch_size, num_heads, seq_len, dim_head).

        Returns:
            torch.Tensor: Attention output tensor of shape (batch_size, num_heads, seq_len, dim_head).
        """
        raw_scores = torch.matmul(q, k.transpose(-2, -1))
        scaled_scores = raw_scores / torch.sqrt(torch.tensor(self.dim_head, dtype=torch.float32))
        attn_weights = F.softmax(scaled_scores, dim=-1)
        attention_output = torch.matmul(attn_weights, v)
        return attention_output

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        """
        Computes multi-head attention.

        Args:
            q (torch.Tensor): Query tensor of shape (batch_size, seq_len, d_model).
            k (torch.Tensor): Key tensor of shape (batch_size, seq_len, d_model).
            v (torch.Tensor): Value tensor of shape (batch_size, seq_len, d_model).

        Returns:
            torch.Tensor: Multi-head attention output of shape (batch_size, seq_len, d_model).
        """
        batch_size, seq_len, _ = q.size()

        # Step 1: Project input tensors to multiple heads
        q = self.w_q(q).view(batch_size, seq_len, self.num_heads, self.dim_head).transpose(1, 2)
        k = self.w_k(k).view(batch_size, seq_len, self.num_heads, self.dim_head).transpose(1, 2)
        v = self.w_v(v).view(batch_size, seq_len, self.num_heads, self.dim_head).transpose(1, 2)

        # Step 2: Apply scaled dot-product attention
        attn_output = self.scaled_dot_product_attention(q, k, v)

        # Step 3: Concatenate outputs from all heads
        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)

        # Step 4: Apply final linear transformation
        output = self.w_out(attn_output)
        return output

# Example usage
if __name__ == "__main__":
    # Input embedding tensor of shape (batch_size, seq_len, d_model)
    batch_size = 2
    seq_len = 5
    d_model = 16
    num_heads = 4

    # Simulated input embeddings
    x = torch.randn(batch_size, seq_len, d_model)

    # Define external linear layers for Q, K, V projections
    w_q = torch.nn.Linear(d_model, d_model)
    w_k = torch.nn.Linear(d_model, d_model)
    w_v = torch.nn.Linear(d_model, d_model)

    # Create Q, K, V using external linear layers
    q = w_q(x)
    k = w_k(x)
    v = w_v(x)

    # Initialize Multi-Head Attention module
    mha = MultiHeadAttention(d_model, num_heads)

    # Forward pass through Multi-Head Attention
    output = mha.forward(q, k, v)
    print("Output shape:", output.shape)
```

