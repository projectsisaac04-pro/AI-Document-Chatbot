# AI Document Assistant 📚

### RAG-Based PDF Question Answering System

An AI-powered document assistant that allows users to upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG).

The application uses semantic search to retrieve relevant information from documents and Anthropic Claude to generate context-aware answers.

## 🚀 Features

- **PDF Upload:** Upload PDF documents through a Streamlit interface.
- **Text Extraction:** Extract text from PDF documents using PyPDF.
- **Text Chunking:** Divide extracted text into smaller chunks using LangChain.
- **Embedding Generation:** Generate vector embeddings using Hugging Face Sentence Transformers.
- **Vector Database:** Store and retrieve document embeddings using ChromaDB.
- **Semantic Search:** Retrieve relevant document chunks based on the meaning of user queries.
- **AI-Powered Answers:** Use Anthropic Claude to generate answers from retrieved document context.
- **Context Grounding:** Instruct the LLM to answer using document content rather than external knowledge.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend interface |
| PyPDF | PDF text extraction |
| LangChain | LLM and RAG integration |
| Hugging Face | Text embedding generation |
| Sentence Transformers | Semantic embeddings |
| ChromaDB | Vector database |
| Anthropic Claude | AI answer generation |
| Python-dotenv | Environment variable management |

## 🏗️ RAG Architecture

The application follows a Retrieval-Augmented Generation architecture.

```text
             PDF Upload
                  |
                  v
           PDF Text Extraction
                  |
                  v
              Chunking
                  |
                  v
          Embedding Generation
                  |
                  v
             ChromaDB
           Vector Storage
                  |
                  |
User Query -------+
     |
     v
Query Embedding
     |
     v
Semantic Retrieval
     |
     v
Relevant Document Chunks
     |
     v
     Claude API
     |
     v
Context-Based Answer
     |
     v
  Streamlit UI
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

```bash
cd AI-DOCUMENT-ASSISTANT
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit pypdf langchain langchain-chroma langchain-huggingface langchain-anthropic sentence-transformers chromadb python-dotenv
```

### 4. Configure API Key

Create a `.env` file in your project directory.

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Replace `your_anthropic_api_key` with your actual Anthropic API key.

**Security:** Never upload your `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
chroma_db/
```

### 5. Run the application

```bash
streamlit run main.py
```

Open the local URL displayed in your terminal.

## 📖 How It Works

**Step 1: Document Upload**

Users upload PDF documents through the Streamlit interface.

**Step 2: Text Extraction**

PyPDF extracts textual content from the uploaded documents.

**Step 3: Text Chunking**

LangChain's CharacterTextSplitter divides the extracted text into smaller chunks.

**Step 4: Embedding Generation**

Hugging Face Sentence Transformers converts the text chunks into numerical vector representations.

**Step 5: Vector Storage**

ChromaDB stores the document chunks and their corresponding embeddings.

**Step 6: Semantic Retrieval**

When a user asks a question, ChromaDB retrieves the most relevant document chunks using vector similarity.

**Step 7: Answer Generation**

The retrieved chunks and user query are passed to Anthropic Claude through LangChain.

**Step 8: Response Display**

Claude generates a context-based response, which is displayed in the Streamlit interface.

## 🔮 Future Improvements

- Support multiple PDF uploads.
- Implement conversational memory and chat history.
- Add document page citations.
- Implement claim verification to improve answer grounding.
- Improve retrieval accuracy using reranking.
- Add support for different document formats.
- Improve the user interface.
- Deploy the application online.

## 🎯 Project Objective

The objective of this project is to build an AI-powered document assistant that makes information retrieval from large PDF documents easier through semantic search and context-aware question answering.

## 👨‍💻 Author

Developed as a personal AI/ML project to explore Retrieval-Augmented Generation, Large Language Models, vector databases and semantic search.
