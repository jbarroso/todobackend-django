import uuid
from django.db import models

class Todos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(db_column='position', default=0)
