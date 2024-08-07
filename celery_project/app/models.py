from django.db import models

# Create your models here.

class Huddle(models.Model):
    key = models.CharField(max_length=40)


class item(models.Model):
    huddle = models.ForeignKey(Huddle,related_name='items',on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['created_at']