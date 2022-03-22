from django import forms

class BandaFormulario(forms.Form):
    banda = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=30)


class MusicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    instrumento = forms.IntegerField()
    
    
class RecitalesFormulario(forms.Form):
    ciudad = forms.IntegerField()    


class BusquedaBanda(forms.Form):
    partial_banda = forms.CharField(label="buscador", max_length=20)