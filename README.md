# Langchain RAG Implementation

This repository contains an implementation of a Retrieval-Augmented Generation (RAG) system using Langchain. The system allows users to query documents using natural language and receive relevant summaries based on the document content.

## Project Structure

```
├── data/
│   ├── pdf/               # PDF documents for knowledge base
│   ├── text_files/        # Text documents for knowledge base
│   └── vector_store/      # Storage for vector embeddings
├── notebook/              # Jupyter notebooks for development and testing
├── src/                   # Source code
│   ├── data_loader.py     # Document loading utilities
│   ├── embedding.py       # Text embedding pipeline
│   ├── search.py         # RAG search implementation
│   └── vectorstore.py    # Vector storage management
├── app.py                # Main application entry point
├── requirements.txt      # Project dependencies
└── pyproject.toml       # Project configuration
```

## Features

- Document loading support for both PDF and text files
- FAISS vector store for efficient similarity search
- Interactive query interface
- RAG-based document summarization

## Prerequisites

- Python 3.11 or higher
- Required Python packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/badalkr2004/langchain-rag.git
cd langchain-rag
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. **Data Preparation**

   - Place your PDF documents in the `data/pdf/` directory
   - Place your text files in the `data/text_files/` directory

2. **Building the Vector Store**
   Uncomment the following lines in `app.py` to build the vector store from your documents:

   ```python
   docs = load_all_documents("data")
   store = FaissVectorStore()
   store.build_from_documents(docs)
   ```

3. **Running the Application**

   ```bash
   python app.py
   ```

   This will start an interactive session where you can:

   - Enter questions about your documents
   - Get AI-generated summaries based on relevant document sections
   - Type 'exit', 'quit', or 'q' to end the session

## Example Queries

You can ask questions like:

- "What is attention in machine learning?"
- "Explain object detection"
- "Describe embeddings in machine learning"

The system will retrieve relevant information from your documents and provide a summarized response.

## Development

- Check out the Jupyter notebooks in the `notebook/` directory for development examples
- Use `pdf_loader.ipynb` for testing PDF document loading
- Use `document.ipynb` for experimenting with document processing
