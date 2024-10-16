import streamlit as st
import cohere
import requests  # For making API calls
from redlines import Redlines

# Set up the Cohere API key
cohere_api_key = st.secrets["cohere"]["cohere_api_key"]
cohere_client = cohere.Client(cohere_api_key)

# ChatGPT-like color palette CSS
def custom_chatgpt_style():
    st.markdown("""
        <style>
        body {
            background-color:#010101;  /* Light gray background */
        }
        .white-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            color: black; /* Dark gray text */
            margin-bottom: 20px;
        }
        .white-container a {
            color: #10a37f;  /* Teal color for links */
            text-decoration: none;
        }
        .white-container strong {
            color: black;  /* Dark gray for strong text (titles) */
        }
        h1, h2, h3, h4 {
            color: white;  /* Dark gray for headers */
        }
        .stButton>button {
            background-color: #10a37f;  /* Teal color for buttons */
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #128274; /* Slightly darker teal for hover state */
        }
        </style>
    """, unsafe_allow_html=True)

def generate_response(prompt, max_tokens=200, temperature=0.5):
    """Helper function to call the Cohere API and return the result."""
    bot_role = "You are an intelligent assistant that helps users improve their research papers. Your role is to rewrite content in an academic style, convert bullet points into well-structured paragraphs, summarize key points for presentation slides, proofread and provide grammar/style corrections, and assist users in finding top-cited research papers. Your responses are concise, clear, and maintain a formal, academic tone. You prioritize enhancing clarity, coherence, and professionalism in academic writing."
    
    try:
        response = cohere_client.generate(
            model="command-xlarge",  # Using a larger Cohere model for better performance
            prompt=f"{bot_role} {prompt}",
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.generations[0].text if response.generations else "No response generated."
    except Exception as e:
        return f"Error generating response: {e}"

# Function to search for papers on CrossRef
def search_crossref(topic):
    url = f"https://api.crossref.org/works?query={topic}&rows=5&sort=score"
    try:
        response = requests.get(url)
        data = response.json()
        return data['message']['items'] if 'items' in data['message'] else []
    except Exception as e:
        return f"Error retrieving papers: {e}"

def academic():
    if st.session_state.user:
        prompt = f"Rewrite the following text, delimited by triple backticks, in academic style: ```{st.session_state.user}```"
        response = generate_response(prompt, max_tokens=500)

        st.subheader("Text with corrections (Tracked Changes)")
        diff = Redlines(st.session_state.user, response)
        st.markdown(f'<div class="white-container">{diff.output_markdown}</div>', unsafe_allow_html=True)

        st.subheader("Rewritten text")
        st.markdown(f'<div class="white-container">{response}</div>', unsafe_allow_html=True)

def bullet():
    if st.session_state.user:
        prompt = f"Convert the following bullet points into one cohesive paragraph, delimited by triple backticks: ```{st.session_state.user}```"
        response = generate_response(prompt, max_tokens=300)
        st.markdown(f'<div class="white-container">{response}</div>', unsafe_allow_html=True)

def slides():
    if st.session_state.user:
        prompt = f"Summarize the following text for presentation slides. Provide bullet points summarizing key concepts: ```{st.session_state.user}```"
        response = generate_response(prompt, max_tokens=300, temperature=0.4)
        st.markdown(f'<div class="white-container">{response}</div>', unsafe_allow_html=True)

def proofreading():
    if st.session_state.user:
        prompt = f"Proofread the following text for grammar, style, and clarity. Provide suggestions for improvement: ```{st.session_state.user}```"
        response = generate_response(prompt, max_tokens=300, temperature=0.3)
        st.subheader("Proofreading Suggestions")
        st.markdown(f'<div class="white-container">{response}</div>', unsafe_allow_html=True)

def find_research_papers():
    if st.session_state.user:
        st.subheader("Top Cited Research Papers")
        papers = search_crossref(st.session_state.user)
        if papers:
            for paper in papers:
                title = paper['title'][0] if 'title' in paper else "No title available"
                doi = paper.get('DOI', None)
                link = f"https://doi.org/{doi}" if doi else "No DOI available"
                st.markdown(f'<div class="white-container"><strong>{title}</strong><br><a href="{link}">Read Paper</a></div>', unsafe_allow_html=True)
        else:
            st.write("No papers found for this topic.")

st.title(":green[AiRes] 💡")
st.write("# Enhance your research papers with AI-powered tools")

# Apply ChatGPT-like styles
custom_chatgpt_style()

# Create Streamlit widgets
st.text_area("Provide your text or topic:", key="user")
option = st.selectbox("Select what would you like the AiRes bot to do:", 
                      ('Find top cited research papers',
                        'Proofread my text and output errors',
                        'Rewrite in academic style', 
                       'Write a paragraph from my bullet point list', 
                       'Summarize text in bullet points for slides', 
                       ))

if option == 'Rewrite in academic style':
    academic()
elif option == 'Write a paragraph from my bullet point list':
    bullet()
elif option == 'Summarize text in bullet points for slides':
    slides()
elif option == 'Proofread my text and output errors':
    proofreading()
else:
    find_research_papers()
