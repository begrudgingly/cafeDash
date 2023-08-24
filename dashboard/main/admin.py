from django.contrib import admin
from .models import SalesRecord
from .models import MenuItemSalesRecord
from .models import ExpensesRecord

admin.site.register(SalesRecord)
admin.site.register(MenuItemSalesRecord)
admin.site.register(ExpensesRecord)