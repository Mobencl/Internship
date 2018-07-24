from django.db import models
from Authorize.models import Partners


# Create your models here.

class Sportcenters(models.Model):
    Name = models.CharField(max_length  = 255)
    Address = models.CharField(max_length  = 255)
    City = models.CharField(max_length  = 255)
    Country = models.CharField(max_length  = 255)
    TelephoneNumber = models.CharField(max_length=12)
    ImagePath = models.CharField(max_length  = 255)
    Description = models.TextField(max_length  = 140)
    Partner = models.ForeignKey(Partners,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Sportcenters'



class Photo(models.Model):# I created this class so I can upload Photos for each sportcenter but there is a problem with the path or media files or the settings.

    path = models.FileField()
    sportcenter = models.ForeignKey(Sportcenters)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Photo'

    def __str__(self):
         return self.sportcenter.Name

class Terrain(models.Model):
    sportcenter = models.ForeignKey(Sportcenters,on_delete=models.CASCADE)
    TerrainType = models.CharField(max_length  = 255)
    minimumCapacity = models.IntegerField(default = 0)
    maximumCapacity = models.IntegerField(default = 0)
    Price= models.IntegerField(default = 0)
    opening = models.DateTimeField(blank=True, null=True)
    closing = models.DateTimeField(blank=True, null=True)
    #time_period = PositiveIntegerField(default =35040 )
    #availableFrom =DateTimeField()
    #availableTo =DateTimeField()
    #status = PositiveIntegerField(default=1)#available
    class Meta:
        verbose_name_plural = 'Terrain'

    def __str__(self):
         return self.TerrainType
