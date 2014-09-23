from django.shortcuts import render
from django.template import Context, loader 
from django.http import HttpResponse 
from django.shortcuts import render_to_response
from tabapp.models import Variables

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required   
 
#def var_list(request): 
  #var_list = Variables.objects.all() 
  #t = loader.get_template('notes/list.html') 
  #c = Context({ 'note_list': note_list, }) 
  #return HttpResponse(t.render(c)) 
  
def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('thetab/templates/index.html', context_dict, context) # context_dict, context)
  