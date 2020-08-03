from django.shortcuts import render


def ecommerce_report_page(request):
   return render(request, 'dashboard/retail_report.html', {})


def marketing_report_page(request):
   return render(request, 'dashboard/marketing_report.html', {})

def task(request):
   return render(request, 'dashboard/task_report.html', {})