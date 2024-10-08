from django import forms
from .models import Blog, Cliente, Comentario, Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'description', 'price','image']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description', 'date','body','image']
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class BuscarProductoForm(forms.Form):
    producto = forms.CharField()

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comment']