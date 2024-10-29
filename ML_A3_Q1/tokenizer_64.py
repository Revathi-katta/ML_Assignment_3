
import os
import pickle
import streamlit as st

def save_tokenizer(tokenizer, path='tokenizer_64.pkl'):
    # Save the tokenizer to a file
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_tokenizer(path=None):
    # Load the tokenizer from a file
    path = path or os.path.join(os.path.dirname(_file_), 'tokenizer_64.pkl')
    st.write("Loading tokenizer from:", path)
    
    if os.path.exists(path):
        with open(path, 'rb') as f:
            tokenizer = pickle.load(f)
        return tokenizer
    else:
        st.error(f"Tokenizer file not found at path: {path}")
        return None
