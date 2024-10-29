import pickle
import streamlit as st
import os

def save_tokenizer(tokenizer, path='tokenizer_64.pkl'):
    # Save the tokenizer to a file
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)
    st.success(f"Tokenizer saved to {path}")

def load_tokenizer(path='tokenizer_64.pkl'):
    # Load the tokenizer from a file
    if os.path.exists(path):
        with open(path, 'rb') as f:
            tokenizer = pickle.load(f)
        st.success(f"Tokenizer loaded from {path}")
        return tokenizer
    else:
        st.error(f"Tokenizer file not found at {path}")
        return None

# Example usage in your Streamlit app
st.title("Tokenizer Example")

# Load tokenizer when app runs
tokenizer = load_tokenizer()

if tokenizer is None:
    # Example: Create a new tokenizer if not loaded
    # tokenizer = create_tokenizer(your_data)
    save_tokenizer(tokenizer)
