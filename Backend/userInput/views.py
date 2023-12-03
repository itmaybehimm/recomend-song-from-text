from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils.spotify_integration import main_function
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import tensorflow as tf
from tensorflow.keras import Sequential
import pickle
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import sklearn
import requests


def home(request):
    return render(request, 'index.html')


def clean_data(text):
    # removing @ tags
    text = re.sub(r'@[a-zA-z0-9]+\s*', ' ', str(text))

    # removing urls
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'www\.\S+', '', text)

    # replacing multiple whitesapces by a single
    text = re.sub(r'\s+', ' ', text)

    # remove all single characters(surrounded by whitespace)
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)

    # remove all single characters except i and I (surrounded by whitespace)
    # text = re.sub(r'\s+(?![iI])[a-zA-Z]\s+', ' ', text)

    # Converting to Lowercase
    text = text.lower()

    # Lemmatization- splits into list of words ['The', 'quick', ....]
    text = text.split()

    lemma = WordNetLemmatizer()
    text = [lemma.lemmatize(word) for word in text]
    text = ' '.join(text)

    words = nltk.word_tokenize(text)

    # Get the list of stopwords
    stop_words = set(stopwords.words('english'))

    # Remove stopwords from the text
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Recreate the text without stopwords
    filtered_text = ' '.join(filtered_words)

    return filtered_text


def process(request):
    if request.method == 'POST':
        text_input = request.POST.get('textPrompt', '')

        file = request.FILES.get('fileInput')

        # process here

        # just printt
        print('Text Input:', text_input)
        print('File:', file)

    return HttpResponse("Successs")


@api_view(['POST'])
def integrate_spotify(request, username, mood):
    mood = float(mood)
    main_function(username, mood)
    return Response("Spotify integration complete!", status=status.HTTP_200_OK)


@api_view(['POST'])
def mood_caluclate(request):
    with open('userInput/countvectorizer_2.pkl', 'rb') as f:
        count_vectorizer = pickle.load(f)

        sentiment_mapping = {
            '0': 0,
            '1': 1,
            '2': 0.8,
            '3': 0.2,
            '4': 0.4,
            '5': 0.6,
        }

        X = ['makes feel wonderful']

        X = count_vectorizer.transform(X).toarray()

        _, m = X.shape

        opt = tf.keras.optimizers.Adam()

        loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        batch_size = 1000

        model = Sequential(
            [tf.keras.Input(shape=(m,)),
             tf.keras.layers.Dense(units=3000, activation='relu'),
             tf.keras.layers.Dense(units=600, activation='relu'),
             tf.keras.layers.Dense(units=400, activation='relu'),
             tf.keras.layers.Dense(units=260, activation='relu'),
             tf.keras.layers.Dense(units=30, activation='relu'),
             tf.keras.layers.Dense(units=8, activation='linear')])

        model.compile(loss=loss, optimizer=opt, metrics='accuracy')

        model.load_weights('userInput/model_2.h5')

        X = [
            str(request.data['feel'])
        ]

        X = [clean_data(x) for x in X]

        X = count_vectorizer.transform(X).toarray()

        y = model.predict(X)
        y = np.argmax(y)
        mood_score = sentiment_mapping[str(y)]

        username = 'kb'
        mood = float(mood_score)
        main_function(username, mood)
        return Response(mood_score)
