import numpy as np 
import cv2
# from PIL import Image
import base64




class GameController:
    def __init__(self, **kwargs):
        self.player1 = kwargs["player1"]
        self.player2 = kwargs["player2"]
        self.time = 0
        self.isChanged = True

    def boardChange(self):
        return self.isChanged
    
    def getGameData(self):
        img = cv2.imread("chess/simple_img.png")
        # img = np.resize(img,(720,1280 ))
        img = cv2.imencode('.jpg', img)[1].tobytes()
        img_base64_enc = base64.b64encode(img)

        img_base64_enc = img_base64_enc.decode('utf-8')
        ret = {
            "image" : img_base64_enc,
            "winner" :"ongoing"  ## "player1" "player2" "draw" "ongoing"
        }
        return ret
    
