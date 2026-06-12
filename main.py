import os

from dotenv import load_dotenv
from pydantic import BaseModel, SecretStr
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatOpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
    model=os.getenv("OPENAI_MODEL", "gpt-5.1"),
    api_key=SecretStr(os.getenv("OPENAI_API_KEY", "")),
    timeout=None,
    http_client=create_httpx_client(),
)

agent = create_agent(
    model=llm,
    tools=[search_tool, wiki_tool, save_tool],
    system_prompt="""
        You are a research assistant that will help generate a research paper.
        Answer the user query and use necessary tools.
        Always save your final research summary using the save_tool before responding.
    """,
    response_format=ResearchResponse,
)

query = input("What can I help you research? ")

raw_response = agent.invoke({"messages": [{"role": "user", "content": query}]})

structured_response: ResearchResponse = raw_response["structured_response"]
print(structured_response.topic)
print(structured_response.summary)
print(structured_response.sources)
print(structured_response.tools_used)
