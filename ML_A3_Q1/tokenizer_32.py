import json
import pickle

from keras.preprocessing.text import tokenizer_from_json

def save_tokenizer(tokenizer, path='tokenizer_32.pkl'):
    # Save the tokenizer to a file
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_tokenizer(path='tokenizer_32.pkl'):
    # Load the tokenizer from a file
    with open(path, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer

def load_tokenizer_json(path='tokenizer_32.json'):
    # Load the tokenizer from a JSON file
    with open(path) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    return tokenizer
