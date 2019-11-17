import cv2
import numpy as np 


vid_add = "./test_game_vid.mp4"
anno_add = "./test_game_vid_anno.txt"
out_vid_add = "./demo.mp4"
out_vid = None

anno_writer = open(anno_add, "a")

cap = cv2.VideoCapture(vid_add)
count =0 
while(True):
	ret, image = cap.read()

	if(ret == False):
		break

	if(out_vid == None):
		[h, w] = image.shape[:2]
		out_vid = cv2.VideoWriter(out_vid_add,cv2.VideoWriter_fourcc(*'mp4v'), 15.0,(w,h))
	
	cv2.putText(image,str(count), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1,(209, 80, 0),3)


	out_vid.write(image)
	count+=1



cap.release()
out_vid.release
print(count)