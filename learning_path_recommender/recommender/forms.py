# recommender/forms.py

from django import forms

# Skill and Goal Choices
SKILL_CHOICES = [
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("java", "Java"),
    ("data_science", "Data Science"),
    ("web_development", "Web Development"),
    ("react", "React"),
]

GOAL_CHOICES = [
    ("full_stack", "Full Stack Developer"),
    ("frontend", "Frontend Developer"),
    ("backend", "Backend Developer"),
    ("data_scientist", "Data Scientist"),
    ("ai_engineer", "AI Engineer"),
]

# ✅ QUESTION BANK (Expanded)
QUESTION_BANK = {
    "python": [
        {"question": "What is a lambda function?", "options": ["Anonymous function", "Loop", "Condition"]},
        {"question": "Which library is used for data analysis?", "options": ["NumPy", "Pandas", "Matplotlib"]},
    ],
    "javascript": [
        {"question": "What does `===` mean?", "options": ["Strict equality", "Assignment", "Increment"]},
        {"question": "Which is a JS framework?", "options": ["Django", "Flask", "React"]},
    ],
    "java": [
        {"question": "What is JVM?", "options": ["Java Virtual Machine", "Java Version Module", "None"]},
        {"question": "Which keyword is used to inherit a class?", "options": ["extends", "implements", "inherits"]},
    ],
    "data_science": [
        {"question": "Which language is mostly used in Data Science?", "options": ["Python", "Java", "PHP"]},
        {"question": "Which library is used for machine learning?", "options": ["Scikit-learn", "Django", "jQuery"]},
    ],
    "web_development": [
        {"question": "Which protocol is used for web?", "options": ["HTTP", "FTP", "SSH"]},
        {"question": "Which is a frontend language?", "options": ["HTML", "Python", "MySQL"]},
    ],
    "react": [
        {"question": "What is JSX?", "options": ["JavaScript XML", "JSON Syntax", "None"]},
        {"question": "Which hook is used for state?", "options": ["useState", "useEffect", "useRef"]},
    ],
}

# ✅ Function to Fetch Questions
def get_questions_for_skill(skill):
    return QUESTION_BANK.get(skill, [])

# ✅ Recommendation Form
class RecommendationForm(forms.Form):
    skill = forms.ChoiceField(choices=SKILL_CHOICES, label="Select Skill")
    goal = forms.ChoiceField(choices=GOAL_CHOICES, label="Select Career Goal")

# ✅ Skill Quiz Form
class SkillQuizForm(forms.Form):
    def __init__(self, skill=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = get_questions_for_skill(skill)
        for idx, q in enumerate(questions):
            self.fields[f"question_{idx}"] = forms.ChoiceField(
                label=q["question"],
                choices=[(opt, opt) for opt in q["options"]],
                widget=forms.RadioSelect,
            )
