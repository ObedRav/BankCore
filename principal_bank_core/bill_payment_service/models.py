from django.db import models

# Create your models here.
class Bills(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('user_service.Users', on_delete=models.CASCADE)
    service_provider = models.ForeignKey('service_provider_service.ServiceProviders', on_delete=models.CASCADE) # Keep in mind
    amount = models.IntegerField()
    dueDate = models.DateTimeField()
    
class Payments(models.Model): # Keep in mind
    payment_id = models.IntegerField(primary_key=True)
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
