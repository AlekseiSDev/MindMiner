---
Связи: 
tags:
  - SysDes
links:
---
В [[Distributed system]] нод обмениваются инфой и сообщениями.
Но невозможно гарантировать, что сообщение будет доставлено точно 1 раз.
https://www.educative.io/courses/distributed-systems-practitioners/the-tale-of-exactly-once-semantics#Avoiding-multiple-deliveries-of-a-message

Сеть не идеальна, оно может потеряться. Тогда мы будем ждать ответа от ноды получателя, и не получив его, отправим заново. Получится, что мы выдаем 2 сообщения одинаковых. 

Есть 2 вида потенциальной обработки
## Idempotent operations approach
Это если мы делаем систему, которой пофиг, что пришло сообщение повторно.
- примером идемпотентной операции является добавление значения в набор значений.
- Примером неидемпотентной операции является увеличение счетчика на единицу.

## De-duplication approach
В подходе дедупликации мы даем каждому сообщению уникальный идентификатор, и каждое повторное сообщение содержит тот же идентификатор, что и исходное. Таким образом, получатель может запомнить набор идентификаторов, которые он получил и уже выполнил. Это также позволит избежать выполнения уже выполняемых операций.

## Difference between delivery and processing
When we think about **exactly-once semantics**, it’s useful to distinguish between the notions of delivery and processing.

In the context of the above discussion, let’s consider **delivery** to be the arrival of the message at the destination node, at the hardware level.

Then, we consider **processing** to be the handling of this message from the software application layer of the node.

In most cases, we care more about how many times a node processes a message, than about how many times it delivers it. For instance, in our previous email example, we were mainly interested in whether the application would display the same email twice, and not whether it would receive it twice.

As the previous examples demonstrated, it’s impossible to have _exactly-once delivery_ in a distributed system. However, it’s still sometimes possible to have _exactly-once processing._

In the end, it’s important for us to understand the difference between these two notions, and clarify what we refer to when we talk about exactly-once semantics.

## Other delivery semantics
As a last note, it’s easy to see that we can easily implement **at-most-once** delivery semantics and **at-least-once** delivery semantics.

We can achieve the _at-most-once_ delivery when we send every message only one time, no matter what happens. Meanwhile, we can achieve the _at-least-once_ delivery when we send a message continuously until we get an acknowledgment from the recipient.