# AI Agent LangChain Demo

A demonstration of an AI research assistant powered by LangChain that autonomously researches topics using multiple tools including web search, Wikipedia, and document storage.

## 📋 Overview

This project showcases how to build an intelligent agent using LangChain that:
- **Answers research queries** using natural language
- **Performs web searches** via DuckDuckGo
- **Queries Wikipedia** for additional information
- **Generates structured responses** with summaries, sources, and tool usage tracking
- **Saves research outputs** to files for later reference

The agent operates with a defined system prompt that guides it to use available tools appropriately and structure its responses in a consistent format.

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **OpenAI API Key** (or compatible API endpoint)
- **pip** (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-agent-lang-chain-demo
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Linux/macOS:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requeriments.txt
   ```

### Configuration

1. **Create a `.env` file** in the project root:
   ```bash
   touch .env
   ```

2. **Add your API credentials to `.env`:**
   ```env
   OPENAI_API_KEY=your-api-key-here
   OPENAI_MODEL=gpt-4
   OPENAI_BASE_URL=https://api.openai.com/v1
   ```

   - Replace `your-api-key-here` with your actual OpenAI API key
   - `OPENAI_MODEL`: The model to use (default: gpt-5.1). Examples: `gpt-4`, `gpt-3.5-turbo`
   - `OPENAI_BASE_URL`: API endpoint (default: OpenAI). Can be customized for local models or other providers

### Running the Project

Simply execute the main script:
```bash
python main.py
```

When prompted, enter your research query:
```
What can I help you research? Your research topic here
```

The agent will:
1. Process your query
2. Use available tools (search, Wikipedia) as needed
3. Generate a structured research response
4. Save the output to the `outputs/` folder
5. Display the results in your terminal

## 📁 Project Structure

```
.
├── main.py              # Main agent entry point
├── tools.py             # Tool definitions (search, Wikipedia, save)
├── requeriments.txt     # Python dependencies
├── README.md            # This file
├── .env                 # Environment variables (create this)
└── outputs/             # Research output files (created automatically)
```

## 🛠️ Available Tools

The agent has access to three tools:

| Tool | Purpose |
|------|---------|
| **search_tool** | Web search using DuckDuckGo |
| **wiki_tool** | Wikipedia queries for reference material |
| **save_tool** | Saves research summaries to the outputs folder |

## 📤 Output Format

The agent returns a structured response containing:

```python
{
    "topic": str,           # The research topic
    "summary": str,         # The research summary
    "sources": list[str],   # List of sources used
    "tools_used": list[str] # Tools utilized for research
}
```

Output files are saved to `outputs/research_output.txt` with timestamps.

## 🔧 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | (required) | Your OpenAI API key |
| `OPENAI_MODEL` | `gpt-5.1` | Model to use |
| `OPENAI_BASE_URL` | `https://api.openai.com/v1` | API endpoint |

## 💡 Example Usage

```bash
$ python main.py
What can I help you research? Machine learning in healthcare

Topic: Machine Learning in Healthcare
Summary: Machine learning is revolutionizing healthcare through...
Sources: ['source1.com', 'source2.com', ...]
Tools Used: ['search_tool', 'wiki_tool', 'save_tool']
```

## 📦 Dependencies

- **langchain**: LLM framework
- **langchain-community**: Community tools and integrations
- **langchain-openai**: OpenAI integration
- **langgraph**: Graph-based agent orchestration
- **pydantic**: Data validation
- **python-dotenv**: Environment variable management
- **wikipedia**: Wikipedia access
- **ddgs**: DuckDuckGo search

## ⚠️ Troubleshooting

**Issue: "OPENAI_API_KEY not found"**
- Ensure you've created a `.env` file in the project root
- Verify the API key is correctly set in `.env`

**Issue: "Module not found"**
- Activate your virtual environment
- Reinstall dependencies: `pip install -r requeriments.txt`

**Issue: Connection timeout**
- Check your internet connection
- Verify the `OPENAI_BASE_URL` is accessible

## 📝 Notes

- Research outputs are appended to `research_output.txt` with timestamps
- Multiple queries create separate entries in the same output file
- The agent uses streaming for real-time response generation
