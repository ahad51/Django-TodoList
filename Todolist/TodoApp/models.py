from django.db import models

class Mytodo(models.Model):
    task= models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.task