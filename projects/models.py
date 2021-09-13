from django.db import models
import uuid

# Create your models here.


class Project(models.Model):
    # Owner =
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # Featured_image =
    demo_link = models.CharField(max_length=1000)
    source_link = models.CharField(max_length=1000)
    vote_total = models.IntegerField(default=0)
    vote_radio = models.IntegerField(default=0)
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
