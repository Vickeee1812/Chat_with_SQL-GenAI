from urllib import response
import psycopg2
import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits import create_sql_agent
from langchain_classic.sql_database import SQLDatabase
from langchain_classic.agents import AgentType
from langchain_classic.callbacks import StreamlitCallbackHandler
from langchain_classic.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3

from langchain_ollama import ChatOllama
from langchain_community.embeddings.ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = ChatOllama(model="llama3.1:8b")

st.set_page_config(page_title="LangChain Ollama Demo", page_icon=":parrot:")
st.title("LangChain SQL Agent with Ollama LLM and Embeddings")


LOCALDB = "USE_LOCALDB"
POSTGRES = "USE_POSTGRES"

radio_opt = ["USe SQLLITE 3 DATABASE - Student.db","Connect to your SQL Database"]
selected_opt = st.sidebar.radio(label="Choose the DB which you want to chat",options=radio_opt)
if radio_opt.index(selected_opt)==1:
    db_uri = POSTGRES
    postgres_host = st.sidebar.text_input("Hey provide SQL Host")
    postgres_user = st.sidebar.text_input("My POSTGRES User")
    postgres_password = st.sidebar.text_input("POSTGRES password",type="password")
    postgres_db = st.sidebar.text_input("POSTGRES database")
else:
    db_uri = LOCALDB

if not db_uri:
    st.info("Please add the groq api")

@st.cache_resource(ttl="10m")
def configure_db(db_uri,postgres_host=None,postgres_user=None,postgres_password=None, postgres_db=None):
    if db_uri == LOCALDB:
        db_filePath = (Path(__file__).parent/"student1.db").absolute()
        print(f" file path is {db_filePath}")
        creator = lambda : sqlite3.connect(f"file:{db_filePath}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///",creator=creator))
    elif db_uri == POSTGRES:
        if not (postgres_host and postgres_password and postgres_user and postgres_db):
            st.error("Provide all the details")
            st.stop()
        connection_string = (f"postgresql+psycopg2://{postgres_user}:{postgres_password}"
        f"@{postgres_host}/{postgres_db}"
        )
        print(f" connection string is {connection_string}")
        return SQLDatabase(create_engine(connection_string))

if db_uri == POSTGRES:
    db = configure_db(db_uri, postgres_host, postgres_user, postgres_password, postgres_db)
else:
    db = configure_db(db_uri)


#toolkit
toolkit = SQLDatabaseToolkit(db=db,llm=llm)
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type= AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    agent_executor_kwargs={"handle_parsing_errors": True},
)

if "message" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["message"]=[{"role":"assistant","content":"How can I help you?"}]

for msg in st.session_state.message:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.message.append({"role":"user","content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.message.append({"role":"assistant","content":response})