from django.shortcuts import render,redirect
from django.views import View 
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import APIView

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
                form.save()     
                return redirect("play")
        else:
            form = PlayDetailForm()         
        context = {
            "form":form
            }
        return render(request,self.template_name,context)


class GamePlay(View):
    template_name = "chess/play.html"
    def get(self,request):

        fil = open("testfile.txt","r")
        st = fil.read()
        print(st)
        fil.close()
        game = GameController(player1='ashsih',player2='ashwin')
        if game.boardChange():
            context = {"sample" : game.getGameData(),"sam":st}
        
            # print(context)
        return render(request,self.template_name,context)


class Endgame(APIView):
    
    # def get(self,request):
    #     list = [1,]
    #     for i in range(1,10):
    #         print(i)
    #         list.append(i)
    #         context = {
    #             'list':list
    #         }
    #         return render(request,"chess/endgame.html",context)

    def get(self,request):
        fil = open("testfile.txt","r")
        st = fil.read()
        print(st)
        fil.close()
        return Response({"cont":st})