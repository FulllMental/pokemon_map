from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Lat = models.FloatField()
    Lon = models.FloatField()
    Appeared_at = models.DateTimeField(null=True, blank=True)
    Disappeared_at = models.DateTimeField(null=True, blank=True)
    Level = models.IntegerField(default=0)
    Health = models.IntegerField(default=0)
    Strength = models.IntegerField(default=0)
    Defence = models.IntegerField(default=0)
    Stamina = models.IntegerField(default=0)
