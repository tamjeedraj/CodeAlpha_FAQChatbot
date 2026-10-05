import json
import faiss
import numpy as np

from embeddings import EmbeddingModel
from preprocess import preprocess_text

from config import TOP_K


class FAQRetriever:

    def __init__(self, data_path="data/faqs.json"):

        self.data_path = data_path

        self.faqs = self._load_data()

        self.embedding_model = EmbeddingModel()

        self.questions = [
            faq["question"]
            for faq in self.faqs
        ]

        processed_questions = [
            preprocess_text(question)
            for question in self.questions
        ]

        embeddings = self.embedding_model.encode(
            processed_questions
        )

        embeddings = np.asarray(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.index.add(embeddings)

    def _load_data(self):

        with open(
            self.data_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def search(self, query, top_k=TOP_K):

        processed_query = preprocess_text(
            query
        )

        query_embedding = self.embedding_model.encode(
            [processed_query]
        )

        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0]
        ):

            results.append(
                {
                    "faq": self.faqs[index],
                    "score": float(score)
                }
            )

        return results