
import pickle

def save_tokenizer(tokenizer, path='tokenizer_64_holmes.pkl'):
    # Save the tokenizer to a file
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_tokenizer(path=r"tokenizer_64_holmes.pkl"):
    # Load the tokenizer from a file
    with open(path, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer
