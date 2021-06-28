from django.db import models
from django.urls import reverse 

# Create your models here.
class Carousal(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class cards(models.Model):
    c_img = models.ImageField(upload_to = 'cardimg')    
    c_title = models.CharField(max_length=150)
    c_text = models.CharField(max_length=150)
    c_body = models.TextField(blank=True)
    publish = models.DateField(auto_now_add=True)
    trending = models.BooleanField(default = False)

    class Meta:
        ordering=('-c_title',)

    def __str__(self):
        return self.c_title
        
    def get_absolute_url(self):
        return reverse("readmore", kwargs={
            "id": self.id
            })
        
