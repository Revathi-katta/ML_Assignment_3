
import pickle

def save_tokenizer(tokenizer, path='C:/Users/katta/Downloads/tokenizer_32.pkl'):
    # Save the tokenizer to a file
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_tokenizer(path='C:/Users/katta/Downloads/tokenizer_32.pkl'):
    # Load the tokenizer from a file
    with open(path, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer
