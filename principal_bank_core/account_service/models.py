from django.db import models

# Create your models here.
class AccountTypes(models.Model):
    account_type_id = models.IntegerField(primary_key=True)
    account_type_name = models.CharField(max_length=100)

class Accounts(models.Model):
    account_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('user_service.Users', on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountTypes, on_delete=models.CASCADE)
    balance = models.IntegerField()
