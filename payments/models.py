from django.db import models
from core.models import SafariPackage

class Transaction(models.Model):
    safari = models.ForeignKey(SafariPackage, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    amount_usd = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)
    amount_kes = models.DecimalField(max_digits=10, decimal_places=2)
    mpesa_request_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default="PENDING") # PENDING, SUCCESS, FAILED
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.safari.title} ({self.status})"