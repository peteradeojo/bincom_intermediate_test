import psycopg2
from django.db import models

conn = psycopg2.connect(
    database='bincom',
    user='peter',
    password='peterojo32'
)

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
