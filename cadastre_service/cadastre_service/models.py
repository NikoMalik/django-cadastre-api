from sqlite3 import Timestamp
from django.db import models 



class QueryHistory(models.Model):
    cadastre_number = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    external_server_response = models.BooleanField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
      return f'{self.cadastre_number} - {self.timestamp}'
    
      