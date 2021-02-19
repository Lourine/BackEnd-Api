from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number=models.CharField(max_length=15, blank=True)
    ##email=models.CharField
   ## password_hash=models.CharField
    def __str__(self):
        return self.first_name
  
class Order(models.Model):
    item = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='orders',on_delete=models.CASCADE)
    class Meta:
        unique_together = ['customer', 'time']
        ordering = ['time']

    def __str__(self):
        return self.item