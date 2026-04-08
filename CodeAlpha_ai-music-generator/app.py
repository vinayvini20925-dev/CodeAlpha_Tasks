import streamlit as st
from transformers import pipeline
import scipy.io.wavfile as wav

st.title("AI Music Generator")

st.write("Generate music using Artificial Intelligence")

prompt = st.text_input("Enter music mood or style:")

if st.button("Generate Music"):

    st.write("Generating music... please wait ")

    generator = pipeline("text-to-audio", model="facebook/musicgen-small")

    music = generator(prompt)

    audio = music["audio"]
    rate = music["sampling_rate"]

    wav.write("generated_music.wav", rate, audio)

    st.audio("generated_music.wav")
    st.success("Music Generated Successfully")



    import streamlit as st

st.title("AI Music Generator ")

name = st.text_input("Enter music mood")

if st.button("Generate"):
    st.write("Generating music for:", name)