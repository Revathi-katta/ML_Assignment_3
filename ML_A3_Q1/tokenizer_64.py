
import pickle

def save_tokenizer(tokenizer, path='C:/Users/katta/Downloads/tokenizer_64.pkl'):
    # Save the tokenizer to a file
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_tokenizer(path='C:/Users/katta/Downloads/tokenizer_64.pkl'):
    # Load the tokenizer from a file
    with open(path, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer
