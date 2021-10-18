# -*- coding: utf-8 -*-
"""SentimentAnalysis.ipynb

Original file is located at
    https://colab.research.google.com/drive/109ZiRsDQVElX0HTJvCmuZA_C8sQ0Am4A
"""

# !pip install transformers

# !pip install tqdm

import spacy
from transformers import pipeline


# Defining a pipeline
classifier = pipeline("sentiment-analysis",
                      model="distilbert-base-uncased-finetuned-sst-2-english")

# importing ner
ner = spacy.load('en_core_web_sm')


class Models:
    def __init__(self):
        print("Analysis")

    def sentiment(self, text):
        # make list for storing the results
        result = []

        # appending the result in result dictionary
        result.append(classifier([text])[0]['label'])

        return result

    def entity(self, text):
        entity = []

        # appending the entities
        doc = ner(text)

        entity.append([(X.text, X.label_) for X in doc.ents])
        return entity
