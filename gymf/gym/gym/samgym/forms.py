from django import forms
from .models import Membership,AI_bot

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['name', 'email', 'phone', 'plan', 'date_created']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Membership.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email




class AIBotForm(forms.ModelForm):
    class Meta:
        model = AI_bot
        fields = ['username', 'question']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }),
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ask a question...',
                'rows': 4
            })
            
        }
