from collections import defaultdict

from django.shortcuts import render
from .forms import QuizForm
from .models import Test, Question, TestResult

def quiz (request):
    test = Test.objects.prefetch_related('question_set__answer_set', 'question_set__professions').first()
    questions = (
        Question.objects
        .filter(test=test)
        .prefetch_related('answer_set', 'professions')
        .order_by('id')
    ) if test else []
    results = []

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            scores = defaultdict(int)

            for answer in form.selected_answers():
                for profession in answer.question.professions.all():
                    scores[profession] += answer.score

            results = sorted(
                [{'profession': profession, 'score': score} for profession, score in scores.items()],
                key=lambda item: item['score'],
                reverse=True,
            )

            user = request.user if request.user.is_authenticated else None
            for item in results[:3]:
                TestResult.objects.create(
                    user=user,
                    profession=item['profession'],
                    score=item['score'],
                )
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz/quiz.html', {
        'test': test,
        'questions': questions,
        'form': form,
        'results': results,
    })
