import streamlit as st
import base64
import openai
from openai import OpenAI
from tempfile import NamedTemporaryFile

# App title
st.set_page_config(page_title='👀 GPT4 Vision')
st.title('👀 GPT4 Vision')
st.info('This app is created using the GPT4 Vision from OpenAI.')

# API Credentials
#if 'OPENAI_API_KEY' in st.secrets:
#  st.success('API key already provided!', icon='✅')
#  openai.api_key = st.secrets['OPENAI_API_KEY']
#else:
#  openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
#  if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
#    st.warning('Please enter your credentials!', icon='⚠️')
#  else:
#    st.success('Proceed to entering your prompt message!', icon='👇')


# Upload image
image_upload = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


if image_upload:
  st.image(image_upload, use_column_width=True)

  # base64_image = encode_image(image_upload)
  # st.write(base64_image)

  bytes_data = image_file.read()
  with NamedTemporaryFile(delete=False) as tmp:
    tmp.write(bytes_data)
    st.write(tmp.name)
      #data = PyPDFLoader(tmp.name).load()
    #os.remove(tmp.name)
    
  

