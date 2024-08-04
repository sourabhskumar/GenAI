import streamlit as st
from langchain_groq import ChatGroq 
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun 
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import ChatPromptTemplate
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Set up the page configuration
st.set_page_config(
    page_title="LangchainApp with Search",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS to style the app
st.markdown(
    """
    <style>
    .main {
        background-color: #FFFFFF;
        color: #ADD8E6; /* Light blue text color */
    }
    .stSidebar {
        background-color: #404040;
        color: #ADD8E6; /* Light blue text color */
    }
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #404040;
        color: #ADD8E6; /* Light blue text color */
    }
    .stTextInput > div > div > input::placeholder {
        color: #FFFFFF; /* White placeholder text */
    }
    .stTabs > div {
        background-color: #FFFFFF;
    }
    .stChatMessage {
        background-color: #444444;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stChatMessage.user {
        background-color: #4CAF50;
        color: #FFFFFF; /* White text color */
    }
    .stChatMessage.assistant {
        background-color: #1E90FF;
        color: #FFFFFF; /* White text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API")

api_wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=api_wiki_wrapper)
api_arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=api_arxiv_wrapper)
search = DuckDuckGoSearchRun(name="Search")

st.title("LangchainApp with Search")

# Sidebar settings
st.sidebar.header("Settings")
st.sidebar.write("Configured using environment variables")

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["Chat", "Conversation History", "Settings"])

with tab1:
    st.header("Chat with the Assistant")

    if "messages" not in st.session_state:
        st.session_state['messages'] = [
            {
                "role": "system",
                "content": "I am an assistant who can search Wikipedia, arXiv, and the web. How can I help you?"
            }
        ]

    input_col, output_col = st.columns(2)

    with input_col:
        st.subheader("User Input")
        for msg in st.session_state.messages:
            if msg['role'] == "user":
                st.markdown(
                    f"""
                    <div class="stChatMessage user">
                        {msg['content']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        prompt = st.text_input("Ask a question:", placeholder="What is machine learning?")
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.markdown(
                f"""
                <div class="stChatMessage user">
                    {prompt}
                </div>
                """,
                unsafe_allow_html=True,
            )

            llm = ChatGroq(model="Llama3-8b-8192", groq_api_key=GROQ_API_KEY, streaming=True)
            tools = [wiki, arxiv, search]
            search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

            with output_col:
                st.subheader("Assistant Response")
                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.markdown(
                    f"""
                    <div class="stChatMessage assistant">
                        {response}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

with tab2:
    st.header("Conversation History")
    history_container = st.container()
    with history_container:
        for msg in st.session_state.messages:
            if msg['role'] == "assistant":
                st.markdown(
                    f"""
                    <div class="stChatMessage assistant">
                        {msg['content']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

with tab3:
    st.header("Settings")
    st.write("This app uses a predefined Groq API key from the .env file.")
    st.write("You can update your .env file to change the API key or other settings.")
