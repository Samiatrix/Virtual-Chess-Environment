import chess
import chess.engine
import time
import cv2
import pandas as pd
import chess.svg as svg
import drawSvg as draw
import sys

anno_file = "./game1.csv"
anno = pd.read_csv(anno_file).iloc[:,:].values

engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

board = chess.Board()
s_time = time.time()

for i, chance in enumerate(anno):
    frame_no = chance[0]
    move = chance[1]
    try:
        board.push_san(move)
        info = engine.analyse(board, chess.engine.Limit(depth=20))
        move = str(move)
        time_of_move = int(time.time() - s_time)
        depth = info["depth"]
        pov_score = info["score"]
        best_counter_move = info["pv"][0].uci()
        print("Time : "+  str(time_of_move) +" Move : "+ str(move) + " Depth : "+ str(depth) + " Best Counter Move : "+ str(best_counter_move)+ " Score : "+str(pov_score))
    except Exception as e:
        print("Game end")
        print(e)

engine.quit()
        
iboard = chess.Board(board.fen())
squares = iboard.attacks(chess.E4)
final_board = str(svg.board(board=iboard, squares=squares))
try:
    sys.exit()
except Exception as e:
    print(e)
# print(type(final_board))
# # print(final_board)
