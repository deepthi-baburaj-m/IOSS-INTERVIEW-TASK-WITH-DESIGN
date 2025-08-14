from django.db import models

class URL(models.Model):
    original_url = models.URLField()
    shorter_url = models.CharField(max_length=10, unique=True)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'urls'

    def __str__(self):
        return f"{self.shorter_url} -> {self.id}"