from django import forms


class TodoForm(forms.Form):
    content = forms.CharField(label='content', widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg border-0 add-todo-input bg-transparent rounded", 'placeholder': "Add new .."}))
    datetime_send = forms.DateTimeInput
