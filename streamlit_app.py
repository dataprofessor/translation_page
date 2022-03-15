import streamlit as st
from googletrans import Translator, constants

# Language selection
languages_value = [i.capitalize() for i in constants.LANGUAGES.values()]
selected_language = st.sidebar.selectbox('Select a language', languages_value, index=languages_value.index('English'))
selected_language_symbol = list(constants.LANGUAGES.keys())[list(constants.LANGUAGES.values()).index(selected_language.lower())]

# Google API translator
def translate(text_input):
    translator = Translator()
    translation = translator.translate(text_input, dest=selected_language_symbol)
    return translation.text

# Page contents
text_page_title = 'Translation Page App'
st.header(f'🔤 {translate(text_page_title)}')

with st.expander(translate('About')):
    st.write(translate('This app displays a language selection box that users can choose so that the contents are translated to the selected language.'))

st.info(translate('Welcome to the app!'))
