from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
    #python manage.py shell
    # from TechStartup.models import Manufacturer
    # Manufacturer.objects.create(name="Test Manufacturer", location="Test Location", description="Test Description", spec="Test Spec", website="http://example.com")

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    spec = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.name

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.name 