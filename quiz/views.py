from collections import defaultdict

from django.core.cache import cache
from django.shortcuts import render, redirect

from .forms import QuizForm
from .models import Test, Question, AnswerVariant


def quiz(request):
    test = Test.objects.filter(is_active=True).first()

    if not test:
        return render(request, "quiz/quiz.html", {
            "test": None,
            "form": None,
            "results": [],
        })

    questions = list(
        Question.objects
        .filter(test=test)
        .prefetch_related("professions")
        .order_by("order")
    )

    total_questions = len(questions)

    if total_questions == 0:
        return render(request, "quiz/quiz.html", {
            "test": test,
            "form": None,
            "results": [],
        })

    current_index = int(request.session.get("quiz_current_index", 0))

    if current_index < 0:
        current_index = 0

    if current_index >= total_questions:
        current_index = total_questions - 1

    current_question = questions[current_index]

    answers = request.session.get("quiz_answers", {})

    field_name = QuizForm.get_field_name(current_question)

    initial = {}

    if str(current_question.id) in answers:
        initial[field_name] = answers[str(current_question.id)]

    results = []

    if request.method == "POST":
        action = request.POST.get("action")

        form = QuizForm(
            request.POST,
            questions=[current_question]
        )

        if form.is_valid():
            for question, answer_variant in form.selected_answers():
                answers[str(question.id)] = answer_variant.id

            request.session["quiz_answers"] = answers

            if action == "next":
                current_index += 1

                if current_index >= total_questions:
                    current_index = total_questions - 1

                request.session["quiz_current_index"] = current_index
                return redirect("quiz")

            elif action == "back":
                current_index -= 1

                if current_index < 0:
                    current_index = 0

                request.session["quiz_current_index"] = current_index
                return redirect("quiz")

            elif action == "finish":
                scores = defaultdict(int)

                for question in questions:
                    answer_id = answers.get(str(question.id))

                    if answer_id:
                        answer_variant = AnswerVariant.objects.get(id=answer_id)

                        for profession in question.professions.all():
                            scores[profession] += answer_variant.points

                results = sorted(
                    [
                        {
                            "profession": profession,
                            "score": score
                        }
                        for profession, score in scores.items()
                    ],
                    key=lambda item: item["score"],
                    reverse=True
                )

                if not request.session.session_key:
                    request.session.create()

                cache_key = f"quiz_result_{request.session.session_key}_{test.id}"

                cache_data = []

                for item in results:
                    cache_data.append({
                        "profession_id": item["profession"].id,
                        "profession_title": item["profession"].title,
                        "score": item["score"],
                    })

                cache.set(cache_key, cache_data, timeout=3600)

                request.session.pop("quiz_current_index", None)
                request.session.pop("quiz_answers", None)

        else:
            current_index = int(request.session.get("quiz_current_index", 0))

    else:
        form = QuizForm(
            questions=[current_question],
            initial=initial
        )

    return render(request, "quiz/quiz.html", {
        "test": test,
        "form": form,
        "results": results,
        "current_index": current_index,
        "total_questions": total_questions,
        "current_number": current_index + 1,
        "is_first": current_index == 0,
        "is_last": current_index == total_questions - 1,
    })