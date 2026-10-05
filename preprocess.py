import spacy


nlp = spacy.load("en_core_web_sm")


def preprocess_text(text: str) -> str:

    doc = nlp(text.lower())

    tokens = []

    for token in doc:

        if token.is_space:
            continue

        if token.is_punct:
            continue

        if token.is_stop:
            continue

        if token.like_num:
            continue

        lemma = token.lemma_.strip()

        if lemma:
            tokens.append(lemma)

    return " ".join(tokens)