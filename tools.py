import os
import wikipedia
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime


OUTPUT_DIR = "outputs"

@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """Saves the research summary to a text file inside the outputs folder.

    Args:
        data: The full research content to save.
        filename: The output file name (default: research_output.txt).
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filepath}"

search_tool = DuckDuckGoSearchRun()

wikipedia.set_user_agent("ai-agent-tutorial/1.0 (research assistant)")
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
