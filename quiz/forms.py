from django import forms
from .models import AnswerVariant


class QuizForm(forms.Form):
    def __init__(self, *args, questions=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.questions = list(questions or [])

        answer_variants = AnswerVariant.objects.all().order_by("order")

        for question in self.questions:
            field_name = self.get_field_name(question)

            field = forms.ModelChoiceField(
                queryset=answer_variants,
                widget=forms.RadioSelect(attrs={"class": "answer-input"}),
                label=question.text,
                empty_label=None,
                required=True,
                error_messages={
                    "required": "Выберите один вариант ответа."
                },
            )

            field.label_from_instance = self.get_answer_label

            self.fields[field_name] = field
            self.fields[field_name].question = question

    @staticmethod
    def get_field_name(question):
        return f"question_{question.id}"

    @staticmethod
    def get_answer_label(answer):
        return answer.text

    def selected_answers(self):
        selected = []

        for question in self.questions:
            field_name = self.get_field_name(question)

            if field_name in self.cleaned_data:
                answer_variant = self.cleaned_data[field_name]
                selected.append((question, answer_variant))

        return selected