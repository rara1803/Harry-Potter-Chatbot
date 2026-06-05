# Harry-Potter-Chatbot
HarryBot is a retrieval-based chatbot that answers Harry Potter questions using FAISS vector search, conversational memory, similarity thresholding, and a Streamlit interface.

# HarryBot

HarryBot is a retrieval-based Harry Potter chatbot that answers questions using a curated Harry Potter knowledge base.

## Features

* Answers only questions related to the provided dataset
* Rejects questions outside the dataset
* Supports conversational memory for follow-up questions
* Uses FAISS vector search for efficient retrieval
* Includes similarity threshold filtering
* Handles greeting messages and self-related questions
* Designed to resist prompt injection and jailbreak attempts
* Streamlit-based user interface

## Technologies Used

* Python
* Streamlit
* FAISS
* OpenAI API
* Sentence Transformers

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
* `requirements.txt` – Dependencies
* `data/` – Harry Potter dataset
  
## Author

Rama Tamimi
