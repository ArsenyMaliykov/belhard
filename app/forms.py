from django.forms import Form, IntegerField, TextInput, ModelForm, Textarea

from .models import Feedback


class Calculator(Form):
    width = IntegerField(min_value=1, widget=TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
            'placeholder': 'Ширина',
            'min': '1'
        }
    ))
    height = IntegerField(min_value=1, widget=TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
            'placeholder': 'Высота',
            'min': '1'
        }
    ))


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone_number', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'type': 'text',
                    'placeholder': 'Enter your name...',
                    'data-sb-validations': 'required'
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'type': 'email',
                    'placeholder': 'info@info.com',
                    'data-sb-validations': 'required,email'
                }
            ),
            'phone_number': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'phone',
                    'type': 'tel',
                    'placeholder': '+375251234567',
                    'data-sb-validations': 'required'
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'type': 'text',
                    'placeholder': 'Enter your message here...',
                    'style': 'height: 10rem',
                    'data-sb-validations': 'required'
                }
            )
        }
