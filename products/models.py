from django.db import models

Category_Choice = (('P','painting'),('S','statuary'),('H','Handicrafts'),('M','Minatory'))
class Product (models.Model):
    title = models.CharField(max_length=100)
    selling_pice = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=Category_Choice,max_length=4)
    product_image = models.ImageField(upload_to='productimg')
    created_time = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return str(self.id)
