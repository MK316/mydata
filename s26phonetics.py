import streamlit as st
from gtts import gTTS
import io

# 1. Your Wordlist (You can add your 10 words here)
# Example: word_list = ["phonetics", "syntax", "pragmatics", ...]
word_list = [
    "Apple", "Banana", "Cherry", "Date", "Elderberry", 
    "Fig", "Grape", "Honeydew", "Iced-tea", "Jujube"
]

# --- App Interface ---
st.set_page_config(page_title="Listening Quiz", layout="centered")

st.title("🎧 Vocabulary Listening Quiz")
st.markdown("""
### Instructions
1. Click the **Play** button for each number.
2. Listen carefully to the word.
3. Write down what you hear in your notebook or a Markdown file.
---
""")

# 2. Generating Items
for i, word in enumerate(word_list[:10], start=1):
    col1, col2 = st.columns([1, 4])
    
    with col1:
        # Visualizing only the number to prevent "reading" the answer
        st.subheader(f"Item {i:02d}")
    
    with col2:
        # Generate TTS in-memory to keep the app fast and clean
        try:
            tts = gTTS(text=word, lang='en')
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            
            # Display the audio player without the text
            st.audio(audio_fp, format='audio/mp3')
        except Exception as e:
            st.error(f"Error generating audio for Item {i}")

# --- Footer for Teachers ---
st.divider()
st.info("💡 **Tip for Students:** Use headphones for better accuracy. You can play each audio as many times as you need.")
