from django.db import models

# Create your models here.
class Plant(models.Model): 
    
    class Category(models.TextChoices):
        TREE = "Tree", "Tree"          
        FRUIT = "Fruit", "Fruit"       
        VEGETABLE = "Vegetable", "Vegetable" 
        FLOWER = "Flower", "Flower"   

    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    
    category = models.CharField(
        max_length=50, 
        choices=Category.choices, 
        default=Category.TREE
    )
    
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model): 
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)