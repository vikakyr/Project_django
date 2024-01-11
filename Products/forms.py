from django import forms
from django.db import models


class CombinedForm(forms.Form):
    # start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'onchange': 'setEndDate()'}))
    # end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    options = forms.MultipleChoiceField(
        choices=[('Skis', 'Skis'), ('Poles', 'Poles'), ('Boots', 'Boots'), ('Helmet', 'Helmet')],
        widget=forms.CheckboxSelectMultiple
    )
    options_level = forms.ChoiceField(
        choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')],
        widget=forms.RadioSelect  
    )



from django.db import models

class ProductDetailsForm(forms.Form):
    product = models.OneToOneField('Products', on_delete=models.CASCADE, related_name='details')
    size_choices_boots = forms.ChoiceField(choices=[
        ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42')], widget=forms.RadioSelect)
    size_choices_helmet = forms.ChoiceField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L')], widget=forms.RadioSelect)
    length_choices_skis = forms.ChoiceField(choices=[ ('120', '120'), ('130', '130'), ('140', '140'), ('150', '150'), ('160', '160')], widget=forms.RadioSelect)    
    length_choices_poles = forms.ChoiceField(choices=[('100', '100'), ('110', '110'), ('120', '120'), ('130', '130'), ('140', '140'), ('150', '150')], widget=forms.RadioSelect)


from django import forms
from .models import ReservedProduct

# forms.py
from django import forms
from .models import ReservedProduct

class ReservedProductForm(forms.ModelForm):
    class Meta:
        model = ReservedProduct
        fields = ['user', 'product', 'selected_size', 'date']



