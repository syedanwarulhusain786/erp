import uuid
from django.db import models

def get_image_filename(instance, filename):
    """Generate a unique filename for each uploaded image."""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"product_images/{filename}"



class Material(models.Model):
    
    PIECE = 'Piece'
    LITER = 'Liter'
    METER = 'Meter'
    CMS = 'Centimeter'

    UNIT_CHOICES = [
        (PIECE, 'Piece'),
        (LITER, 'Liter'),
        (METER, 'Meter'),
        (CMS, 'Centimeter'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    unit_of_measurement = models.CharField(max_length=10, choices=UNIT_CHOICES, default=PIECE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    materials = models.ManyToManyField(Material, through='ProductMaterial')
    
    def __str__(self):
        return self.name

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity_per_piece = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.material} for {self.product}"
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename)

    def __str__(self):
        return f"Image for {self.product}"
class ProductMaterialImage(models.Model):
    product_material = models.ForeignKey(ProductMaterial, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename)

    def __str__(self):
        return f"Image for {self.product_material}"