import os
import pickle

def save_tokenizer(tokenizer, path='tokenizer_32.pkl'):
    """Save the tokenizer to a file."""
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_tokenizer(path='tokenizer_32.pkl'):
    """Load the tokenizer from a file."""
    if os.path.exists(path):
        with open(path, 'rb') as f:
            tokenizer = pickle.load(f)
        return tokenizer
    else:
        raise FileNotFoundError(f"Tokenizer file not found at path: {path}")
