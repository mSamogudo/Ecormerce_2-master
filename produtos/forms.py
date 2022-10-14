from django import forms


class AddParaCarinhoForm(forms.Form):
    quantidade = forms.IntegerField()
