from django.db import models

# Create your models here.
# 장고는 pk 만들어줌

class Notice(models.Model):
    title = models.CharField(max_length=500 , null=True)
    content = models.CharField(max_length = 500 , null = True)
    username = models.CharField(max_length=500 , null = True)

    def __str__(self):
        return self.title # key 값 설정