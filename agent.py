from rag import FAQRetriever
from llm import GeminiLLM

from config import SIMILARITY_THRESHOLD


class FAQAgent:

    def __init__(self):

        self.retriever = FAQRetriever()

        self.llm = GeminiLLM()

    def run(self, question):

        results = self.retriever.search(
            question
        )

        if not results:

            return {
                "answer": (
                    "Sorry, I couldn't find "
                    "relevant information."
                ),
                "confidence": 0.0,
                "sources": []
            }

        best_score = results[0]["score"]

        if best_score < SIMILARITY_THRESHOLD:

            return {
                "answer": (
                    "Sorry, I couldn't find a "
                    "relevant answer in my FAQ "
                    "knowledge base."
                ),
                "confidence": best_score,
                "sources": []
            }

        context_parts = []

        for result in results:

            faq = result["faq"]

            context_parts.append(
                f"Question: {faq['question']}\n"
                f"Answer: {faq['answer']}"
            )

        context = "\n\n".join(
            context_parts
        )

        answer = self.llm.generate(
            question,
            context
        )

        return {
            "answer": answer,
            "confidence": best_score,
            "sources": results
        }