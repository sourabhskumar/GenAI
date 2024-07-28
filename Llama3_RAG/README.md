# Conversational RAG with PDF Uploads

This project is a Streamlit application that allows users to upload PDFs and interact with their content through a conversational interface. The application uses a Retrieval-Augmented Generation (RAG) system to answer questions based on the content of the uploaded PDFs.

## Features
- Upload multiple PDF files
- Extract and process text from PDFs
- Create embeddings for the text content
- Set up a history-aware retriever
- Chat interface to interact with the content
- Maintains chat history across sessions

## Installation

1. Clone the repository:
    ```bash
    git clone 
    cd
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scriptsctivate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add the following:
    ```plaintext
    HF_TOKEN=your_hugging_face_token
    ```

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
