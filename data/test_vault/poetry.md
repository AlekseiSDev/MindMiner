---
tags:
  - Python
  - Dev
links:
---
Либа для управления [[Dependencies (зависимости)]] на [[Python]]

# Project Setup and Logging Overview

## Installation

To set up the project, you need to use [Poetry](https://python-poetry.org/), a dependency management and packaging tool. Below are the steps to install Poetry and run the project.

### Poetry Installation

For **macOS** and **Ubuntu**, follow these steps:

1. Install Poetry by running the following command in your terminal:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. Add Poetry to your path:
   ```
   export PATH="$HOME/.local/bin:$PATH"
   ```

### Running the Project

1. Clone the repository and navigate to the project folder.
2. Create a `.env` file in the root directory. Add the following environment variables:
   ```
   OPENAI_API_KEY=<your_openai_api_key>
   OPENAI_BASE_URL=<your_openai_base_url>
   ```
3. Install dependencies and run the project:
   ```
   poetry install
   poetry run python main.py
   ```

