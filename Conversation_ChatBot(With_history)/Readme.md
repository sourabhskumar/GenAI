# Chat Notebook Explanation

This repository contains the detailed explanation and implementation of a chat notebook that demonstrates the usage of LangChain with various models and components.

## Files

- `chat.ipynb`: The original Jupyter Notebook with the implementation.
- `chat_notebook_explanation.txt`: A detailed text explanation of each cell in the notebook.
- `main.py`: The main script to run the notebook as a Python script.
- `.env`: Environment file to store API keys and tokens.
- `requirements.txt`: A file listing all required packages.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chat-notebook-explanation.git
    cd chat-notebook-explanation
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API keys:
    ```text
    GROQ_API_KEY=your_groq_api_key
    HF_TOKEN=your_huggingface_token
    ```

5. Run the main script:
    ```bash
    python main.py
    ```

## Usage

The main script `main.py` will load environment variables, set up models and embeddings, and run the example queries as shown in the notebook.

## License

This project is licensed under the MIT License.
