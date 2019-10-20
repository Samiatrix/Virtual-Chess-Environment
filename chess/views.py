from django.shortcuts import render
from django.views import View 
import base64
from .models import *
from .forms import *
from .gameController import GameController

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

        game = GameController(player1='ashsih',player2='ashwin')
        if game.boardChange():
            context = {"sample" : game.getGameData()}
        
            # print(context)
        return render(request,self.template_name,context)

