# django
from django.db import models
from django.utils.text import slugify

# imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import Transpose


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(editable=False)
    image = models.FileField(upload_to="images/categories", blank=True, null=True)
    thumbnail_image = ImageSpecField(
        source= 'image',
        processors= [Transpose(),],
        format= 'JPEG',
        options= {'quality': 30}
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    subcategory = models.ForeignKey(SubCategory, related_name="tags", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Seller(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name="products", on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey(Tag, related_name="products", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    amount = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(Seller, related_name="seller", on_delete=models.CASCADE)
    image = models.FileField(upload_to="images/products")
    thumbnail_image = ImageSpecField(
        source= 'image',
        processors= [Transpose(),],
        format= 'JPEG',
        options= {'quality': 30}
    )

    def credit_payment(self):
        yearly_percentage = 44
        per_month = (self.price * (1 + yearly_percentage/100)) / 12
        return per_month 

    def __str__(self):
        return self.title 

class Size(models.Model):
    product = models.ForeignKey(Product, related_name="sizes", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"size for {self.product.title}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.FileField(upload_to="images/products")
    thumbnail_image = ImageSpecField(
        source= 'image',
        processors= [Transpose(),],
        format= 'JPEG',
        options= {'quality': 30}
    )
    
    def __str__(self):
        return f"image for {self.product.title}"
    
# class Liked(models.Model):
#     user = models.ForeignKey(User, related_name="likes_list", on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name="likes", on_delete=models.CASCADE)
#     liked_date = models.DateTimeField(auto_now_add=True)
    
class BannerImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="images/banner-images")
    thumbnail_image = ImageSpecField(
        source= 'image',
        processors= [Transpose(),],
        format= 'JPEG',
        options= {'quality': 30}
    )

    def __str__(self):
        return self.title




















