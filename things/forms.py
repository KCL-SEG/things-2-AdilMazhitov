"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    name = forms.CharField(label = 'Name', max_length = 30)
    class Meta:
        model = Thing
        fields =['description','quantity']
        widgets = {'description': forms.Textarea(),
                    'quantity': forms.NumberInput(
                        attrs= {
                            'max':'50',
                            'min':'0',
                        }),
                }