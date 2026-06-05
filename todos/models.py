from django.db import models

# Database table
class Todo(models.Model):
    title = models.CharField(max_length=200)                # VARCHAR
    description = models.TextField(blank=True)              # TEXT
    completed = models.BooleanField(default=False)          # BOOLEAN
    created_at = models.DateTimeField(auto_now_add=True)    # set on INSERT, not touched again
    updated_at = models.DateTimeField(auto_now=True)        # updated one every save automatically

    def __str__(self):
        return self.title