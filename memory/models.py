from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default="")
    create_time = models.DateTimeField(auto_now_add=True)
    # time_1=models.DateTimeField(null=True)
    # time_2=models.DateTimeField(null=True)
    # time_3=models.DateTimeField(null=True)
    # time_4=models.DateTimeField(null=True)
    # time_5=models.DateTimeField(null=True)
    # time_6=models.DateTimeField(null=True)
    # time_7=models.DateTimeField(null=True)
    # time_8=models.DateTimeField(null=True)
    current_step = models.IntegerField(default=0)

