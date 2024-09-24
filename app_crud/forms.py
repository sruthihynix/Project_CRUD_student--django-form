from django import forms
from .models import User

class StudentRegForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','pwd']
        # widgets add to modify fields/ customerize fields
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}), # form-control is style from bootstrap
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pwd': forms.PasswordInput(render_value=True ,attrs={'class': 'form-control'}), # rendervalue true ayit kodthal mathrame pwd updste cheyyan varikyolu
        }