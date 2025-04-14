from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
import fitz  # PyMuPDF for PDF to image conversion
import google.generativeai as genai
import requests

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Lottie Animation Function
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Convert PDF to image using PyMuPDF (fitz)
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        first_page = doc.load_page(0)  # load first page
        pix = first_page.get_pixmap()
        img_byte_arr = io.BytesIO(pix.tobytes("jpeg"))

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr.getvalue()).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Gemini API Call
def get_gemini_response(prompt, pdf_content, job_description):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, pdf_content[0], job_description])
    return response.text

# Streamlit UI Config
st.set_page_config(page_title="ATS Resume Expert", layout="wide")

st.markdown("""
    <style>
        .main { background-color: #f4f6fa; }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            background: -webkit-linear-gradient(#0072ff, #00c6ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #444;
            margin-bottom: 20px;
        }
        .stTextArea label, .stFileUploader label {
            font-weight: bold;
            font-size: 16px;
            color: #333;
        }
        .stButton button {
            background-color: #0072ff;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #005ce6;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Choose a page", ["🏠 Home", "📄 Resume Evaluation", "💡 Skillset Suggestions", "🔑 Missing Keywords", "📊 Match Percentage"])

# Load Lottie Animation
lottie_url = "https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json"

if page == "🏠 Home":
    st.markdown("<div class='title'>Welcome to ATS Resume Expert</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Unleash the Power of AI to Land Your Dream Job</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.components.v1.html(f"""
            <lottie-player src="{lottie_url}" background="transparent" speed="1" style="width: 100%; height: 300px;" loop autoplay></lottie-player>
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        """, height=300)

    with col2:
        st.markdown("""
        ### ✨ What You Can Do:
        - Upload your resume 📄
        - Paste a job description 📋
        - Get AI-powered feedback 🧠
        - Understand your strengths & weaknesses
        - See your match % with key insights

        > Powered by Google's Gemini AI ✨
        """)

else:
    st.markdown(f"<div class='title'>{page}</div>", unsafe_allow_html=True)
    st.markdown("---")
    input_text = st.text_area("📋 Paste the Job Description:")
    uploaded_file = st.file_uploader("📎 Upload your Resume (PDF only):", type=["pdf"])

    prompts = {
        "📄 Resume Evaluation": """
            You are an experienced Technical Human Resource Manager with tech experience in any one field of data analysis, data science, machine learning engineering, AI engineering, DevOps, cloud computing, or cybersecurity. 
            Your task is to review the provided resume against the job description for these profiles. 
            Please share your professional evaluation on whether the candidate's profile aligns with the role. 
            Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
        """,
        "💡 Skillset Suggestions": """
            You are a career development coach with extensive knowledge in the fields of data analysis, data science, machine learning engineering, AI engineering, DevOps, cloud computing, or cybersecurity. 
            Your task is to review the provided resume and job description, and then suggest ways the candidate can improve their skillset to better align with the job requirements.
        """,
        "🔑 Missing Keywords": """
            You are an experienced ATS (Applicant Tracking System) specialist with deep knowledge of keyword optimization in resumes. 
            Your task is to review the provided resume and job description, and identify which important keywords are missing from the resume.
        """,
        "📊 Match Percentage": """
            You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one field of data analysis, data science, machine learning engineering, AI engineering, DevOps, cloud computing, or cybersecurity, and deep ATS functionality. 
            Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description. 
            First, provide the output as a percentage, then list the missing keywords, and finally, give your final thoughts.
         """
    }

    if st.button("🚀 Run ATS Analysis"):
        if uploaded_file and input_text:
            with st.spinner("Processing with Gemini AI..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_gemini_response(prompts[page], pdf_content, input_text)
            st.success("✅ Done!")
            st.subheader("📌 Result:")
            st.write(response)
        else:
            st.warning("⚠️ Please upload a resume and paste a job description.")
