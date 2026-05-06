from django.shortcuts import render
from .models import Test, Question

def quiz (request):
    test = Test.objects.prefetch_related('question_set__answer_set').first()
    questions = Question.objects.filter(test=test).prefetch_related('answer_set') if test else []
    first_question = questions[0] if questions else None

    return render(request, 'quiz/quiz.html', {
        'test': test,
        'questions': questions,
        'first_question': first_question,
    })
