import os
from dotenv import load_dotenv
import json
from openai import OpenAI

# Load environment variables
load_dotenv()

# Set up AIML API token
API_TOKEN = os.getenv("AIML_API_TOKEN")
BASE_URL = "https://api.aimlapi.com"

client = OpenAI(
    api_key=API_TOKEN,
    base_url=BASE_URL,
)


def generate_ai_content(prompt, system_content):
    try:
        chat_completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=128,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating content: {e}")
        return None


def generate_resume_summary(job_title):
    system_content = "You are a professional resume writer. Be concise and impactful."
    prompt = f"Write a professional resume summary for a {job_title}:"
    return generate_ai_content(prompt, system_content)


def extract_keywords(job_title):
    system_content = "You are a job market expert. Provide relevant keywords."
    prompt = f"List relevant keywords for a {job_title}, separated by commas:"
    keywords = generate_ai_content(prompt, system_content)
    return [keyword.strip() for keyword in keywords.split(",")] if keywords else []


def generate_role_objectives(job_title):
    system_content = (
        "You are a career counselor. Provide clear and actionable objectives."
    )
    prompt = f"List role objectives for a {job_title}:"
    objectives = generate_ai_content(prompt, system_content)
    return (
        [obj.strip() for obj in objectives.split("\n") if obj.strip()]
        if objectives
        else []
    )


def generate_resume_content(job_title):
    content = {
        "resume_summary": generate_resume_summary(job_title),
        "optimized_keywords": extract_keywords(job_title),
        "role_objectives": generate_role_objectives(job_title),
    }
    return json.dumps(content, indent=2)


# Example usage
if __name__ == "__main__":
    job_title = input("Enter the job title: ")
    resume_content = generate_resume_content(job_title)
    print(resume_content)
