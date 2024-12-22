---
Связи: 
tags:
  - SysDes
links:
---
Распределенная система - система из множества компонентов, связанных с помощью [[Network]]

- [[#Компоненты|Компоненты]]
- [[#Benefits|Benefits]]
	- [[#Benefits#Performance|Performance]]
	- [[#Benefits#Scalability|Scalability]]
	- [[#Benefits#Availability|Availability]]
- [[#Fallacies/Заблуждения|Fallacies/Заблуждения]]
	- [[#Fallacies/Заблуждения#The network is reliable|The network is reliable]]
	- [[#Fallacies/Заблуждения#Latency is zero|Latency is zero]]
	- [[#Fallacies/Заблуждения#Bandwidth is infinity (Пропускная способность неограничена)|Bandwidth is infinity (Пропускная способность неограничена)]]
	- [[#Fallacies/Заблуждения#The network is secure|The network is secure]]
	- [[#Fallacies/Заблуждения#Topology doesn’t change|Topology doesn’t change]]
	- [[#Fallacies/Заблуждения#Transport cost is zero|Transport cost is zero]]
- [[#The global clock fallacy|The global clock fallacy]]
- [[#Why distributed systems are hard to design|Why distributed systems are hard to design]]
	- [[#Why distributed systems are hard to design#Network asynchrony|Network asynchrony]]
	- [[#Why distributed systems are hard to design#Partial failures|Partial failures]]
	- [[#Why distributed systems are hard to design#Concurency|Concurency]]
- [[#Measures of Correctness in Distributed Systems|Measures of Correctness in Distributed Systems]]
- [[#General properties of Distributed Systems|General properties of Distributed Systems]]
	- [[#General properties of Distributed Systems#Properties each system follows|Properties each system follows]]
	- [[#General properties of Distributed Systems#Categories of distributed systems|Categories of distributed systems]]
- [[#Types of failure|Types of failure]]




## Компоненты
- Ноды - ПК/сервера
- [[Network]] для их связи


## Benefits
![[Pasted image 20230918122803.png]]
### Performance
Мы можем разгонять мощность распределенной системы до очень высоких значений
- С одним компьютером, даже супер компьютером, мы не можем растить мощности линейно
- С кучей независимых и (в меру) дешевых нод, выполняющих работу одновременно - изи
### Scalability
Возможность системы, сети или процесса обрабатывать возрастающее нагрузку, или потенциал быть быстро модифированной для такой цели
- Как и с прошлым пунктом, маштабирование мощной машины для работы с возрастарющим количеством нагрузки бесконечно невозможно (или бесконечно дорого), с системой более реально
### Availability
Возможность системы быть доступной большую часть времени, когда она необходима.
- Современный мир требует доступности 24/7, если мы говорим, что сервис доступен "файв найн", т.е. 99.999% времени, мы подрузумеваем, что даун-тайм не больше 5 минут в год. 
- Маштабировать один компьютер до такого состояния примерно невозможно
- **Redundancy** is one of the widely used mechanisms to achieve higher availability. It refers to storing data into multiple, redundant computers.


## Fallacies/Заблуждения
https://www.educative.io/courses/distributed-systems-practitioners/fallacies-of-distributed-computing
Обсудим заблуждения разрабов, касательно Distributed Systems
![[Pasted image 20230918123539.png]]

###  The network is reliable
- Часто разрабы предполагают это. Конечно, это не так.


### Latency is zero
- Задержка вызовов между либами (или даже между сервсисами при отладке) может быть около нулевой. Но в распределенной системе, где между пользователем и инфраструктурой могут быть штаты, страны и даже континенты задержка определенно не нулевая.


### Bandwidth is infinity (Пропускная способность неограничена)
- Сейчас не столь актуально, но все-же. Сейчас, с мощными дата-центрами, ограничения по трафику намного выше, но это не значит, что мы сможем пропустить весь интернет через нашу систему

### The network is secure
- Сеть, используемая двумя узлами для связи, не всегда под их контролем, и это небезопасно. Вернемся позже

### Topology doesn’t change
Сеть также состоит из множества различных частей, которыми разные организации могут управлять с помощью разного оборудования. Более того, сбои в некоторых частях этой сети могут потребовать от нас изменения ее топологии, чтобы сохранить ее работоспособность. Это также подчеркивает два других заблуждения: есть один администратор и сеть однородна.


### Transport cost is zero
Передача инфы между 2мя точками требует ресурсов сети и машин -> небесплатна. Это надо учитывать.

## The global clock fallacy
- «Распределенные системы имеют глобальные часы, которые мы можем использовать для определения того, когда происходят события». Это предположение весьма обманчиво, поскольку оно несколько интуитивно понятно и справедливо даже для нераспределенных систем. Например, приложение, работающее на одном компьютере, может использовать локальные часы компьютера, чтобы решать, когда и в каком порядке происходят события. Однако это не так в распределенной системе, где каждый узел системы имеет свои собственные локальные часы, работающие с уникальной частотой.



## Why distributed systems are hard to design
![[Pasted image 20230918130554.png]]

### Network asynchrony
- Распределенные системы асинхронны и нет гарантии доставки события, например максимальное время, которое требуется сообщению чтоб быть доставленным. 
- Оно может быть доставленно не по порядку - или даже не быть доставленным вовсе

### Partial failures
- Бывает кейсы, когда час

![[Pasted image 20230918130729.png]]


### Concurency
Часто распределнные системы выполняют много вычислений/операций одновременно (по большому счету, для этого они и созданы) и их нужно как-то синкать, ибо они могут писать в одни и теже доки и т.п. - и конкурировать
![[Pasted image 20230919180639.png]]


## Measures of Correctness in Distributed Systems
https://www.educative.io/courses/distributed-systems-practitioners/measures-of-correctness-in-distributed-systems#Correctness
Safety
Liveness

## General properties of Distributed Systems
### Properties each system follows
- How the nodes of a distributed system interact with each other
- How the nodes of a distributed system can fail
### Categories of distributed systems
1. Synchronous systems
2. Asynchronous systems


## Types of failure
https://www.educative.io/courses/distributed-systems-practitioners/types-of-failures
- Fail-stop - Остановка - нода остановилась и остается остановленной. Остальные ноды могут это видеть
- Crash - Авария - нода упала, но молча и другие ноды не могут напрямую видеть ее статус
- Omission - Упущения - нода не отвечает на реквесты
- Byzantine - Византинский - Узел демонстрирует произвольное поведение: он может передавать произвольные сообщения в произвольное время, предпринимать неверные шаги или останавливаться. Византийские сбои возникают, когда узел не ведет себя в соответствии со своим конкретным протоколом или алгоритмом. Обычно это происходит, когда злоумышленник или программная ошибка подвергают риску узел. 

 Чтобы справиться с этими неудачами, нам нужны комплексные решения. Однако большинство компаний развертывают распределенные системы в средах, которые они считают конфиденциальными и безопасными. Сбои, связанные с отказом, являются самыми простыми и удобными с точки зрения человека, создающего распределенные системы. Однако они не очень реалистичны. Это связано с тем, что в реальных системах существует множество случаев, когда нам нелегко определить, произошел сбой другого узла или нет.

![[Pasted image 20230919181457.png]]