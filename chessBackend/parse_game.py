import chess
import chess.engine
import cv2
import time
import pprint
import pandas as pd
import chess.svg as svg
import numpy as np
import json
import os

class Parse_Game:
    def __init__(self,games_dir = "./.Data/" ,game_name = "game1"):
        self.Video = games_dir + game_name + ".mp4"
        self.vid_cap = cv2.VideoCapture(self.Video)

        self.anno = games_dir + game_name + ".csv"

        self.anno = pd.read_csv(self.anno).iloc[:,:].values
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

        self.RealFrame = None
        self.ProcessedData = None
        self.winner = None # final structure {"game_result": "player1 or player 2 or draw by repetition draw by stalement or draw by insufficient material" }

    
    def run(self):


        
        ## Now start the engine
        s_time = time.time()
        fnumber = 0
        move_count = 0

        while (True):
            
            if(self.board.is_game_over()):
                if(self.board.is_stalemate()):
                    self.winner={"game_result": "Stalemate"}

                if(self.board.is_insufficient_material()):
                    self.winner={"game_result": "Insufficient material"}

                if(self.board.is_repetition()):
                    self.winner={"game_result": "Repetition"}

                if(self.board.is_checkmate()):
                    ass_win = 1
                    if(len(self.ProcessedData)%2 == 0):
                        ass_win+=1
                    self.winner={"game_result": " Winner is Player "+ str(ass_win)}


            ret, image = self.vid_cap.read()

            if(ret == False or  move_count>=len(self.anno)):
                break

            self.RealFrame = image.copy()
            fnumber+=1
            
            chance = self.anno[move_count]    
            frame_no = chance[0]
            move = chance[1]

            if(frame_no == fnumber):
                
                move_count+=1

                try:
                    self.board.push_san(move)
                    info = self.engine.analyse(self.board, chess.engine.Limit(depth=20))
                    move = str(move)
                    time_of_move = str(int(time.time() - s_time))
                    depth = str(info["depth"])
                    pov_score = str(info["score"])
                    best_counter_move = str(info["pv"][0].uci())
                    print("Chance ==> " + str(move_count))
                except Exception as e:
                    print(e)
                    print(frame_no)
                    print(self.board)
                    print(move)
                    break

                iboard = chess.Board(self.board.fen())
                squares = iboard.attacks(chess.E4)
                final_board = str(svg.board(board=iboard, squares=squares))
            

                chance_data = {
                    "boardSVG": final_board,
                    "moveNo": str(move_count),
                    "timeOfMove": time_of_move,
                    "move" : move,
                    "depthOfSearch": depth,
                    "Score" : pov_score,
                    "bestCounterMove" : best_counter_move

                }
               
                self.ProcessedData = chance_data.copy()
                
        self.engine.quit()
        # out.close()
        # os.system("rm engine.txt")


def main():
    ojj = Parse_Game()
    ojj.run()
 
if __name__ == "__main__":
    main()
