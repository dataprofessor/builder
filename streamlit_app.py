import streamlit as st
import base64
import time
import openai
from openai import OpenAI
from tempfile import NamedTemporaryFile
from streamlit_image_select import image_select

# App title
st.set_page_config(page_title='🎈 Streamlit App Builder', page_icon='🎈', layout='wide')
st.title('🎈 Streamlit App Builder')
st.info('In this app you can **Show** (provide mock-up image) or **Tell** (provide text prompt) how you want your Streamlit app to be built.')
# This app builder is created using the GPT-4 with Vision (GPT-4V) from OpenAI.

# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
}

</style>
""", unsafe_allow_html=True)


# Initialize OpenAI client with API key
api_key = st.secrets['OPENAI_API_KEY']
client = OpenAI(api_key=api_key)

tabs = st.tabs(['Show', 'Tell'])

# Show how the app should be built
with tabs[0]:
    # Upload image
    st.subheader('Upload your own mock-up image')
    image_upload = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])
    
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

    # Example images
    example_img = st.toggle('Try example mock-up images')
    if example_img:
        st.subheader('Try these example mock-up images')
        img = image_select(
                label="Select a cat",
                images=[
                         "https://bagongkia.github.io/react-image-picker/0e1abaf656c3367fc89f628f0d52ad11.jpg",
                         "https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg",
                         "https://bagongkia.github.io/react-image-picker/6c800cccebf18c24f51d5fd411818ac8.jpg",
                         "https://bagongkia.github.io/react-image-picker/eb0659e2eebacafff0601e1b93797d7c.jpg",
                        ],
                #captions=["A cat", "Another cat", "Oh look, a cat!", "Guess what, a cat..."],
                )
    
    with st.expander('Expand to edit prompt instructions'):
        prompt_instructions = st.text_area("Prompt instructions",
                                "You are an experienced Python developer who can build amazing Streamlit apps.\n"
                                "You will be given a mock-up image of a Streamlit app for which you will convert it to a Streamlit app by generating the Python code.\n"
                              )

    
    
    # Start LLM process
    start_button = st.button('Build', key='button_image_start')
    

    
    if 'img' in locals() or 'img' in globals():
        if start_button:
            with st.spinner('Processing ...'):
                time.sleep(1.5)
                if img == 'https://bagongkia.github.io/react-image-picker/0e1abaf656c3367fc89f628f0d52ad11.jpg':
                    st.code('Code 1')
                if img == 'https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg':
                    st.code('Code 2')
                if img == 'https://bagongkia.github.io/react-image-picker/6c800cccebf18c24f51d5fd411818ac8.jpg':
                    st.code('Code 3')
                if img == 'https://bagongkia.github.io/react-image-picker/eb0659e2eebacafff0601e1b93797d7c.jpg':
                    st.code('Code 4')
        

    
    elif image_upload is not None and api_key and start_button:
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
    
          # Clear results
          if st.button('Clear', key='button_image_clear'):
            os.remove(tmp.name)
        
        except Exception as e:
          st.error(f'An error occurred: {e}')
          
    else:
      if not image_upload and start_button:
      #if not image_upload and not img and start_button:
        st.warning('Please upload your mock-up image.')
      if not api_key:
        st.warning('Please provide your OpenAI API key.')


# Tell how the app should be built
with tabs[1]:
    text_prompt = st.text_area(
        "Describe details on the functionalities of the Streamlit app that you want to build.",
        "", 
        height=240
    )

    with st.expander('Expand to edit system prompt'):
        prompt_instructions = st.text_area("System Prompt",
                                "You are an experienced Python developer who can build amazing Streamlit apps.\n"
                              )
    
    # Start LLM process
    start_button = st.button('Build', key='button_text_start')
    
    if text_prompt is not None and api_key and start_button:
        with st.spinner('Processing ...'):
            messages=[
                        {"role": "system", "content": "You are an experienced Python developer who can build amazing Streamlit apps."},
                        {"role": "user", "content": text_prompt}
                      ]
        try:
          # Response generation
          full_response = ''
          message_placeholder = st.empty()
              
          for completion in client.chat.completions.create(
            model='gpt-4', messages=messages, 
            max_tokens=1280, stream=True):
                      
              if completion.choices[0].delta.content is not None:
                full_response += completion.choices[0].delta.content
                message_placeholder.markdown(full_response + '▌')
                      
          message_placeholder.markdown(full_response)
    
          # Clear results
          if st.button('Clear', key='button_text_clear'):
            os.remove(tmp.name)
        
        except Exception as e:
          st.error(f'An error occurred: {e}')
          
    else:
      if not text_prompt and start_button:
        st.warning('Please provide your text prompt.')
      if not api_key:
        st.warning('Please provide your OpenAI API key.')
