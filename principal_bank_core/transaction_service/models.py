from django.db import models

# Create your models here.
class Transactions(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    source_account_id = models.ForeignKey('account_service.Accounts', on_delete=models.CASCADE, related_name='account_id')
    destination_account_id = models.ForeignKey('account_service.Accounts', on_delete=models.CASCADE, related_name='account_id')
    amount = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
