from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Good, Review
from django.contrib.auth import get_user_model



class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('summary', 'description', 'category', 'picture')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["summary"] == cleaned_data["description"]:
            raise ValidationError("Название и описание задачи не должны быть одинаковыми!", code="message_error", params={"id": "id"})
        return cleaned_data

class GoodDeleteForm(forms.Form):
    summary = forms.CharField(max_length=120, required=True, label='Введите название задачи, чтобы удалить её')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label="Поиск")
