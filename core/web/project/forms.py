from django import forms

from models.project.models import (
    Project,
    Task,
    TaskAssignment,
    TaskCategory,
    TaskComment,
)


class ProjectCreateForm(forms.ModelForm):
    """
    Project create form
    """

    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "end_date"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class TaskCategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class TaskCreateForm(forms.ModelForm):
    """
    Task create form
    """

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "category",
            "start_date",
            "end_date",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class TaskCommentCreateForm(forms.ModelForm):
    """
    Task comment create form
    """

    class Meta:
        model = TaskComment
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 3}),
        }


class TaskAssignmentCreateForm(forms.ModelForm):
    """
    Task assignment create form
    """

    class Meta:
        model = TaskAssignment
        fields = ["user"]
