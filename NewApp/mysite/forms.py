from django import forms
from .models import TestImage,User,Karuta_data,Final_Test,Words

class TestForm(forms.Form):

    image0 = forms.CharField(max_length=15000,required=False)
    image1 = forms.CharField(max_length=15000,required=False)
    image2 = forms.CharField(max_length=15000,required=False)
    image3 = forms.CharField(max_length=15000,required=False)
    image4 = forms.CharField(max_length=15000,required=False)
    image5 = forms.CharField(max_length=15000,required=False)
    image6 = forms.CharField(max_length=15000,required=False)
    image7 = forms.CharField(max_length=15000,required=False)
    image8 = forms.CharField(max_length=15000,required=False)
    image9 = forms.CharField(max_length=15000,required=False)
    image10 = forms.CharField(max_length=15000,required=False)
    image11 = forms.CharField(max_length=15000,required=False)
    image12 = forms.CharField(max_length=15000,required=False)
    image13 = forms.CharField(max_length=15000,required=False)
    image14 = forms.CharField(max_length=15000,required=False)

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('user_name','user_age','user_sex',)

class KarutaForm(forms.ModelForm):
    class Meta():
        model = Karuta_data
        fields = ('mistake_count','finished_time',)

class FinalTestForm(forms.Form):

         words0 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=1).words,max_length=100,required=False)
         words1 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=2).words,max_length=100,required=False)
         words2 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=3).words,max_length=100,required=False)
         words3 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=4).words,max_length=100,required=False)
         words4 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=5).words,max_length=100,required=False)
         words5 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=6).words,max_length=100,required=False)
         words6 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=7).words,max_length=100,required=False)
         words7 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=8).words,max_length=100,required=False)
         words8 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=9).words,max_length=100,required=False)
         words9 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=10).words,max_length=100,required=False)
         words10 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=11).words,max_length=100,required=False)
         words11 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=12).words,max_length=100,required=False)
         words12 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=13).words,max_length=100,required=False)
         words13 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=14).words,max_length=100,required=False)
         words14 = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':15}),label=Words.objects.get(pk=15).words,max_length=100,required=False)
