from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60,verbose_name='Title')
    images = models.ImageField(upload_to='images/',verbose_name="image",null=True, blank=True)
    description = models.CharField(null = True,verbose_name='Description',max_length=100)

    def __str__(self):
        fila  = "title"+self.title + " - " + "description" + self.description
        return fila

    def delete(self, using=None, keep_parebrs = False):
        self.images.delete(self.images.name)
        super().delete()