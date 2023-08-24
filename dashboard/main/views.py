from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import *
from django.views.generic import *

def homepage(request):
	menu_item = {"Iced Coffee", "Croissant", "Lemon Cheesecake"}

	context = {'menus': menu_item}
	return render(request, 'main/home.html', context)

def obtainCustomerRating(request):
    return render(request, 'main/ratingRecord.html')

class obtainExpenses(ListView):
	model = ExpensesRecord

	def expensesItem(self, **kwargs):
		context = super().get_context_data(**kwargs)

		return context

	def get_context_data(self, **kwargs):
		context = super(obtainExpenses, self).get_context_data(**kwargs)

		expenses_items = ExpensesRecord.objects.order_by('-dateRecorded')

		#calculate total expenses by multiplying total expenses and quantity expenses, assign them to value 'totalexptype'
		calcExpenses = ExpensesRecord.objects.values('expensesType').annotate(totalExpType=Sum(F('totalExpenses')*F('quantityExpenses'), output_field=FloatField()))

		labelExpenses = []
		dataExpenses = []

		#push values of total expenses/expenses type into chart's data and label axes
		dataExpenses = list(calcExpenses.values_list('totalExpType', flat=True))
		labelExpenses = list(calcExpenses.values_list('expensesType', flat=True))

		context.update({'labelExpenses': labelExpenses, 'dataExpenses': dataExpenses, 'calcExpenses': calcExpenses})
		return context

class obtainMenuItemSales(ListView):
	model = MenuItemSalesRecord

	def obtainDailySales(self, **kwargs):
		context = super().get_context_data(**kwargs)

		return context

	def get_context_data(self, **kwargs):
		context = super(obtainMenuItemSales, self).get_context_data(**kwargs)

		#accumulate total quantity sold of distinct menu item, assign them to value 'totalSold'
		agg_MenuItem = MenuItemSalesRecord.objects.values('menuItem').annotate(totalSold=Sum('quantitySold')).order_by('-totalSold')[:5]

		#show the most popular menu item; the first on the list
		mostPopular = MenuItemSalesRecord.objects.values('menuItem').annotate(totalSold=Sum('quantitySold')).order_by('-totalSold')[:1]

		#push values of quantity sold/menu item into chart's data and label axes
		dataTotalSales = list(agg_MenuItem.values_list('totalSold', flat=True))
		labelTotalSales = list(agg_MenuItem.values_list('menuItem', flat=True))

		context.update({'agg_MenuItem': agg_MenuItem, 'labelTotalSales': labelTotalSales, 'dataTotalSales': dataTotalSales, 'mostPopular': mostPopular})
		return context

class obtainDailyBranch(ListView):
	model = SalesRecord

	def obtainDailySales(self, **kwargs):
		context = super().get_context_data(**kwargs)

		return context

	def get_context_data(self, **kwargs):
		context = super(obtainDailyBranch, self).get_context_data(**kwargs)

		dataSelangor = []
		labelSelangor = []

		list_DailySelangor = SalesRecord.objects.filter(branchOfOrigin="Selangor")
		for sales in list_DailySelangor:
			dataSelangor.append(sales.totalSales)
			labelSelangor.append(sales.dateOfSales)

		dataJohor = []
		labelJohor = []

		list_DailyJohor = SalesRecord.objects.filter(branchOfOrigin="Johor")
		for sales in list_DailyJohor:
			dataJohor.append(sales.totalSales)
			labelJohor.append(sales.dateOfSales)

		dataPerak = []
		labelPerak = []

		list_DailyPerak = SalesRecord.objects.filter(branchOfOrigin="Perak")
		for sales in list_DailyPerak:
			dataPerak.append(sales.totalSales)
			labelPerak.append(sales.dateOfSales)

		agg_DailyBranch = SalesRecord.objects.values('branchOfOrigin').annotate(totalBranchSales=Sum('totalSales')).order_by('branchOfOrigin')

		agg_MonthlySelangor = SalesRecord.objects.values('branchOfOrigin').filter(branchOfOrigin="Selangor").annotate(totalSelangor = Sum('totalSales'))
		agg_MonthlyJohor = SalesRecord.objects.values('branchOfOrigin').filter(branchOfOrigin="Johor").annotate(totalJohor = Sum('totalSales'))
		agg_MonthlyPerak = SalesRecord.objects.values('branchOfOrigin').filter(branchOfOrigin="Perak").annotate(totalPerak = Sum('totalSales'))

		dataMonthlySales = list(agg_DailyBranch.values_list('totalBranchSales', flat=True))
		labelMonthlySales = list(agg_DailyBranch.values_list('branchOfOrigin', flat=True))

		context.update({'agg_DailyBranch': agg_DailyBranch, 'labels': labelMonthlySales, 'data': dataMonthlySales, 'list_DailySelangor': list_DailySelangor, 'dataSelangor': dataSelangor, 'labelSelangor': labelSelangor, 'dataJohor': dataJohor, 'labelJohor': labelJohor, 'dataPerak': dataPerak, 'labelPerak': labelPerak, 'agg_MonthlySelangor': agg_MonthlySelangor, 'agg_MonthlyJohor': agg_MonthlyJohor, 'agg_MonthlyPerak': agg_MonthlyPerak})
		return context
