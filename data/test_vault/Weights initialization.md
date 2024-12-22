---
tags:
  - "#DL"
  - "#Math"
links:
---
А вот создали мы новую сеточку, [[neural network]], а как ее веса инициализировать?
Норм статья https://www.deeplearning.ai/ai-notes/initialization/index.html
Вот еще интересное обсуждение https://stackoverflow.com/questions/49433936/how-do-i-initialize-weights-in-pytorch
Дефолтная инициализия в пайторче:
The type of initialization depends on the layer. You can check it from the [`reset_parameters`](https://pytorch.org/docs/stable/_modules/torch/nn/modules/linear.html#Linear) method or from the docs as well.

For both linear and conv layers, it's He initialization ([`torch.nn.init.kaiming_uniform_`](https://pytorch.org/docs/stable/nn.init.html#torch.nn.init.kaiming_uniform_)).

- https://stackoverflow.com/questions/65606553/how-pytorch-model-layer-weights-get-initialized-implicitly

А как бы мы сами хотели?
- Дефолтно случайно - нам не хочется там одних чиселок и 0й. А как, стандартным нормальным? Можно, но лучше нормировать немношк
- Проблема - дисперсия выходного - это n*дисперию входа, поэтому лучше делить на n?
![[Pasted image 20241207103829.png]]

По дефолту ща в pytorch - 