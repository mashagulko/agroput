from django import forms


class QuizForm(forms.Form):
    def __init__(self, *args, questions=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.questions = list(questions or [])

        for question in self.questions:
            field_name = self.get_field_name(question)
            self.fields[field_name] = forms.ModelChoiceField(
                queryset=question.answer_set.all().order_by('id'),
                widget=forms.RadioSelect(attrs={'class': 'answer-input'}),
                label=question.text,
                empty_label=None,
                required=True,
                error_messages={'required': 'Выберите один вариант ответа.'},
            )
            self.fields[field_name].question = question

    @staticmethod
    def get_field_name(question):
        return f'question_{question.id}'

    def selected_answers(self):
        return [
            self.cleaned_data[self.get_field_name(question)]
            for question in self.questions
            if self.get_field_name(question) in self.cleaned_data
        ]
