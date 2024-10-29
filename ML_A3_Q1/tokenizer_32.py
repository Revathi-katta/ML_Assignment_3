import pickle
import gdown
import os

# Define the URL for the tokenizer file on Google Drive
TOKENIZER_URL = "https://drive.google.com/file/d/145sobjWSSubTtjQzFoMkBn_5aNKdLxHb/view?usp=sharing"

def download_tokenizer(path='tokenizer.pkl'):
    """Download the tokenizer from Google Drive if it doesn't exist locally."""
    if not os.path.exists(path):
        gdown.download(TOKENIZER_URL, path, quiet=False)
    return path

def load_tokenizer(path='tokenizer.pkl'):
    """Load the tokenizer from a file."""
    download_tokenizer(path)  # Ensure the tokenizer file is downloaded
    with open(path, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer

