import numpy as np
import math
import cv2
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
def ration_factor(height,point1,point2):
    virtaul_height=math.sqrt(((point1[0] - point2[0]) ** 2) + (point1[1] - point2[1]) ** 2)
    x=height/virtaul_height
    ratio=float("{0:.4f}".format(x))
    return ratio

def find_distance(point1,point2):
    distance = math.sqrt(((point1[0] - point2[0]) ** 2) + (point1[1] - point2[1]) ** 2)
    return distance


def suit_lenght(ratio,point1,point2,factor):
    distance=math.sqrt(((point1[0] - point2[0]) ** 2) + (point1[1] - point2[1]) ** 2)
    x=distance*ratio
    y=x+factor
    return y
def chest(ratio,point1,point2,factor):
    distance = math.sqrt(((point1[0] - point2[0]) ** 2) + (point1[1] - point2[1]) ** 2)
    x=distance*ratio
    y=x*2
    return y+factor

def full_body_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    print(bodies)
    (x,y,w,h)=bodies[0]
    for (x, y, w, h) in bodies:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
    img= image[y:y+h, x:x+w]

def edge_detection(image):
    w = 368
    h = 716
    dim = (w, h)
    frame = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flter = cv2.bilateralFilter(gray, 11, 15, 15)
    edge = cv2.Canny(flter, 170, 200)
    contor, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print('lenfht of contors')
    print(len(contor))
    contours=[]
    for c in contor:
        a=c[0][0]
        a=tuple(a)
        contours.append(a)
    return contours,contor,edge

def find_radius(point1,point2,ratio):
    r=math.sqrt(((point1[0] - point2[0]) ** 2) + (point1[1] - point2[1]) ** 2)
    r=r*ratio
    circum_ference=3.14*r
    circum_ference=circum_ference/2
    return circum_ference

def check_y_coordinate(ctn,center):
    y = center[1]
    points=[]
    for i in range(10):
        a=center[1]-(5*i)
        b=center[1]+(5*i)
        for item in ctn:
            if item[1]>a and item[1]<b and item[0]>center[0]:
                points.append(item)
        if len(points)>0:
            break
    sum=0
    x_cordinate=[]
    for item in points:
        x_cordinate.append(item[0])
    x_cordinate.sort()
    sides=(x_cordinate[0],y)
    return sides,True

def find_mid_point(point1,point2):
    p=(int((point1[0]+point2[0])/2),int((point1[1]+point2[1])/2))
    return p






