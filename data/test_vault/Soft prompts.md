---
tags:
  - "#NLP"
  - "#LLM"
links:
---
Идея: давайте улучшать [[Prompt|промпт]] не докидывая слова к нему, [[Prompt Engineering]] и т.п., а обучая векторок-[[Embeddings|ембедов]], которые можно досыпать к прошедшим токенизацию промптам.
Это можно делать градиентными методами. 
Схожая концепция - 


## Startup/project idea
Давай сделаем фреймворк, который станет оберткой над ЛЛМками у компаний, улучшая их запросы промпт-инженерингом

## Materials
**Main paper:**
The Power of Scale for Parameter-Efficient Prompt Tuning, 2021
https://aclanthology.org/2021.emnlp-main.243.pdf

Learning How to Ask: Querying LMs with Mixtures of Soft Prompts, 2021
https://aclanthology.org/2021.naacl-main.410.pdf

**Interesting papers:**
- PERSOMA: PERsonalized SOft ProMpt Adapter Architecture for Personalized Language Prompting https://arxiv.org/pdf/2408.00960
	- Фреймворк-архитектура от Гугла для захвата User-history и подмешивания в LLM, посути о памяти в LLM
- LASP: Text-to-Text Optimization for Language-Aware Soft Prompting of Vision & Language Models https://openaccess.thecvf.com/content/CVPR2023/papers/Bulat_LASP_Text-to-Text_Optimization_for_Language-Aware_Soft_Prompting_of_Vision__CVPR_2023_paper.pdf
	- Фреймворк LASP, как я понимаю из abstarct, чтобы оборачивать LLMки soft-промптами, но детектить и предотвращать оверфит, попутно классифицируя промпты и скрамливая нужный софт?
- Tailor: A Soft-Prompt-Based Approach to Attribute-Based Controlled Text Generation https://aclanthology.org/2023.acl-long.25.pdf
	- Чуваки пытаются софт-промптами направить генерацию в нужное русло, например докидывать эмоций
- Decomposed Soft Prompt Guided Fusion Enhancing for Compositional Zero-Shot Learning https://openaccess.thecvf.com/content/CVPR2023/papers/Lu_Decomposed_Soft_Prompt_Guided_Fusion_Enhancing_for_Compositional_Zero-Shot_Learning_CVPR_2023_paper.pdf
	- Вводят фреймворк для улучшений генераций незнакомой VLM картинки через soft-prompts?
- InfoPrompt: Information-Theoretic Soft Prompt Tuning for Natural Language Understanding https://proceedings.neurips.cc/paper_files/paper/2023/file/c01c0da4fe2ef2df9863f55261e2e924-Paper-Conference.pdf

- Adapting LLMs for Efficient Context Processing through Soft Prompt Compression https://dl.acm.org/doi/pdf/10.1145/3677779.3677794
- A lot of papers from ScienceOs search https://app.scienceos.ai/chat/c/ixDUhGvhnP5Xqy8mPkrCSX


NotebookLM:
https://notebooklm.google.com/notebook/2aeba3a1-408e-48cc-b174-8a752a6a8bd1?pli=1

### ScienceOs
https://app.scienceos.ai/chat/c/ixDUhGvhnP5Xqy8mPkrCSX
Кайфовый граф бай зе вей


![[Pasted image 20241202122348.png]]