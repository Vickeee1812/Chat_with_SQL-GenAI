# Chat with SQL - GenAI

A Streamlit-based application that enables natural language queries on SQL databases using LangChain and local Ollama LLM.

## 📋 Overview

This project allows you to interact with SQL databases (SQLite or PostgreSQL) using natural language conversations. Instead of writing SQL queries manually, you can ask questions in plain English and the AI agent will:
- Understand your intent
- Generate appropriate SQL queries
- Execute them against your database
- Return results in a conversational format

## 🎯 Features

- **Natural Language Interface**: Chat with your database using plain English
- **Dual Database Support**: 
  - SQLite (local database - `student1.db`)
  - PostgreSQL (remote database with custom credentials)
- **Local LLM**: Uses Ollama with Llama 3.1 (8B) model for privacy-focused processing
- **Interactive UI**: Built with Streamlit for an intuitive chat experience
- **Message History**: Maintains conversation history within a session
- **SQL Agent**: Leverages LangChain's SQL Database Toolkit and Agent framework
- **Error Handling**: Robust parsing error handling for complex queries

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Ollama installed with `llama3.1:8b` model
- Ollama Embeddings model: `nomic-embed-text`

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up the local database** (if using SQLite):
```bash
python sqllite.py
```
This will create and populate a `student1.db` database with sample student data.

4. **Ensure Ollama is running**:
```bash
ollama serve
```

### Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📚 Usage

### Using Local SQLite Database

1. Select **"USe SQLLITE 3 DATABASE - Student.db"** from the sidebar
2. Type your question in the chat input, for example:
   - "Show me all students"
   - "What is the average age of students?"
   - "Find students in section A1"
3. The AI agent will generate and execute the appropriate SQL query

### Using PostgreSQL Database

1. Select **"Connect to your SQL Database"** from the sidebar
2. Enter your PostgreSQL credentials:
   - **SQL Host**: Database server hostname
   - **POSTGRES User**: Username
   - **POSTGRES password**: Password
   - **POSTGRES database**: Database name
3. Ask your questions - the agent will interact with your PostgreSQL database

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── sqllite.py          # SQLite database initialization and population
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## 🗄️ Database Schema

### SQLite Database (student1.db)

**Table: Student1**
| Column | Type | Description |
|--------|------|-------------|
| name | TEXT | Student name |
| age | INTEGER | Student age |
| grade | TEXT | Grade/Academic level |
| section | TEXT | Class section |

## 🔧 Technical Stack

- **LangChain**: LLM orchestration and SQL Agent framework
- **Ollama**: Local LLM runtime (Llama 3.1:8b)
- **Streamlit**: Web UI framework
- **SQLAlchemy**: SQL database abstraction
- **SQLite3**: Local database support
- **psycopg2**: PostgreSQL adapter
- **LangChain Community**: Extended toolkits and integrations

## ⚙️ Configuration

### Environment Variables

Currently, the application uses hardcoded models:
- **LLM Model**: `llama3.1:8b`
- **Embeddings Model**: `nomic-embed-text`

These can be modified in `app.py`:
```python
embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = ChatOllama(model="llama3.1:8b")
```

### Caching

Database connections are cached for 10 minutes to improve performance:
```python
@st.cache_resource(ttl="10m")
```

## 🛠️ Troubleshooting

### Ollama Connection Issues
- Ensure Ollama is running: `ollama serve`
- Verify models are installed: `ollama list`
- Check if models can be pulled: `ollama pull llama3.1:8b` and `ollama pull nomic-embed-text`

### Database Connection Issues
- **SQLite**: Ensure `student1.db` exists in the project directory
- **PostgreSQL**: Verify credentials and network connectivity

### Import Errors
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`
- Check Python version compatibility

## 📝 Notes

- The SQLite database opens in read-only mode (`mode=ro`)
- Message history is stored in Streamlit's session state
- Clear message history using the "Clear message history" button in the sidebar

## 🔐 Security Considerations

- PostgreSQL passwords are handled as input in the UI (consider using environment variables for production)
- Ollama models run locally, keeping data private
- SQLite database is read-only to prevent accidental modifications

## 📦 Dependencies

See `requirements.txt` for the complete list of dependencies. Key packages include:
- langchain & langchain-community
- langchain_ollama
- streamlit
- sqlalchemy
- psycopg2
- pypdf
- bs4

## 🚀 Future Enhancements

Potential improvements:
- Support for additional database types (MySQL, MongoDB, etc.)
- Enhanced error messages and debugging
- Query result visualization and charts
- Export query results to CSV/PDF
- User authentication and multi-user support
- Query caching and optimization

## 📄 License

[Add your license information here]

## 👨‍💻 Author

[Add author information here]

---

For more information on LangChain: https://python.langchain.com/
For more information on Ollama: https://ollama.ai/
For more information on Streamlit: https://streamlit.io/
