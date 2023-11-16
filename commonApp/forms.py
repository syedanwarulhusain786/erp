# forms.py
from django import forms
from .models import Material, Product, ProductMaterial,ProductMaterialImage,ProductImage

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = '__all__'

class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = '__all__'

class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = '__all__'
        
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'
class ProductMaterialImageForm(forms.ModelForm):
    class Meta:
        model = ProductMaterialImage
        fields = '__all__'