from django.db import models
from dedupebackend.fields import UniqueFileField, UniqueImageField


class HenkenDorp(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    image = models.ImageField()

    # uniquefile = UniqueImageField(null=True)
    # uniqueimage = UniqueImageField(null=True)

    def __unicode__(self):
        return self.name