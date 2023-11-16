from django.db import models

class Ledger(models.Model):
    ledger_name = models.CharField(max_length=255, unique=True)
    ledger_type = models.CharField(max_length=50)  # You might want to use choices for predefined types
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    ledger_limit = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    ledger_limitLeft = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    

    def __str__(self):
        return self.ledger_name
