import streamlit as st
import torch
from model import NextWord
from tokenizer_32 import load_tokenizer as load_tokenizer_32
from tokenizer_64 import load_tokenizer as load_tokenizer_64
from tokenizer_32_holmes import load_tokenizer as load_tokenizer_32_holmes
from tokenizer_64_holmes import load_tokenizer as load_tokenizer_64_holmes

# Load Model
@st.cache_resource  # Caches model to avoid reloading on each interaction
def load_model(variant_name, block_size, embedding_dim, activation_func):
    # Load the tokenizer based on the model variant
    if variant_name == "embedding32_hidden1024":
        tokenizer = load_tokenizer_32()
    elif variant_name == "embedding64_hidden1024":
        tokenizer = load_tokenizer_64()
    elif variant_name == "embedding32_hidden1024_holmes":
        tokenizer = load_tokenizer_32_holmes()
    elif variant_name == "embedding64_hidden1024_holmes":
        tokenizer = load_tokenizer_64_holmes()
    else:
        raise ValueError(f"Unknown model variant: {variant_name}")

    stoi = tokenizer.word_index
    itos = {i: w for w, i in stoi.items()}

    # Initialize model with the selected activation function
    model = NextWord(block_size=block_size, vocab_size=len(stoi) + 1, emb_dim=embedding_dim, hidden_size=1024, activation_func=activation_func)
    
    # Load model weights
    state_dict = torch.load(f"C:/Users/katta/Downloads/{variant_name}.pt", map_location=torch.device('cpu'))
    compatible_state_dict = {k[len('_orig_mod.'):] if k.startswith('_orig_mod.') else k: v for k, v in state_dict.items()}
    model.load_state_dict(compatible_state_dict)
    model.eval()  # Set model to evaluation mode
    
    return model, tokenizer, stoi, itos

# User input
st.title("Next-Word Prediction")
user_input = st.text_input("Enter a sentence:", "The quick brown fox")
context_length = st.slider("Context Length", 1, 10, 5)
embedding_dim = st.selectbox("Embedding Dimension", [32, 64])
activation_func = st.selectbox("Activation Function", ["relu", "tanh", "sigmoid"])
variant = st.selectbox("Choose Model Variant", ["embedding32_hidden1024", "embedding64_hidden1024", "embedding32_hidden1024_holmes", "embedding64_hidden1024_holmes"])
word_count = st.slider("Number of words to predict", 1, 20, 10)  # Number of words to generate

# Load the selected model and tokenizer
model, tokenizer, stoi, itos = load_model(variant, context_length, embedding_dim, activation_func)

# Check for unknown words in user input
known_words = set(stoi.keys())
user_words = user_input.split()
missing_words = [word for word in user_words if word not in known_words]

if missing_words:
    st.warning(f"The following words are not in the vocabulary: {', '.join(missing_words)}. Using placeholders for unknown words.")

# Generate Prediction Function
def generate_prediction(model, input_text, word_count, context_length):
    tokens = tokenizer.texts_to_sequences([input_text])[0]
    
    # Replace unknown tokens with a placeholder
    context = [stoi.get('.', None)] * context_length  # Initialize context with padding if needed

    for token in tokens[-context_length:]:  # Populate context from user input
        if token is not None:  # Only add valid tokens to the context
            context = context[1:] + [token]
        else:
            context = context[1:] + [stoi.get('[UNK]', None)]  # Placeholder for unknown tokens

    sentence = ""
    for _ in range(word_count):
        x = torch.tensor([context], dtype=torch.long)
        
        # Ensure that x is not empty (context may be all placeholders)
        if x.size(1) == 0:
            break
        
        y_pred = model(x)
        ix = torch.distributions.Categorical(logits=y_pred).sample().item()
        word = itos.get(ix, "[UNK]")  # Default to "[UNK]" if the index is not in `itos`
        
        if word == '.':
            break
        sentence += word + " "
        context = context[1:] + [ix]  # Update context with predicted word
        
    return sentence.strip()

# Display generated prediction
if user_input and model:
    prediction = generate_prediction(model, user_input, word_count, context_length)
    st.write("Generated Text:", prediction)
