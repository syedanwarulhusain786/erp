# forms.py
from django import forms
from .models import Material

from .models import Product

class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
        

from django import forms
from commonApp.models import Service, ServiceCategory,ProductBrand,ProductCategory

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['name']
        labels = {'name': 'Category Name'}

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'category', 'price','Qty','costing']
        labels = {
            'name': 'Service Name',
            'description': 'Description',
            'category': 'Category',
            'price': 'Price',
            'Qty': 'Qty',
            'costing': 'Costing',
        }
        
class ProductBrandForm(forms.ModelForm):
    class Meta:
        model = ProductBrand
        fields = ['name', 'description']
        labels = {
            'name': 'ProductBrand Name',
            'description': 'Description',
            
        }
        
        
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
        labels = {
            'name': 'ProductCategory Name',
            'description': 'Description',
           
        }
        
        
        
        
        
# forms.py

from django import forms
from .models import ProductMaterial, Material

class ProductMaterialForm(forms.ModelForm):
    # materials = forms.ModelMultipleChoiceField(
    #     queryset=Material.objects.all(),
    #     widget=forms.SelectMultiple(attrs={'class': 'form-control select2', 'data-placeholder': 'Select materials'}),
    #     required=False,
    # )

    class Meta:
        model = ProductMaterial
        fields = ['product','quantity_per_piece', 'material']
# forms.py
class ProductMaterialEditForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = ['product', 'quantity_per_piece', 'material']