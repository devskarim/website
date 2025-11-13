from django import forms

class BookForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Kitob nomi", "required": "required"})
    )
    author = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Muallif", "required": "required"})
    )
    desc = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Kitob tavsifi", "rows": 5, "required": "required"})
    )
    price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={"placeholder": "Narxi"})
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and not title.istitle():
            raise forms.ValidationError("Kitob nomi bosh harf bilan boshlanishi kerak.")
        return cleaned_data
