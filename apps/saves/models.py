from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE


class Save(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=CASCADE, related_name="saves")
    title = models.CharField(max_length=1000)
    info = models.TextField()
    save_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}, {self.title}"
