from django import forms

from tasks.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
