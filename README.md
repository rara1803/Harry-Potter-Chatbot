# Harry Potter Chatbot ⚡

HarryBot is a retrieval-based chatbot that answers Harry Potter questions using FAISS vector search, conversational memory, similarity thresholding, and a Streamlit interface.

### Home Page
![image_alt](https://github.com/rara1803/Harry-Potter-Chatbot/blob/a4b066f4e1ed374f7c9bb343c28f14eba383a0d8/homepage%20hp%20bot.png)

### Example Conversation
![image_alt]

### Out-of-Scope Question
![image_alt]

## Features

* Answers questions only when the information exists in the provided dataset
* Rejects out-of-scope questions
* Supports conversational memory for follow-up questions
* Uses FAISS vector search for efficient retrieval
* Implements similarity threshold filtering
* Handles greetings and self-related questions
* Designed to resist prompt injection and jailbreak attempts
* Streamlit-based user interface

## Technology Stack

| Component            | Technology                               |
| -------------------- | ---------------------------------------- |
| Programming Language | Python 3.11                              |
| Web Interface        | Streamlit                                |
| Data Handling        | Pandas, OpenPyXL                         |
| Embedding Model      | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Search        | FAISS (IndexFlatIP)                      |
| Language Model       | Qwen-Plus                                |
| API Client           | OpenAI Python SDK                        |
| Numerical Computing  | NumPy                                    |

## System Architecture

1. User submits a question through the Streamlit interface.
2. A FAISS index containing question-answer pairs searches for highly similar questions.
3. If the similarity score exceeds a predefined threshold, the stored answer is returned directly.
4. Otherwise, a second FAISS index retrieves relevant context from the dataset.
5. The retrieved context is provided to the language model to generate an answer.
6. If sufficient information is unavailable, the chatbot responds with:

> I cannot answer that..

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

* `app.py` – Streamlit interface
* `chatbot.py` – Chatbot logic
* `requirements.txt` – Project dependencies
* `harry_potter_data_02.xlsx` – Harry Potter knowledge base

## Authors

* Rama Tamimi
* Joud Wardeh
