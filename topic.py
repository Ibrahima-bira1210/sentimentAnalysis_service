import spacy

nlp = spacy.load("fr_core_news_sm")


def get_Topic(text):
    doc = nlp(text)
    topics = []
    for sent in doc.sents:
        for chunk in sent.noun_chunks:
            topics.append(chunk.text)
    try:
        return topics[0]
    except IndexError:
        return ' '


text = ""

print(get_Topic(text))
