from django.http import HttpResponse
from django.template import loader

def run(request):
    users = {'name': 'kenneth', 'likes': 9}
    
    template = loader.get_template('tutorial_app/index.html')
    return HttpResponse(template.render(users,request))