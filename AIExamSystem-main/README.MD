# AI-Based Online Exam System

An **AI-driven online exam platform** built with **Java (Swing)** and **Python (backend)**.  
The system dynamically generates questions using **Google Gemini AI**, stores them in JSON format, and provides a **Java Swing GUI** for students to take the exam.

---

## ✅ Features
- **AI Question Generation**: Uses Google Gemini to create unique MCQs.
- **JSON Question Storage**: Questions saved in `data/questions_dataset.json`.
- **Java Swing GUI**: User-friendly interface for taking exams.
- **Scoring System**: Automatically checks answers and displays the final score.
- **Expandable**: Future integration with **proctoring** and **voice-based answers**.

---

## 🛠 Tech Stack
- **Frontend**: Java (Swing)
- **Backend**: Python 3
- **AI Model**: Google Gemini API
- **Data**: JSON
- **Libraries**:
  - **Java**: [Gson](https://github.com/google/gson) (for JSON parsing)
  - **Python**: `google-generativeai`

---

## 📂 Project Structure
    AI-Exam-System/
    │
    ├── java-frontend/
    │ ├── AIExamSystem.java # Main Java GUI code
    │ ├── lib/gson-2.10.jar # JSON parsing library
    │
    ├── python-backend/
    │ ├── question_generator.py # Python script for question generation
    │ ├── requirements.txt # Python dependencies
    │
    ├── data/
    │ ├── questions_dataset.json # Generated question set
    │
    ├── README.md # Project documentation
    ├── LICENSE
    └── .gitignore

---

## ⚙️ Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/EbrahimAR/AIExamSystem.git
cd AI-Exam-System
```

### **2. Set Up Python Backend**

Install dependencies:

```bash
cd python-backend
pip install -r requirements.txt
```

Create an environment variable for the Gemini API key:

```bash
export GEMINI_API_KEY="your_api_key"
```

Generate questions:

```bash
python question_generator.py "Java" "Beginner"
```

This will save questions in data/questions_dataset.json.

### **3. Set Up Java Frontend**
Open **java-frontend/AIExamSystem.java** in IntelliJ, Eclipse, or NetBeans.

Add Gson library:

1. Download `gson-2.10.jar`

2. Place it in `java-frontend/lib/`

3. Add it to the project classpath.

Compile and run the Java file.

---

## ▶️ Usage
1. Generate questions using the Python script.

2. Launch the Java GUI application.

3. Answer all questions displayed in the GUI.

4. Submit answers to see your final score.

---

## 🔗 Future Enhancements
- Facial Recognition Proctoring using OpenCV.

- Speech Recognition for voice-based answers.

- FastAPI Integration for real-time question generation.

- JWT Authentication for secure user management.

---

## 👨‍💻 Author
Ebrahim Abdul Raoof

[LinkedIn](https://www.linkedin.com/in/ebrahim-ar/)

[GitHub](https://github.com/EbrahimAR)

---

## 📜 License
This project is licensed under the MIT License. See [LICENSE](https://github.com/EbrahimAR/AIExamSystem/blob/main/LICENSE) for details.
