from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    image = models.CharField(max_length=500, default='🥚')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
