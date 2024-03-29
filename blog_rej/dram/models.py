from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# users , posts

class Post(models.Model):
    title = models.CharField(max_length = 100 )
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(default ='default.jpg', upload_to ='post_pics' )
    
    
    def __str__(self):
        return self.title
        # post_set, 
    
