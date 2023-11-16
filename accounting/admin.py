from django.contrib import admin
from .models import Ledger

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ('ledger_name', 'ledger_type', 'opening_balance', 'current_balance')
    search_fields = ('ledger_name', 'ledger_type')

# If you want to create a custom form for the Ledger model
# Uncomment the following section:

# from django import forms
# 
# class LedgerForm(forms.ModelForm):
#     class Meta:
#         model = Ledger
#         fields = '__all__'
# 
# class LedgerAdmin(admin.ModelAdmin):
#     form = LedgerForm
#     list_display = ('ledger_name', 'ledger_type', 'opening_balance', 'current_balance')
#     search_fields = ('ledger_name', 'ledger_type')
# 
# admin.site.register(Ledger, LedgerAdmin)

