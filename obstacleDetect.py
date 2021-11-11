#start to track time
from timeit import default_timer as time
start_time=time()
#obj detect program begin
import cv2 #opencv
import shutil as ui
columns=ui.get_terminal_size()[0]
#formatting for progress bar
if columns>11:
    graph_config="graph_config.pbtxt"
    graph="frozen_inference_graph.pb"
    model = cv2.dnn_DetectionModel(graph,graph_config)
    #load classes
    classes=[]
    labels_file="labels.txt"
    with open(labels_file,'rt') as lf:
        classes=lf.read().rstrip("\n").split("\n")
    # read video
    video=cv2.VideoCapture("input.mp4")
    frames=int(video.get(cv2.CAP_PROP_FRAME_COUNT))+1
    fps=video.get(cv2.CAP_PROP_FPS)
    if not video.isOpened():
        print("failed once")
        video=cv2.VideoCapture(0)
    if not video.isOpened():
        print("failed again")
        raise IOError("Cannot Open Video")

    #create output file
    fourcc=cv2.VideoWriter_fourcc('m','p','4','v')#*'DIVX'
    out=cv2.VideoWriter('output.mp4',fourcc,fps,(1280,720))
    model.setInputSize(320,320)
    model.setInputScale(1.0/127.5)
    model.setInputMean((127.5,127.5,127.5))
    model.setInputSwapRB(True)


    #font size
    font_size=3
    font=cv2.FONT_HERSHEY_PLAIN
    #init progress bar count
    count=1
    print("[",end="",flush=True)
    try:
        while True: 
            if count>=(frames/(columns-10)):
                print("-",end="",flush=True)
                count=1
            count+=1
            ret,frame=video.read()
            classIndex, confidence,bbox=model.detect(frame,confThreshold=0.55)
            if (len(classIndex)!=0):
                for classI,conf,boxes in zip(classIndex.flatten(),confidence.flatten(),bbox):
                    if (classI<=80):
                        cv2.rectangle(frame,boxes,(255,0,0),2)
                        cv2.putText(frame,classes[classI-1],(boxes[0]+10,boxes[1]+40),font,fontScale=font_size,color=(0,255,0),thickness=3)
            out.write(frame)           
    except:#when detection is exited or if file ends
        print("]\nDone\n")
    #finish tracking time
    time_to_detect=time()-start_time
    #output
    print("Time taken to process input.mp4: ",time_to_detect," s")
    print("Processed video saved in: output.mp4")
    video.release()
    cv2.destroyAllWindows()
else:
    print("please increase the width of the terminal")