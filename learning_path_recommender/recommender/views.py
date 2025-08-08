from django.shortcuts import render, redirect
from .data.courses import course_data
from .ml_model import generate_learning_path
from django.contrib.auth.decorators import login_required

# Quiz question bank
quiz_questions = {
    "Python": [
        {"question": "What is a correct syntax to output 'Hello World' in Python?", "options": ["echo 'Hello World'", "p('Hello World')", "print('Hello World')"], "answer": "print('Hello World')"},
        {"question": "What data type is the object below? \nL = [1, 23, 'hello', 1]", "options": ["List", "Dictionary", "Tuple"], "answer": "List"},
    ],
    "Web Development": [
        {"question": "What does HTML stand for?", "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language"], "answer": "Hyper Text Markup Language"},
        {"question": "Which HTML tag is used to define an internal style sheet?", "options": ["<style>", "<script>", "<css>"], "answer": "<style>"},
    ],
    "Java": [
        {"question": "Which keyword is used to define a class in Java?", "options": ["function", "def", "class"], "answer": "class"},
        {"question": "Which method is the entry point of a Java program?", "options": ["start()", "main()", "run()"], "answer": "main()"},
    ],
}

def home(request):
    skills = list(quiz_questions.keys())
    return render(request, 'home.html', {'quiz_questions': quiz_questions, 'skills': skills})

@login_required
def recommend_path(request):
    if request.method == 'GET':
        skill = request.GET.get('skill')
        goal = request.GET.get('goal')
        if skill and goal:
            from django.urls import reverse
            return redirect(f"{reverse('my_recommendations')}?skill={skill}&goal={goal}")
    return redirect('home')

@login_required
def my_recommendations(request):
    skill = request.GET.get('skill')
    goal = request.GET.get('goal')
    if not skill or not goal:
        return redirect('home')

    recommended_path = generate_learning_path(skill, goal)
    courses = course_data.get(skill, [])
    return render(request, 'my_recommendations.html', {
        'skill': skill,
        'goal': goal,
        'recommended_path': recommended_path,
        'courses': courses
    })

@login_required
def quiz(request):
    skill = request.GET.get('skill')
    if not skill or skill not in quiz_questions:
        return redirect('home')

    questions = quiz_questions[skill]
    return render(request, 'quiz.html', {'skill': skill, 'questions': questions})

@login_required
def quiz_result(request):
    if request.method == 'POST':
        skill = request.POST.get('skill')
        user_answers = {}
        score = 0
        questions = quiz_questions.get(skill, [])

        for i, q in enumerate(questions):
            q_key = f"question_{i}"
            user_answer = request.POST.get(q_key)
            if user_answer == q["answer"]:
                score += 1
            user_answers[q["question"]] = user_answer

        recommended_path = generate_learning_path(skill, "improve")  # Using "improve" as generic goal
        courses = course_data.get(skill, [])
        return render(request, 'result.html', {
            'skill': skill,
            'score': score,
            'total': len(questions),
            'recommended_path': recommended_path,
            'courses': courses
        })
    else:
        return redirect('home')
