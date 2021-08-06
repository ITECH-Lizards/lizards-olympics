from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'sex', 'personID', 'email', 'birth', 'edu', 'school',
                  'major', 'experience', 'position', 'photo')

        edu_list = (
            ('Junior College','Junior College'),
            ('Undergraduate','Undergraduate'),
            ('Master','Master'),
            ('Doctor','Doctor'),
            ('Others','others'),
        )
        widgets = {

            'edu': forms.Select(choices=edu_list),
            'photo': forms.FileInput(),
        }