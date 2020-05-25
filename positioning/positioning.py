import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#차량 번호판 좌표
car_position = []
#영상에 주차되어 있는 차량
car_number = []

#setting : encoding='UTF8'
fp = open('car_position.txt', mode='rt', encoding="utf8")
fn = open('car_number.txt', mode='rt',encoding="utf8")
number = 0

for line in fp:
    data = line.split(' ')
    data_area = data[0]
    data_x = data[1]
    data_y = data[2]
    number += 1
    car_position.append({
        'area': data_area,
        'x': data_x,
        'y': data_y[:-1],
    })

for line in fn:
    car_number.append(line[:-1])

#print(car_number)
#print(car_position)

#사용자로부터 입력받는 차량번호
car_info = []
#사용자로부터 차량 번호를 받아옵니다
car_info = input('차량번호를 입력하세요 : ')

cnt = 0
find_num = 0
for j in range(0, number):
    for i in range(0, 7):
        #차량 번호판을 확인합니다
        if car_number[j][i] == car_info[i]:
            if cnt >= 6:
                continue
            cnt += 1
            find_num = j

if cnt >= 5:
    if car_position[find_num]['area'] == 'A':
        x = 40
        y = 40
    elif car_position[find_num]['area'] == 'B':
        x = 550
        y = 40
    elif car_position[find_num]['area'] == 'C':
        x = 40
        y = 360
    else:
        x = 550
        y = 360
else:
    print('없는 차량입니다\n')

#A 구역 주차장 이미지 입니다
a = cv2.imread('a.jpg')
#red로 주차된 차량 위치를 알려줍니다
red = (0, 0, 255)

if cnt >= 5:
    if car_position[find_num]['area']=='A':
        sum_y=(int(car_position[0]['y'])+int(car_position[1]['y'])+int(car_position[2]['y']))/3
        int(sum_y)
    elif car_position[find_num]['area']=='B':
        sum_y = (int(car_position[0]['y']) + int(car_position[1]['y']) + int(car_position[2]['y'])) / 3
        int(sum_y)
    elif car_position[find_num]['area']=='C':
        sum_y = (int(car_position[0]['y']) + int(car_position[1]['y']) + int(car_position[2]['y'])) / 3
        int(sum_y)
    else:
        sum_y = (int(car_position[0]['y']) + int(car_position[1]['y']) + int(car_position[2]['y'])) / 3
        int(sum_y)

if cnt >=5:
    #첫번째 차량 위치표시
    if car_number[find_num]==car_number[0]:
        x1 = int(int(car_position[find_num]['x'])/2)
        y1 = int(sum_y/2)

        # a.jpg 그림  : (첫번째 줄, 첫번째 칸) 기준 = (0,0)
        #(0,0) 주차공간
        if 0 <= x1 <= 240 and 0 <= y1 <= 270 :
            cv2.circle(a, (140, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(1,0) 주차공간
        elif 0 <= x1 <= 240 and 270 < y1 <= 540 :
            cv2.circle(a, (140, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(1,0) 주차공간
        elif 240 < x1 <= 480 and 0 <= y1 <= 270 :
            cv2.circle(a, (365, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(1,1) 주차공간
        elif 240 < x1 <= 480 and 270 < y1 <= 540 :
            cv2.circle(a, (365, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(2,0) 주차공간
        elif 480 < x1 <= 720 and 0 <= y1 <= 270:
            cv2.circle(a, (590, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(2,1) 주차공간
        elif 480 < x1 <= 720 and 270 < y1 <= 540:
            cv2.circle(a, (590, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(3,0) 주차공간
        elif 720 < x1 <= 960 and 0 <= y1 <= 270:
            cv2.circle(a, (815, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(3,1) 주차공간
        elif 720 < x1 <= 960 and 270 < y1 <= 540:
            cv2.circle(a, (815, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

    #두번째 차량 위치표시
    elif car_number[find_num]==car_number[1]:
        x2 = int(int(car_position[find_num]['x'])/2)
        y2 = int(sum_y/2)

        #(0,0) 주차공간
        if 0 <= x2 <= 240 and 0 <= y2 <= 270:
            cv2.circle(a, (140, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(0,1) 주차공간
        elif 0 <= x2 <= 240 and 270 < y2 <= 540:
            cv2.circle(a, (140, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(1,0) 주차공간
        elif 240 < x2 <= 480 and 0 <= y2 <= 270:
            cv2.circle(a, (365, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(1,1) 주차공간
        elif 240 < x2 <= 480 and 270 < y2 <= 540:
            cv2.circle(a, (365, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(2,0) 주차공간
        elif 480 < x2 <= 720 and 0 <= y2 <= 270:
            cv2.circle(a, (590, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(2,1) 주차공간
        elif 480 < x2 <= 720 and 270 < y2 <= 540:
            cv2.circle(a, (590, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(3,0) 주차공간
        elif 720 < x2 <= 960 and 0 <= y2 <= 270:
            cv2.circle(a, (815, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(3,1) 주차공간
        elif 720 < x2 <= 960 and 270< y2 <= 540:
            cv2.circle(a, (815, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

    #세번째 차량 위치 표시
    elif car_number[find_num]==car_number[2]:
        x3 = int(int(car_position[find_num]['x'])/2)
        y3 = int(sum_y/2)

        #(0,0) 주차공간
        if 0 <= x3 <= 240 and 0 <= y3 <= 270:
            cv2.circle(a, (140, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(0,1) 주차공간
        elif 0 <= x3 <= 240 and 270 < y3 <= 540:
            cv2.circle(a, (140, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(1,0) 주차공간
        elif 240 < x3 <= 480 and 0 <= y3 <= 270:
            cv2.circle(a, (365, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(1,1) 주차공간
        elif 240 < x3 <= 480 and 270 < y3 <= 540:
            cv2.circle(a, (365, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(2,0) 주차공간
        elif 480 < x3 <= 720 and 0 <= y3 <= 270:
            cv2.circle(a, (590, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(2,1) 주차공간
        elif 480 < x3 <= 720 and 270 < y3 <= 540:
            cv2.circle(a, (590, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

        #(3,0) 주차공간
        elif 720 < x3 <= 960 and 0 <= y3 <= 270:
            cv2.circle(a, (815, 130), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        #(3,1) 주차공간
        elif 720 < x3 <= 960 and 270 < y3 <= 540:
            cv2.circle(a, (815, 400), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
