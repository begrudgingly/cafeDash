from django.db import models
from django.db.models import *
from django.db.models.functions import *

class SalesRecord(models.Model):
    BRANCHES = (('Selangor', 'Selangor'), ('Johor', 'Johor'), ('Perak', 'Perak'))

    totalSales = models.FloatField()
    dateOfSales = models.DateTimeField('date recorded')
    branchOfOrigin = models.CharField(max_length=100, choices=BRANCHES)

    def __str__(self):
        return self.branchOfOrigin

class MenuItemSalesRecord(models.Model):
    MENUITEM = (('Chocolate Cake', 'Chocolate Cake'), ('Lemon Tart', 'Lemon Tart'), ('Banana Bread', 'Banana Bread'), ('Cinnamon Roll', 'Cinnamon Roll'), ('Croissant', 'Croissant'), ('Apple Pie', 'Apple Pie'), ('Iced Tea', 'Ice Tea'), ('Iced Coffee', 'Iced Coffee'), ('Iced Lemonade', 'Iced Lemonade'), ('Milk Tea', 'Milk Tea'))

    dateOfSales = models.DateTimeField('date recorded')
    menuItem = models.CharField(max_length=100, choices=MENUITEM)
    menuItemPrice = models.FloatField()
    quantitySold = models.IntegerField()

    def __str__(self):
        return self.menuItem

class ExpensesRecord(models.Model):
    EXPENSESTYPE = (('Utilities', 'Utilities'), ('Stock Resupply', 'Stock Resupply'), ('Rent', 'Rent'), ('Worker Salary', 'Worker Salary'))

    dateRecorded = models.DateTimeField('date recorded')
    expensesType = models.CharField(max_length=100, choices=EXPENSESTYPE)
    totalExpenses = models.FloatField()
    quantityExpenses = models.IntegerField()

    def __str__(self):
        return self.expensesType
