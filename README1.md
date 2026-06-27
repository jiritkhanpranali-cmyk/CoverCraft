CoverCraft: AI-Based Intelligent Cover Letter Generator Using Local Large Language Model

Author: Pranali Jiritkhan  
Project Type: Artificial Intelligence / Natural Language Processing Application  
Abstract
CoverCraft is an AI-powered intelligent cover letter generation system that automatically creates professional and personalized cover letters based on candidate information, resume details and job requirements. The system uses Natural Language Processing (NLP) techniques and a Large Language Model (LLM) to understand user information and generate context-aware cover letters.
The system provides features such as resume parsing, skill extraction, ATS-based resume matching, missing skill identification, job comparison, user authentication, cover letter history management and document export. CoverCraft reduces manual effort in preparing job applications and improves the quality of professional communication between candidates and recruiters.
Keywords:Artificial Intelligence, Natural Language Processing, Large Language Model, Resume Analysis, Cover Letter Generator, Streamlit, Ollama
I. Introduction
Problem Statement
Creating customized cover letters for different job applications is a time-consuming task. Many candidates struggle to highlight their skills, experience, and achievements according to specific job requirements.
Traditional methods require manually writing and editing cover letters for every job application, which reduces efficiency and personalization.
The objective of CoverCraft is to develop an AI-based system that automatically generates professional cover letters by analyzing resumes and job descriptions.
II. Methodology
The proposed system follows an AI-driven workflow:
1. Resume Upload and Parsing- The user uploads a resume PDF. The system extracts text information using PDF parsing techniques.
2. Information Extraction-Important candidate information is extracted:
- Name
- Email
- Phone number
- Technical skills
- Soft skills
- Education
- Projects
- Certifications
3. Resume-Job Matching- The system compares resume skills with job descriptions and calculates an ATS compatibility score. It identifies:
- Matched skills
- Missing skills
- Improvement suggestions
4. AI Cover Letter Generation-A Large Language Model generates a personalized cover letter based on:
- Candidate details
- Job role
- Company name
- Skills
- Experience
- Job description
5. Document Generation-The generated letter can be exported as:
- PDF
- DOCX
Tools and Technologies Used
Programming Language- Python
Framework- Streamlit
Streamlit is used to create an interactive web-based user interface for the application.
AI Model-Ollama + Llama 3
A locally running Large Language Model is used for generating professional cover letters.
Libraries
- Streamlit
- PyPDF
- Python-docx
- ReportLab
- SQLite
- bcrypt
III. Literature Review
Several existing systems focus on resume analysis and automated job recommendation.Existing solutions include:
1. Resume Screening Systems-These systems mainly focus on filtering resumes using keyword matching.
2. Online Cover Letter Generators-These platforms generate templates but provide limited personalization.
3. AI Writing Assistants-Modern AI assistants generate text but do not deeply analyze resume-job compatibility.
Advantages of Proposed System
- Reduces manual cover letter writing effort
- Provides personalized job application content
- Improves resume-job compatibility
- Detects missing skills
- Works with local AI model
- Provides downloadable documents
- User-friendly interface
 IV. Implementation
The application is implemented using Python and Streamlit. Streamlit was selected because:
- It provides rapid development of AI applications
- It supports interactive UI components
- It integrates easily with Python libraries
- It simplifies deployment
System modules:
1. User Authentication Module-Handles registration and login.
2. Resume Parser Module-Extracts information from uploaded resumes.
3. Analyzer Module-Calculates ATS score and provides suggestions
4. AI Generation Module-Uses LLM to create professional cover letters.
5. Database Module-Stores user data and generated letters using SQLite.
V. Conclusion
CoverCraft successfully demonstrates an AI-based approach for automated cover letter generation. The system combines resume analysis, NLP and LLM technology to create personalized professional documents.
The developed solution reduces job application preparation time and helps candidates improve their application quality.
VI. Future Scope
Future improvements include:
- Cloud-based AI model integration
- Voice-based resume input
- Multiple language support
- Advanced recruiter analytics
- Real-time job portal integration
- AI interview preparation assistant
VII.References
[1] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, 
A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, 
G. Krueger, T. Henighan, R. Child, A. Ramesh, D. Ziegler, J. Wu, C. Winter, 
C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, 
S. McCandlish, A. Radford, I. Sutskever, and D. Amodei, 
"Language Models are Few-Shot Learners," 
Advances in Neural Information Processing Systems (NeurIPS), vol. 33, pp. 1877–1901, 2020
[2] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, 
L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, 
"Attention Is All You Need," 
31st Conference on Neural Information Processing Systems (NeurIPS), 2017.
[3] J. Devlin, M. Chang, K. Lee, and K. Toutanova, 
"BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," 
Proceedings of NAACL-HLT, pp. 4171–4186, 2019.
[4] OpenAI, 
"GPT Models and Large Language Models for Natural Language Processing Applications," 
OpenAI Technical Documentation.
[5] Ollama Team, 
"Ollama: Run Large Language Models Locally," 
Available: https://ollama.com
[6] Streamlit Inc., 
"Streamlit Documentation: The Fastest Way to Build Data Apps in Python," 
Available: https://streamlit.io
[7] M. A. Hearst, 
"Untangling Text Data Mining," 
Proceedings of the 37th Annual Meeting of the Association for Computational Linguistics, 1999.
[8] S. Bird, E. Klein, and E. Loper, 
"Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit," 
O'Reilly Media, 2009.
[9] R. Baeza-Yates and B. Ribeiro-Neto, 
"Modern Information Retrieval: The Concepts and Technology Behind Search," 
2nd Edition, Addison-Wesley, 2011.
[10] Python Software Foundation, 
"Python Documentation," 
Available: https://www.python.org/doc/
[11] SQLite Consortium, 
"SQLite Database Documentation," 
Available: https://sqlite.org/docs.html
[12] ReportLab, 
"ReportLab PDF Generation Library Documentation," 
Available: https://docs.reportlab.com
[13] PyPDF Development Team, 
"PyPDF Documentation: PDF Processing Library for Python," 
Available: https://pypi.org/project/pypdf/
[14] Microsoft Research, 
"Resume Parsing and Information Extraction Techniques Using Natural Language Processing," 
Microsoft Research Publications.
[15] IEEE Computer Society, 
"IEEE Editorial Style Manual for Authors," 
IEEE Publications..
