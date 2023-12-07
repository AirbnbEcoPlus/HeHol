
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Load data
with open('data.json', 'r', encoding='utf-8') as f:
    raw_data = f.read()

# Preprocess data
def preprocess(data):
    # Tokenize data
    tokens = nltk.word_tokenize(data)
    
    # Lowercase all words
    tokens = [word.lower() for word in tokens]
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

# Train the model
def train_model(data):
    processed_data = [preprocess(qa) for qa in data.split('\n')]

    vocab_size = 5000
    embedding_dim = 64
    max_length = 100
    trunc_type = 'post'
    padding_type = 'post'
    oov_tok = "<OOV>"
    training_size = len(processed_data)

    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(processed_data)

    sequences = tokenizer.texts_to_sequences(processed_data)
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    training_data = padded_sequences[:training_size]
    training_labels = padded_sequences[:training_size]

    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Conv1D(64, 5, activation='relu'),
        tf.keras.layers.MaxPooling1D(pool_size=4),
        tf.keras.layers.LSTM(64),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(vocab_size, activation='softmax')
    ])

    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    num_epochs = 50
    history = model.fit(training_data, training_labels, epochs=num_epochs, verbose=2)

    return model, tokenizer



trained_model, trained_tokenizer = train_model(raw_data)

# Predict the answer
def predict_answer(model, tokenizer, question):
    question = preprocess(question)
    sequence = tokenizer.texts_to_sequences([question])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    pred = model.predict(padded_sequence)[0]
    idx = np.argmax(pred)
    answer = tokenizer.index_word[idx]
    return answer

# Start chatbot
def response(question):
    return predict_answer(trained_model, trainder_tokenizer, question)
        

