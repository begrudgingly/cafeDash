from django.urls import path
from . import views
from .views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("ratingRecord/", views.obtainCustomerRating, name="ratingRecord"),
    
    path("homepage/", views.homepage, name="homepage"),
    
    path("expensesItem/", views.obtainExpenses.as_view(template_name="main/expensesItem.html"), name="expensesItem"),
    path("itemSalesMenu/", views.obtainMenuItemSales.as_view(template_name="main/itemSalesMenu.html"), name="itemSalesMenu"),
    path("branchSalesMenu/", views.obtainDailyBranch.as_view(template_name="main/branchSalesMenu.html"), name="branchSalesMenu"),
]
