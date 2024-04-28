
import streamlit as st
from tasks import imageToText, textToSpeech, textToStory

def main():
    st.set_page_config(page_title="PicTalk", page_icon="📸")

    st.header("PicTalk")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        st.image(bytes_data, caption="Uploaded Image.", use_column_width=True)
        with open(f'data/{uploaded_file.name}', "wb") as f:
            f.write(bytes_data)
        scenario = imageToText(f'data/{uploaded_file.name}')
        story = textToStory(scenario)
        audio_file = textToSpeech(story)
        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)
        st.audio(audio_file)


if __name__ == "__main__":
    main()