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

prompt_instructions = st.text_area("Prompt instructions",
            "You are an experienced Python developer who can build amazing Streamlit apps.\n"
            "You will be given a mock-up image of a Streamlit app for which you will convert it to a Streamlit app by generating the Python code."
            ""
           )

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


if image_upload:
  st.image(image_upload, use_column_width=True)

  # base64_image = encode_image(image_upload)
  # st.write(base64_image)

  bytes_data = image_upload.read()
  with NamedTemporaryFile(delete=False) as tmp:
    tmp.write(bytes_data)
    st.write(tmp.name)
    
    #os.remove(tmp.name)
    

# Start LLM process
start_button = st.button('Build')

# Initialize OpenAI client with API key
api_key = st.secrets['OPENAI_API_KEY']
client = OpenAI(api_key=api_key)

if image_upload is not None and api_key and start_button:
# if image_upload is not None and openai.api_key and start_button:
  with st.spinner('Processing ...'):
    base64_image = encode_image(tmp.name)
    
    messages = [
            {
                'role': 'user',
                'content': [
                    {'type': 'text', 'text': prompt_instructions},
                    {
                        'type': 'image_url', 'image_url': f'data:image/jpeg;base64,{base64_image}',
                    },
                ],
            }
        ]

    try:
      # Response generation
      full_response = ''
      message_placeholder = st.empty()
          
      for completion in client.chat.completions.create(
        model='gpt-4-vision-preview', messages=messages, 
        max_tokens=1280, stream=True):
                  
          if completion.choices[0].delta.content is not None:
            full_response += completion.choices[0].delta.content
            message_placeholder.markdown(full_response + '▌')
                  
      message_placeholder.markdown(full_response)
    
    except Exception as e:
      st.error(f'An error occurred: {e}')
      
else:
  if not image_upload and start_button:
    st.warning('Please upload your mock-up image.')
  if not api_key:
    st.warning('Please provide your OpenAI API key.')

