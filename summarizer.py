from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_issue(title: str, body: str) -> str:
    text = f"{title}\n\n{body}"

    if not text or len(text.strip()) == 0:
        return "No content to summarize."

    result = summarizer_pipeline(
        text,
        max_length=130,
        min_length=30,
        do_sample=False
    )

    return result[0]["summary_text"]
