
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

# img2txt
def imageToText(url):
    from transformers import pipeline
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = image_to_text(url)
    print(text)
    return text[0]['generated_text']

# imageToText('data/mom-and-daughter.jpeg')



# llm
def textToStory(text):
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    print(text)
    llm = ChatOpenAI()

    # Failed attempts , gpt didn't worked on PromptTemplate
    # prompt_command = """
    # You are a storyteller:
    # You can generate a short story based on a simple native the story should no longer than 80 words

    # STORY TITLE: {context}
    # STORY:
    # """

    # Instantiation using from_template (recommended)
    # https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.prompt.PromptTemplate.html
    # prompt = PromptTemplate.from_template(prompt_command)
    # formatted_prompt = prompt.format(context=text)
    # print(formatted_prompt)

    # chain = prompt | llm 
    # # chain.invoke({"input": "how can langsmith help with testing?"})
    # story = chain.invoke({"context": text})

    prompt = ChatPromptTemplate.from_messages([
        ("system", " You are a storyteller. You can generate a short story based on a simple native the story should no longer than 80 words"),
        ("user", "{context}")
    ])

   
    chain = prompt | llm 
    story = chain.invoke({"context": text})

    print(story)
    return story.content

# textToStory('there is a woman holding a baby in her lap and smiling')


# text to speech via inteference api.
def textToSpeech(text):
    import requests
    from datetime import datetime
    HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payload = {
        "inputs": text,
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    file_name = f"data/output-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.flac"
    with open(file_name, "wb") as f:
        f.write(response.content)
    return file_name
# textToSpeech("In a small village nestled among the rolling hills, a woman sat on her front porch. With the warm sunlight kissing her skin, she cradled a precious baby in her arms. As she gazed down at the tiny face looking up at her with innocent eyes, a radiant smile lit up her face. The soft coos of the baby blended with the gentle rustling of leaves, creating a symphony of love and peace that enveloped them both.")

# manual run
# image_explanation = imageToText('data/mom-and-daughter.jpeg')
# story = textToStory(image_explanation)
# textToSpeech(story)


