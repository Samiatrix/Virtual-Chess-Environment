from django.shortcuts import render
from django.views import View 

from .models import *
from .forms import *

class IndexView(View):
    template_name = "chess/index.html"

    def get(self,request):
        form = PlayDetailForm()
        return render(request,self.template_name,{"form":form})

    def post(self,request):
        if request.method == "POST":
            form = PlayDetailForm(request.POST)
            if form.is_valid():
                print(form)
                form.save()     
                return self.get(request)  
        else:
            form = PlayDetailForm()         
        context = {
            "form":form
            }
        return render(request,self.template_name,context)


class GamePlay(View):
    template_name = "chess/play.html"
    def get(self,request):

        return render(request,self.template_name,{})

