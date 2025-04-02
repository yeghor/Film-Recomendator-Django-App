from django import forms

choices = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5 "),
]
class QueryForm(forms.Form):
    genre = forms.CharField(max_length=100, label="Prefered Genre", required=False)
    query_text = forms.CharField(max_length=250, label="Preferences")
    n_results = forms.ChoiceField(choices=choices, label="Number of results")

    