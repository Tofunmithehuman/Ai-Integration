import json
import random

def generate_resume_summary(job_title):
    summaries = {
        "Senior Software Engineer": "Experienced Senior Software Engineer with a proven track record in designing and developing robust, scalable applications. Skilled in leading complex projects and mentoring junior developers. Proficient in multiple programming languages, cloud technologies, and agile methodologies. Strong problem-solving abilities with a focus on writing efficient, high-quality code and implementing best practices in software development.",
        "Data Scientist": "Results-driven Data Scientist with expertise in statistical analysis, machine learning, and data visualization. Experienced in developing predictive models and extracting actionable insights from large datasets. Proficient in Python, R, and SQL, with a track record of driving data-informed decision-making across various industries. Skilled in communicating complex findings to both technical and non-technical stakeholders.",
        "AI Engineer": "Innovative AI Engineer with extensive experience in developing and deploying machine learning models and AI systems. Proficient in deep learning frameworks, natural language processing, and computer vision. Skilled in optimizing AI algorithms for performance and scalability. Strong background in data preprocessing, feature engineering, and model evaluation. Experienced in integrating AI solutions into production environments.",
        "Product Manager": "Strategic Product Manager with a proven ability to drive product vision and execution. Skilled in market analysis, user experience design, and cross-functional team leadership. Experienced in Agile methodologies and adept at balancing stakeholder needs with technical constraints. Track record of delivering innovative products that exceed user expectations and drive business growth."
    }
    return summaries.get(job_title, f"Experienced {job_title} with a strong background in the field, demonstrating expertise in relevant skills and technologies. Proven track record of success in delivering high-quality results and collaborating effectively with cross-functional teams.")

def extract_keywords(job_title):
    keywords = {
        "Senior Software Engineer": [
            "Software Development", "Java", "Python", "C++", "JavaScript",
            "Cloud Computing", "Agile Methodologies", "CI/CD", "Microservices",
            "RESTful APIs", "Database Design", "System Architecture",
            "Version Control", "DevOps", "Test-Driven Development", "Scalability"
        ],
        "Data Scientist": [
            "Machine Learning", "Statistical Analysis", "Python", "R", "SQL",
            "Data Visualization", "Big Data", "Predictive Modeling",
            "Natural Language Processing", "Deep Learning", "Data Mining",
            "A/B Testing", "Hadoop", "Spark", "TensorFlow", "Scikit-learn"
        ],
        "AI Engineer": [
            "Artificial Intelligence", "Machine Learning", "Deep Learning",
            "Natural Language Processing", "Computer Vision", "Neural Networks",
            "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Feature Engineering",
            "Model Optimization", "AI Ethics", "Reinforcement Learning",
            "Data Preprocessing", "Algorithm Design"
        ],
        "Product Manager": [
            "Product Strategy", "Agile", "Scrum", "User Experience", "Market Research",
            "Competitive Analysis", "Product Roadmapping", "Stakeholder Management",
            "KPI Tracking", "Product Lifecycle", "A/B Testing", "User Stories",
            "Prioritization", "Product Launch", "Customer Feedback", "Data-Driven Decision Making"
        ]
    }
    return keywords.get(job_title, [
        "Leadership", "Communication", "Problem Solving", "Teamwork",
        "Project Management", "Time Management", "Analytical Skills",
        "Attention to Detail", "Creativity", "Adaptability", job_title
    ])

def generate_role_objectives(job_title):
    objectives = {
        "Senior Software Engineer": [
            "Design and develop scalable, high-performance software applications",
            "Lead complex projects and mentor junior developers",
            "Implement best practices for coding, testing, and deployment",
            "Collaborate with cross-functional teams to deliver high-quality products",
            "Optimize system architecture for improved performance and reliability",
            "Stay current with emerging technologies and industry trends"
        ],
        "Data Scientist": [
            "Develop and implement advanced machine learning models",
            "Analyze large datasets to extract actionable insights",
            "Create data visualizations to communicate findings effectively",
            "Collaborate with stakeholders to define and solve business problems",
            "Implement statistical methods to validate hypotheses and support decision-making",
            "Stay up-to-date with the latest advancements in data science and analytics"
        ],
        "AI Engineer": [
            "Design and develop AI models and algorithms for various applications",
            "Implement and optimize machine learning pipelines",
            "Integrate AI solutions into existing systems and workflows",
            "Collaborate with data scientists and software engineers on AI projects",
            "Evaluate and improve AI model performance and accuracy",
            "Research and implement cutting-edge AI techniques and technologies"
        ],
        "Product Manager": [
            "Define and execute product strategy aligned with business goals",
            "Gather and prioritize product requirements from stakeholders",
            "Lead cross-functional teams throughout the product development lifecycle",
            "Analyze market trends and competitor activities to inform product decisions",
            "Monitor and report on key product metrics and KPIs",
            "Collaborate with UX/UI teams to ensure optimal user experience"
        ]
    }
    return objectives.get(job_title, [
        f"Lead and execute projects in the field of {job_title}",
        "Collaborate with cross-functional teams to achieve organizational goals",
        f"Analyze and solve complex problems related to {job_title}",
        f"Stay current with industry trends and best practices in {job_title}",
        "Contribute to the continuous improvement of processes and methodologies",
        "Mentor and guide team members in areas of expertise"
    ])

def generate_resume_content(job_title):
    content = {
        "resume_summary": generate_resume_summary(job_title),
        "optimized_keywords": extract_keywords(job_title),
        "role_objectives": generate_role_objectives(job_title)
    }
    return json.dumps(content, indent=2)

# Example usage
job_title = input("Enter the job title: ")
resume_content = generate_resume_content(job_title)
print(resume_content)