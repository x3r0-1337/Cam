import socket
import cv2
import multiprocessing
import pickle
import time
#This part of the code is used to connect to the server side and send the arra in string format using UTF-8 encoding
def send_video_as_string(sock,frame):
    video_string=pickle.dumps(frame)
    sock.send(video_string.encode('utf-8'))
def main():
    start=time.time()
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c=sock.connect((ip_address,port))
    #This is the opencv ojject instantization 
    video=cv2.VideoCapture(0)
    check,frame=video.read()#Here frame is a 2D numpy array
    p=multiprocessing.Process(send_video_as_string,(c,frame)) 
    while True:
        check,frame=video.read()

        cv2.imshow("capturing",frame)   #This line is just to show the video
        if start-time.time()>1:         #The image file is send after ever 5 seconds
            p.start()
            start=time.time()           #To start the time measuring process all over again
        key=cv2.waitKey(1)
        if key==ord('q'):
            break   
    video.release()
    cv2.destroyAllWindows
    print(video_string)


