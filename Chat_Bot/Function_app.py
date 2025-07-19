from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers.string import StrOutputParser
from langchain_together import ChatTogether

from dotenv import load_dotenv
load_dotenv()

def get_response(
        user_query,
        chat_history
):
    api_key = '326c17f84f17a4e7fb6400ae619a86d15c1e9be3d6ee0309b49a6553cf5c47d0'
    llm = ChatTogether(
        model="meta-llama/Llama-3-70b-chat-hf",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key = api_key
    )

    template = """
    You are a helpful assistant. Answer the following questions considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()

    return chain.stream(
        {"chat_history":chat_history,
         "user_question":user_query}
    )