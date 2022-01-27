from django import forms
from order.models import Item, Attachment

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('order',)
        widgets = {
             'width': forms.TextInput(attrs={'style': 'width: 45px'}),
             'lenght': forms.TextInput(attrs={'style': 'width: 45px'}),
             'quantity': forms.TextInput(attrs={'style': 'width: 20px'}),
             'description': forms.Textarea(attrs={'style': 'width: 60px',
                                                  'rows': 2,
                                                  'cols': 2,}),}
        labels = {'description': 'Opis',}

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        exclude = ('order',)