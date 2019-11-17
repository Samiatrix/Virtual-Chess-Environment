from django.shortcuts import render,redirect
from django.views import View 
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import APIView
import json 
import base64
from .models import *
from .forms import *
import os
import sys
sys.path.append("../")
from virtualchess.chessBackend.parse_game import Parse_Game

# from chess-backend.parse_game import Parse_Game



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
                # fie = open("chess_engine/start_engine.txt", "w")
                # fie.write("yes")
                # fie.close()
                
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

        # fil = open("chess_engine/engine.txt","r")
        # st = fil.read()
        # print(st)
        # fil.close()
        # game = GameController(player1='ashsih',player2='ashwin')
        

        # Creating New thread for the chess-backend
        



        context = {"sam":"ABC"}
        
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
        fil = open("chess-backend/engine.txt","r")
        d = json.load(fil)
        sv = d[0]["boardSVG"]
        
        print("Refreshed")

        print(sys.path)
        print(os.system("pwd"))
        

        # print(type(d))
        # print(d[0]["boardSVG"])
        fil.close()
        return Response({"cont":d, "svg":sv})