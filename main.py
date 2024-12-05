import gradio as gr
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain.tools.retriever import create_retriever_tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage
from langgraph.checkpoint.memory import MemorySaver
import logging
from datetime import datetime
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[logging.FileHandler('chat_history.log')]
)
logger = logging.getLogger(__name__)

embedding_llm = OllamaEmbeddings(model="llama3.2")
db = Chroma(persist_directory='./chroma', embedding_function=embedding_llm,
            collection_name="planetbucks")

retriever_tool = create_retriever_tool(
    db.as_retriever(search_type='mmr'),
    name="planetbucks_search",
    description="""Search for information about PlanetBucks store, including store information, 
    coffee drink menus, specialty coffee beans menu, and bean fact sheet.""",
)

config = {"configurable": {"thread_id": "thread1"}}
llm = ChatOllama(model="llama3.2", temperature=0)
tools = [retriever_tool]

SYSTEM_MESSAGE = """You are a helpful receptionist at PlanetBucks, which is a coffee cafe. Your name is Echo.
You will answer politely but playfully since it's Christmas festival time now."""

chat_history = []
memory = MemorySaver()

langgraph_agent_executor = create_react_agent(
    llm,
    tools,
    state_modifier=SYSTEM_MESSAGE,
    checkpointer=memory
)

def log_messages(response):
    for message in response['messages']:
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'role': message.type,
            'content': message.content,
            'additional_kwargs': message.additional_kwargs
        }
        logger.info(json.dumps(log_entry))

def chat(message, history):
    global chat_history
    response = langgraph_agent_executor.invoke(
        {"messages": [("human", message)]},
        config
    )
    chat_history = response
    log_messages(response)
    return response['messages'][-1].content

demo = gr.ChatInterface(fn=chat, title="Echo, the PlanetBucks Receptionist",
                        description="Welcome to PlanetBucks, a virtual cafe filled with AI enthiusiasts!",
                        examples=["What is the menu for today?", "What is the specialty coffee bean?", "What is the store information?"])

if __name__ == "__main__":
    demo.launch(share=False)