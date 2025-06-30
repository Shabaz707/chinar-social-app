# F:\chinar\core\models.py

from django.db import models
from django.contrib.auth.models import User # Ensure this line is exactly as shown

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    caption = models.TextField(blank=True)
    image_url = models.URLField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0) # This field will now be updated by the Like model logic

    def __str__(self):
        return f"Post by {self.user.username} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-timestamp']

class Like(models.Model):
    # Links a user to a post. One user can like one post.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    # IMPORTANT CHANGE: Added related_name='liked_by'
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_by')
    timestamp = models.DateTimeField(auto_now_add=True) # When the like occurred

    class Meta:
        # Ensures that a user can only like a specific post once
        unique_together = ('user', 'post')

    # Ensure this method is properly indented within the Like class
    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"
