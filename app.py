import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from mood_utils import detect_mood
from prompts import get_prompt
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

st.set_page_config(
    page_title="AI Mental Health Checker",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🧘‍♀️ AI Mental Health Checker")
st.markdown('''Welcome to your anonymous AI support companion.  
Type or speak your thoughts below.'''
)


user_input = st.text_area("What's on your mind?", height=150)
input_ready = st.button("Analyze and Chat")


if input_ready and user_input.strip():
    with st.spinner("Analyzing mood and generating a response..."):
        mood = detect_mood(user_input)
        prompt = get_prompt(mood)
        full_prompt = f"{prompt}\n\nUser said: {user_input}\n\nYour response:"
        response = llm.invoke([HumanMessage(content=full_prompt)])

        st.markdown(f"###  Detected Mood: `{mood.title()}` ")
        st.markdown("### AI Response:")
        st.success(response.content)


elif input_ready and not user_input.strip():
    st.warning("Please provide some input.")
