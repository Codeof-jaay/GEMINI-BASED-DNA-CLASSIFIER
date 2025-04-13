import streamlit as st
import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("AIzaSyBfijZ3PAx6mWtKrM5u8x86Yt3PpDMbEdw"))
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")  

# Streamlit app layout
st.title("DNA Classifier with Gemini Pro")
st.write("Enter a DNA sequence below and let Gemini tell you whether it's from a **human, bacterium, or virus**.")

# Text input
dna_sequence = st.text_area("DNA Sequence", height=150, placeholder="Enter or paste a DNA sequence (e.g. ATGGCGG...)")

# Button
if st.button("Classify DNA"):
    if not dna_sequence.strip():
        st.warning("Please enter a DNA sequence.")
    else:
        with st.spinner("Classifying..."):
            prompt = f"""
            You are a genomics expert.
            Analyze this DNA sequence: {dna_sequence}
            Determine whether it most likely originates from a human, bacterium, or virus.
            Explain your reasoning using genomic features like GC content, patterns, or known motifs.
            """
            try:
                response = model.generate_content(prompt)
                st.success("Classification Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")