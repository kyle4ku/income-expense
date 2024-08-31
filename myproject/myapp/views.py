from django.template import loader
from django.http import HttpResponse

def app(request):
    template = loader.get_template('myapp/child-main.html')
    return HttpResponse(template.render())

def add_expense(request):
    template = loader.get_template('myapp/add/add_expenses.html')
    return HttpResponse(template.render())