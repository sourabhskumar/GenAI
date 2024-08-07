import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API")
# Constants for database selection
LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

# Set page configuration
st.set_page_config(
    page_title="LangchainApp with SQL",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#2e7bcf, #2e7bcf);
            color: white;
        }
        .chat-message {
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            animation: fadeIn 0.5s ease-in-out;
            display: flex;
        }
        .chat-message.user {
            background-color: #DCF8C6;
            justify-content: flex-end;
        }
        .chat-message.assistant {
            background-color: #F1F0F0;
            justify-content: flex-start;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .main-header {
            text-align: center;
            padding: 20px;
            font-size: 2.5rem;
            color: #2e7bcf;
        }
        .container {
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        .message-container {
            flex: 1;
            overflow-y: auto;
        }
        .input-container {
            padding: 10px;
            background-color: #f9f9f9;
            border-top: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<div class="main-header">Langchain: Conversation with SQL</div>', unsafe_allow_html=True)

# Sidebar options
st.sidebar.header("Database Configuration")
radio_opt = ["Use SQLite 3 Database", "Connect to your SQL Database"]
selected_opt = st.sidebar.radio(label="Select the Database", options=radio_opt)

if selected_opt == "Use SQLite 3 Database":
    db_url = "USE_LOCALDB"
else:
    db_url = "USE_MYSQL"
    mysql_host = st.sidebar.text_input("Enter the host name", key="mysql_host")
    mysql_user = st.sidebar.text_input("Enter the username", key="mysql_user")
    mysql_password = st.sidebar.text_input("Enter the password", type="password", key="mysql_password")
    mysql_db = st.sidebar.text_input("Enter the database name", key="mysql_db")

# Error handling for missing API key
if not groq_api_key:
    st.sidebar.error("Groq API Key not found. Please check your .env file.")

# LLM Configuration
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", streaming=True)

@st.cache_resource(ttl="2h")
def configure_database(db_url, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_url == "USE_LOCALDB":
        dbfilepath = Path(__file__).parent / "student.db"
        return SQLDatabase(create_engine(f"sqlite:///{dbfilepath}", creator=lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)))
    elif db_url == "USE_MYSQL":
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.sidebar.error("Please enter all MySQL details")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

# Database Configuration
if db_url == "USE_MYSQL":
    db = configure_database(db_url, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_database(db_url)

# Toolkit and agent setup
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True
)

# Initialize session state for chat
if "messages" not in st.session_state or st.sidebar.button("Clear Chat"):
    st.session_state['messages'] = [{"role": "assistant", "content": "Hello! I am Langchain Assistant. How can I help you?"}]

# Main container
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="message-container">', unsafe_allow_html=True)

# Display chat messages with animation
for msg in st.session_state.messages:
    role_class = "user" if msg['role'] == "user" else "assistant"
    st.markdown(f'<div class="chat-message {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="input-container">', unsafe_allow_html=True)

# User query input
user_query = st.text_input("Your message:", placeholder="Ask me anything...")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Process user query
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.markdown(f'<div class="chat-message user">{user_query}</div>', unsafe_allow_html=True)

    with st.spinner("Processing..."):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f'<div class="chat-message assistant">{response}</div>', unsafe_allow_html=True)