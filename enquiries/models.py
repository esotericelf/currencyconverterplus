from django.db import models
from django.contrib.auth.models import User

class Enquiry(models.Model):
    index = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enquiries')
    buying_currency = models.CharField(max_length=3)
    selling_currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    date_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry {self.index}"

    def detailed_str(self):
        return f"{self.index}: {self.buying_currency} to {self.selling_currency} - {self.amount}"