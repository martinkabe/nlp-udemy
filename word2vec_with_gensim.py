import os
import pandas as pd
import numpy as np
import nltk
from gensim import (
    corpora, models, similarities
)


def custom_tokenize(text):
    if not text or text != text:
        print('The text to be tokenized is a None type. Defaulting to blank string.')
        text = ''
    return nltk.word_tokenize(text)


def create_store_model(model_name: str) -> None:
    df = pd.read_csv("data/jokes.csv")
    print(f'Data has {df.shape[0]} rows and {df.shape[1]} columns')

    x = df['Question'].values.tolist()
    y = df['Answer'].values.tolist()

    corpus = x + y

    tok_corp = [custom_tokenize(sent) for sent in corpus]
    # for sent in corpus:
    #     print(custom_tokenize(sent))

    model = models.Word2Vec(
        sentences=tok_corp,
        min_count=1,
        vector_size=32
    )

    model.save(f'models/{model_name}')


def get_vectors(model: models.Word2Vec) -> dict:
    vectors = dict({})
    for idx, key in enumerate(model.wv.vocab):
        vectors[key] = model.wv.get_vector(key)
    return(vectors)


if __name__ == '__main__':
    # create_store_model(model_name='test_model')
    model = models.Word2Vec.load('models/test_model')
    most_similar_vectors = model.wv.most_similar('native')
    print(most_similar_vectors)
    print(model.wv.get_vector('native'))
