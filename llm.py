from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiLLM:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, question, context):

        prompt = f"""
You are an FAQ AI assistant.

Your job is to answer the user's question
using ONLY the provided FAQ context.

Rules:
1. Do not invent information.
2. If the context does not contain enough
   information, say that the information is
   not available in the FAQ knowledge base.
3. Keep the answer clear and concise.
4. Answer naturally like a helpful chatbot.

FAQ Context:
{context}

User Question:
{question}

Answer:
"""

        interaction = self.client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt
        )

        return interaction.output_text