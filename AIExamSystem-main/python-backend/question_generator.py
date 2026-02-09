import sys
import json
import re
import os
import google.generativeai as genai

# ------------------------------------
# AI Exam System - Question Generator
# ------------------------------------
# Generates 10 unique multiple-choice questions using Google Gemini API.
# Saves them in JSON format for later use.
#
# Usage (from Java or CLI):
# python question_generator.py <subject> <level>
#
# Example:
# python question_generator.py "Python" "Beginner"
# ------------------------------------

# ✅ Configure API using environment variable for security
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ Error: GEMINI_API_KEY environment variable not set.")
genai.configure(api_key=API_KEY)

# ✅ Load the model
model = genai.GenerativeModel("gemini-2.0-flash")

# ✅ Get subject and level from arguments
subject = sys.argv[1] if len(sys.argv) > 1 else "General Knowledge"
level = sys.argv[2] if len(sys.argv) > 2 else "Beginner"

def build_prompt(subject: str, level: str, count: int) -> str:
    """
    Build the prompt for generating a quiz question.
    """
    return f"""
Generate a {level} level multiple choice quiz question in {subject}.
Make it unique and totally different. Do not repeat previous questions.
Format exactly like this:
Q: <question text>
A. <option 1>
B. <option 2>
C. <option 3>
D. <option 4>
Answer: <A/B/C/D>

This is question number {count+1}.
"""

def parse_mcq(text: str):
    """
    Parse the generated text into a structured MCQ format.
    """
    match = re.search(
        r"Q:\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nAnswer:\s*([ABCD])",
        text, re.DOTALL
    )
    if not match:
        return None
    q, a, b, c, d, correct = match.groups()
    return {
        "subject": subject,
        "level": level,
        "question": q.strip(),
        "options": {"A": a.strip(), "B": b.strip(), "C": c.strip(), "D": d.strip()},
        "correct": correct.strip()
    }

# ✅ Generate questions
dataset = []
seen_questions = set()
tries = 0

print(f"📚 Generating 10 questions for subject: {subject}, level: {level}")

while len(dataset) < 10 and tries < 30:
    prompt = build_prompt(subject, level, len(dataset))
    try:
        response = model.generate_content(prompt)
        text = response.text
        parsed = parse_mcq(text)

        if parsed:
            question_text = parsed['question']
            if question_text not in seen_questions:
                dataset.append(parsed)
                seen_questions.add(question_text)
                print(f"✅ ({len(dataset)}/10): {question_text[:50]}...")
            else:
                print("⚠️ Duplicate question skipped.")
        else:
            print("❌ Failed to parse response.")
    except Exception as e:
        print(f"❌ Error: {e}")
    tries += 1

# ✅ Save the dataset
os.makedirs("data", exist_ok=True)  # Ensure 'data' folder exists
output_file = "data/questions_dataset.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4)

print(f"✅ Saved {len(dataset)} questions to '{output_file}'")
