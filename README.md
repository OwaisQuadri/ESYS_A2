# ESYS_A2
Embedded Systems Assignment 2 Code  
  
Python Obstacle detection program using OpenCV and TensorFlow. Accepts input in the form of a video file. Used for Assignment 2 to measure the differences in performance for each different architecture emulated in QEMU.  
  
How to Install and Run:  
1. clone project
```
git clone https://github.com/OwaisQuadri/ESYS_A2
cd ESYS_A2
```
2. ensure python, pip and dependencies are installed
```
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip
pip install opencv-python 
```
3. Run program by ensuring that there is an "input.mp4" file and run:
```
python3 obstacleDetect.py
```
