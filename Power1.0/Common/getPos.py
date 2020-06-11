import time

import pyautogui as py 
import pyautogui


def get_pos(x_dis,y_dis):
    x1=py.position()[0]
    y1=py.position()[1]
    checkbox_x=x1+x_dis
    checkbox_y=y1+y_dis
    postion=[checkbox_x,checkbox_y]
    return(postion)

def get_MultiPos(x,y,x_dis,y_dis):
    checkbox_x=x+x_dis
    checkbox_y=y+y_dis
    postion=[checkbox_x,checkbox_y]
    return(postion)
#     py.click(checkbox_x,checkbox_y)
if __name__=='__main__':
    time.sleep(2)
    for i in range(15):
        y=i*40
        get_pos(0,y)
        pyautogui.click(get_MultiPos(395,143,0,y)[0],get_MultiPos(395,143,0,y)[1])
        time.sleep(2)
    