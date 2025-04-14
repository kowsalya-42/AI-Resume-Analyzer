## 🚀 ATSResumeExpert  
**An AI-Powered Resume Analysis & Optimization Tool for Job Seekers**

ATSResumeExpert is a smart, privacy-focused resume evaluation tool that leverages **Google's Gemini AI** to simulate **Applicant Tracking System (ATS)** analysis. Built using **Streamlit**, it helps candidates align their resumes with job descriptions, optimize keyword usage, and receive personalized feedback to increase their chances of landing interviews.

![ATSResumeExpert Banner](https://github.com/user-attachments/assets/d240c37d-0153-4ea9-b5e8-05c6a2c14021)


### 🧠 Key Features

- 📄 **Resume Evaluation:** Get intelligent, role-specific feedback based on the job description  
- 💡 **Skillset Suggestions:** Identify missing or in-demand skills based on the job profile  
- 🔑 **Keyword Optimization:** Discover ATS-relevant keywords missing from your resume  
- 📊 **Match Percentage Calculation:** See how closely your resume matches the target role  
- 🎨 **Modern UI & Lottie Animations:** Responsive and visually appealing interface  
- 🔒 **Privacy First:** Resume data processed securely, with no storage of personal information


### 🛠️ Tech Stack

- **Frontend:** Streamlit + LottieFiles  
- **AI Backend:** Google Gemini API (`gemini-1.5-flash`)  
- **File Handling:** PyMuPDF (PDF to Image Conversion)  
- **Deployment:** Streamlit Sharing / Docker (Optional)  
- **Styling:** Custom CSS for enhanced UX  


### 📦 Getting Started

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/ATSResumeExpert.git
cd ATSResumeExpert
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Set Environment Variable**
Create a `.env` file and add your Gemini API key:
```
GOOGLE_API_KEY=your_key_here
```

4. **Run the Application**
```bash
streamlit run app.py
```


### 📂 Folder Structure

```
ATSResumeExpert/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .env                  # API key (excluded from version control)
└── assets/               # Animations and static files
```


### 📢 Contribution Guidelines

We welcome contributions from the community! Whether it's bug fixes, feature enhancements, or documentation improvements—feel free to submit a pull request or open an issue.


### 📄 License

This project is licensed under the [MIT License](LICENSE).


### 🙌 Acknowledgments

- [Google Gemini API](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [LottieFiles](https://lottiefiles.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)

