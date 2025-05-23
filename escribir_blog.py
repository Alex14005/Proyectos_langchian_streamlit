import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

st.set_page_config(
    page_title= "Blog Post Generator Aerospace"
)

st.title("Blog Pos Generator")

groq_api_key=st.sidebar.text_input(
    "Groq Api Key",
    type="password"   
)

def generate_response(topic):
    llm = ChatGroq( model="gemma2-9b-it", groq_api_key=groq_api_key)
    template="""
    Como escritor y divulgador de la ingenieria aeroespacial y temas relacionados
    gener una entrada de blog de 400 palabras sobre {topic}

    Tu respuesta debe tener este formato:
    Primero, imprime la entrada del blog.
    Despues, suma el numero total de palabras e imprime el resultado asi:
    """
    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template
    )
    query= prompt.format(topic=topic)
    response=llm(query, max_tokens=2048)
    return st.write(response)

topic_text=st.text_input("Enter topic: ")
if not groq_api_key.startswith("sk-"):
    st.warning("Falta tu Groq Api Key")
if groq_api_key.startswith("sk-"):
    generate_response(topic_text)