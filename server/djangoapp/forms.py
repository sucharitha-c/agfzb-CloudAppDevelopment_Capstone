from django import forms
from .models import review

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ("name","date_joined","content")
        widgets={
                "name":forms.TextInput(attrs={"class":"col-sm-12"}),
                "date_joined":forms.TextInput(attrs={"class":"col-sm-12"}),
                "content":forms.TextInput(attrs={"class":"col-sm-12"}),
        }