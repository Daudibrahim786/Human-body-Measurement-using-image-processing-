import cv2
import mediapipe as mp
import time
from measure_calcuation import chest,suit_lenght,ration_factor,edge_detection,find_radius,check_y_coordinate,find_mid_point,find_distance
def centroid(point1,point2,point3,point4):
    x,y=(int((point1[0]+point2[0])/2),int((point1[1]+point2[1])/2))
    x1,y1=(int((point3[0]+point4[0])/2),int((point3[1]+point4[1])/2))
    a,b=int((x+x1)/2),int((y+y1)/2)
    return a,b


mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
img=cv2.imread('devil2.jpeg')
height=163
sizes=img.shape
# w=368
if sizes[1]>1500:
    w=230
    h=620
else:
    w=330
    h=716
dim=(w,h)
frame = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
# frame=img
imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
results = pose.process(imgRGB)
points=[]
for id, lm in enumerate(results.pose_landmarks.landmark):
    h, w, c = frame.shape
    # print(id, lm)
    cx, cy = int(lm.x * w), int(lm.y * h)
    points.append([cx, cy])
print(points)
print(points[12],points[11],points[24],points[23])
(a,b)=centroid(points[12],points[11],points[24],points[23])
print('center of upper body',(a,b))
# cv2.circle(img=frame, center = (a,b), radius =6, color =(255,0,0), thickness=6)
if results.pose_landmarks:
    mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


# calcuating the body measurement
ratio=ration_factor(height,points[0],points[28])

# cv2.line(frame,points[0],points[28],(255,0,0),3)
# cv2.putText(frame,'A',points[0],cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# cv2.putText(frame,'B',points[28],cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# a1=find_mid_point(points[0],points[28])
# d1=find_distance(points[0],points[28])
# d1='{:.2f}'.format(d1)
# cv2.putText(frame,str(d1),a1,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
#
# cv2.line(frame,points[12],points[16],(255,0,0),3)
# cv2.putText(frame,'C',points[12],cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# cv2.putText(frame,'D',points[16],cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# a1=find_mid_point(points[12],points[16])
# d1=find_distance(points[12],points[16])
# d1='{:.2f}'.format(d1)
# cv2.putText(frame,str(d1),a1,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
#
# cv2.line(frame,points[23],points[27],(255,0,0),3)
# cv2.putText(frame,'E',points[23],cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# cv2.putText(frame,'F',points[27],cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# a1=find_mid_point(points[23],points[27])
# d1=find_distance(points[23],points[27])
# d1='{:.2f}'.format(d1)
# cv2.putText(frame,str(d1),a1,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
#
# cv2.line(frame,points[11],points[12],(255,0,0),3)
# cv2.putText(frame,'G',points[11],cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# t1=(points[12][0]+30,points[12][1])
# cv2.putText(frame,'H',t1,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
# a1=find_mid_point(points[11],points[12])
# d1=find_distance(points[11],points[12])
# d1='{:.2f}'.format(d1)
# cv2.putText(frame,str(d1),a1,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)





# first let's find all measurement for suit(coat)

#1. suit lenght , factor=10 for suit lenght
lengths=suit_lenght(ratio,points[12],points[24],0)
#2 arm lenght , factor=2.6
arms=suit_lenght(ratio,points[12],points[16],0)
#3 chest ,factor=13(there are 2 side comes in chest so we have to take twice of factor)
chests=chest(ratio,points[12],points[11],0)

#4 shoulder lenght , factor=3.5 (there are 2 side in shoulder so we have to also take twice of factor)
shoulder=suit_lenght(ratio,points[12],points[11],0)

# paint length for lower body part factor=10.33
paint_lenght=suit_lenght(ratio,points[24],points[28],0)

# now calculating circular measurement
# first lets take upper body waist
p=(a,b)
contours,edge,edgess=edge_detection(img)
print('contour values are',contours)
print('checking center value in edge detection ..')
print(check_y_coordinate(contours,p))
sides,_=check_y_coordinate(contours,p)
print('center and sides points',p,sides)
# cv2.circle(img=edgess, center = sides, radius =2, color =(0,0,255), thickness=2)
# cv2.circle(img=edgess, center = p, radius =2, color =(255,0,0), thickness=2)
# sd=(sides[0]-9,sides[1])
# cv2.line(edgess,p,sd,(255,0,0),3)
# cv2.drawContours(frame, edge, -1, (0, 255, 0), 3)

circume_ference=find_radius(p,sides,ratio)
print('upper body waist is  ',circume_ference)

print('lenght =',lengths)
print('arms lenght',arms)
# print('chest ',chests)
print('shoulder lenght',shoulder)
print('paint lenght',paint_lenght)
# cv2.imwrite('data-vaule.png',frame)




# now working in circular measurement

# 1 first let's check the chest
chest_mid=find_mid_point(points[11],points[12])
temp=(chest_mid[0],chest_mid[1])
temp2=(points[11][0],points[11][1])
# cv2.circle(frame,temp2,3,(255,0,0),3)
# cv2.circle(frame,temp,3,(255,0,0),3)
ch=suit_lenght(ratio,temp2,temp,0)
chests=ch*4
cht=2*ch*3.14
print('chest value is ',chests)
print('chest with pi',cht)
# heap of the body using key points
heap=suit_lenght(ratio,points[24],points[23],0)
heap=heap*2*3.14
print('heap of the body is ',heap)

# calculating the thigh
temp=find_mid_point(points[23],points[25])
hside,_=check_y_coordinate(contours,temp)
thigh=suit_lenght(ratio,temp,hside,0)
thigh=2*3.14*thigh
print('thigh of the body',thigh)
cv2.circle(frame,temp,2,(255,0,0),3)
cv2.circle(frame,hside,2,(255,0,0),3)
cv2.line(frame,temp,hside,(255,0,0),3)

# cv2.imwrite('heap2.png',frame)
cv2.imshow('mediapipe_circular',frame)
cv2.imshow('edgess',edgess)

cv2.waitKey(0)