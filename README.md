🤖 GitHub Issue Summarizer AI Agent
This AI-powered agent fetches open issues from any public GitHub repository and summarizes each issue using a locally-run NLP model (facebook/bart-large-cnn) from Hugging Face. It provides concise summaries directly in your terminal and saves them as a Markdown report. Video Demo: https://youtu.be/7B2lQXm6a6g?si=WFt5YmS_yyZL2vr7

🚀 Quick Start
**1. Install Dependencies**
pip install -r requirements.txt
**2. (Optional) Create .env for GitHub Token**
GITHUB_TOKEN=your_github_token_here
If you don’t include a GitHub token, unauthenticated API calls are limited to 60/hour.
**3. Run the Script**
python main.py owner/repo
Example:

python main.py openai/openai-python
**📦 Output**
Summaries printed to the terminal
Markdown file saved as owner_repo_summaries.md (e.g., openai_openai-python_summaries.md)
🧠 Design Choices
Why GitHub + Summarization?

GitHub issues often contain long technical discussions. Summarizing them helps developers quickly triage and prioritize work — especially useful for maintainers or contributors reviewing many issues.

Why Hugging Face Instead of OpenAI?

We use a local summarization model from Hugging Face (facebook/bart-large-cnn) which is:

Free to use

Runs offline after the initial download

Widely accepted for summarization tasks

Why facebook/bart-large-cnn?

Pre-trained on CNN/DailyMail summarization dataset

Balanced trade-off between quality and speed

Works well for semi-formal technical text

Why Markdown Output?

Easy to share and render in GitHub

Easy to copy into documentation

Supports automation workflows

🧰 Tech Stack
| Component  | Tool/Library            |
| ---------- | ----------------------- |
| Language   | Python 3                |
| GitHub API | requests                |
| NLP Model  | facebook/bart-large-cnn |
| ML Runtime | transformers, torch     |
| Env Config | python-dotenv           |
🧪 Example Output (Terminal)
Issue 1: Unexpected behavior in API response
Link: https://github.com/example/repo/issues/123
Summary: The issue describes a mismatch between the documented behavior and the actual API output.
💡 What I’d Improve with More Time

Web UI (Flask / Streamlit)

Interactive CLI with filters

Batch scheduling

Keyword tagging

GitHub comment posting

Multiple model support (T5, Pegasus, Mistral)
✅ Status
Feature	Done
GitHub issue fetching	✅
Local summarization	✅
Markdown export	✅
CLI repo input	✅
OpenAI-free runtime	✅
📜 License

MIT License — free to use with attribution.
