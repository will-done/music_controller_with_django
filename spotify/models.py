from django.db import models
from api.models import Room 

class SpotifyToken(models.Model): 
    user = models.CharField(max_length=50, unique=True)
    access_token = models.CharField(max_length=150)
    token_type = models.CharField(max_length=50)
    refresh_token = models.CharField(max_length=150, null=True, blank=True)
    expires_in = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    
class Vote(models.Model):
    user = models.CharField(max_length=50, unique=True )
    created_at = models.DateTimeField(auto_now_add=True) 
    song_id = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE )

    