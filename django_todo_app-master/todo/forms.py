from django import forms 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=999, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'meubel', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'autofocus': 'autofocus'}))

    #price = forms.IntegerField(widget=forms.TextInput(
     #       attrs={'class' : 'form-control', 'placeholder' : 'meubel', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

    price = forms.FloatField(initial='price',widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.01", 'autofocus': 'autofocus'}))
    
    url = forms.URLField(initial='http://')