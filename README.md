# MindMiner
Your Companion across your knowledge-base

MindMiner is an advanced RAG (Retrieval-Augmented Generation) system designed to transform how people engage with and explore their Obsidian notes. The assistant enables efficient retrieval, synthesis, and summarization of critical information, making it easier to generate insights and maintain a comprehensive understanding of complex research topics. Think of each note as a graph node, and the entire vault of notes as a rich, interconnected graph that MindMiner helps you navigate seamlessly.
It's provides as Obsidian extencion, you also can donwload additional fronted for it, like tg-bot

## Structure
- app
    - api
    - core
- build
    - backend
    - frontend
    - init
- data
- research



## Project Goals
- Automate the search for relevant information within your Obsidian notes
- Integrate and analyze data to construct a cohesive knowledge base
- Summarize key points to accelerate comprehension of core ideas
- Provide an intuitive interface for managing and visualizing research content
- Enhance productivity and efficiency for researchers using Obsidian

## Key Features
### Information Retrieval and Citation Extraction
- Search for relevant notes using keywords or concepts
- Extract key info and references from your knowledge vault
- Chat with your knowledge

### Data Integration and Analysis
- Dive deeper into linked notes and references
- Combine information from multiple sources for comprehensive analysis

### Summarization and Rewriting
- Generate concise and insightful summaries using state-of-the-art summarization techniques
- Rewrite and optimize queries to discover related research and ideas


## 🛠 Technology Stack
- **Language**: Python
- **Frameworks**: FastAPI, Aiogram, LangChain, FlagEmbedding
- **Vector DB**: Qdrant
- **Frontend**: Streamlit and Tg-Bot

## Getting Started

#### Running RAG

1. Clone the repository
    ```bash
    git clone https://github.com/AlekseiSDev/MindMiner.git
    cd MindMiner
    ```
2. Create the .env and config.json files and fill them out based on the provided examples ([app/.env.example](app/.env.example) and [config_example.json](config_example.json)).

3. Install the required dependencies:

    Using pip:
    ```bash
    pip install -r requirements.txt
    ```
    Or using poetry:
    ```bash
    poetry install
    ```

4. Build and start the Docker containers:
    ```
    docker compose up --build -d
    ```

5. Visit the application at http://localhost:80.

#### Running Tg-Bot

1.  Create the .env file and fill it out based on the provided [bot/.env.example](bot/.env.example).

2. Run it:
    ```bash
    cd bot
    ```

    ```python
    python main.py
    ```


## Contacts
[Aleksey Stepin](https://github.com/AlekseiSDev)      
[Nikita Safonov](https://github.com/sixxio)       
[Rustam Akimov](https://github.com/AkiRusProd)