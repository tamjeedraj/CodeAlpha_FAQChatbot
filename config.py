import os

from dotenv import load_dotenv


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add it to your .env file."
    )


EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# You can change the model if your Gemini account/API
# provides another suitable current model.
GEMINI_MODEL = "gemini-3.8-flash"

TOP_K = 3
SIMILARITY_THRESHOLD = 0.35