from django.db import models
from .user_model import User

class Todo(models.Model):
    text = models.TextField()
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "User: {} Text: {} {}"\
               .format(self.user, self.text, 'Done' if self.is_done else "Not Done")