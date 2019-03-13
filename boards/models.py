from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   # 갱신될 때마다 시간이 새로 찍힘
    
    def __str__(self):
        return f"{self.id}: {self.title}"