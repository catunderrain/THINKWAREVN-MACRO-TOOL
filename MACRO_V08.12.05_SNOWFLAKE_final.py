#---------------------------------------------------------------------------------------------------------- IMPORT BLA BLA BLAH :)
import keyboard
import pyautogui
from time import sleep
from screeninfo import get_monitors

#------------------------------------------------------------------------------------------------------------------ PRINT INTRO :)
def introduction():
    intro = """
    ╔════════════════════════════════════════════════════════════════════════╗
    ║                       WELCOME TO THE MACRO LABEL TOOL                  ║
    ║                Conceptualized, Developed, and Perfected by             ║
    ║                              NGUYEN THAI TOAN                          ║
    ║                         Version: v08.12.05 - 2024                      ║
    ║                             SNOWFLAKE EDITION                          ║
    ║                                                                        ║
    ║        "This is not just a tool. It’s a vision brought to life."       ║
    ║                                                                        ║
    ║    License: MIT License                                                ║
    ║     You are free to use, modify, and distribute this tool, as long     ║
    ║     as credit is attributed to the original author.                    ║
    ║                                                                        ║
    ║    FEATURES:                                                           ║
    ║     - Precise labeling at the speed of thought.                        ║
    ║     - Unparalleled user experience for optimal productivity.           ║
    ║     - Designed to empower professionals worldwide.                     ║
    ║                                                                        ║
    ║        --- PERFECTION IS NOT AN OPTION, IT’S THE STANDARD ---          ║
    ║                                                                        ║
    ║                        ❆ BTW MERRY CHRISTMAS! ❆                        ║
    ║               Ready to redefine how you label? Let’s go!               ║
    ╚════════════════════════════════════════════════════════════════════════╝
    """
    print(intro)

introduction()

#------------------------------------------------------------------------------------------------------------------------- HELP :)
help_lines = r"""----------------------------------------------------------------------------------------
Key			Function
========================================================================================
`			get position	    : for debugging
1,2,3,4,5,6	car direction
0			direction None
7,8,9		color of sign	    : blue - yellow - red
-			switch mode         : main/break
=			increase sleep time	: (base) 0.1 - 0.15 - 0.2 - 0.25 - 0.3
q,e			backward/forward images + auto save
w,a,s,d		movements
r			like ctrl+E
t,ctrl+t	stopline, crosswalk
y,ctrl+y	draw combo of plate 1-3 for green/red light
u,i,o,p		shape of lightplate	: 3-1, 1-3, 3-2, 2-3
[,]			draw box of green/red light
ctrl + [,]	change label to green/red light
\			exit tool (just usable in MODE main)
f,g,h,j,k	5 direction of arrow (left, forward left, forward, forward right, right)
l			traffic cone label
;           stop sign
'			draw box of lightplate (with base shape 1-3)
ctrl+'		label to lightplate
z			like ctrl+z
x			visible/invisible all labels (like press T)
ctrl+x		label Heavy
c			car
alt+c		draw box of car
v			truck
b			bus
n			pedestrian
m			rider
,			motobike
.			bicycle
/           curve
space		zoom back to fit screen
----------------------------------------------------------------------------------------"""
#------------------------------------------------------------------------------------------------------------------ BIAS THINGS :)
# BASE PAUSE
pyautogui.PAUSE = 0.005

# BASE CTRL E
POS_CTRL_E = (700, 300)

# SPEED FOR WASD
SPEED_MOVE = 5

# MAKE COLOR
print('╔══════════════════════════════════════════════════════════════════════════════════════>')

# GET THE MONITOR SHAPE INFO
for monitor in get_monitors():
    w = monitor.width
    h = monitor.height
    print('║\tScreen\t:', w, 'x', h)

# CHECK FlAG
print('║\t> Input flag of 0 (or enter) for mostly use, 1 for special laptop')
input_flag = input('║\tFlag\t: ')
if input_flag == '1': PC_FLAG = 1
else                : PC_FLAG = 0
print('║\tPc flag\t:', PC_FLAG)

#---------------------------------------------------------------------------------------------------------------- BIAS POSITION :)
# CHOOSE BASE POSITION
if PC_FLAG == 0:
    print('║\tName\t: TW PC')
    POS_OK = (870,380)
    POS_LF = (720, 600)
    POS_RF = (900, 600)
    POS_LR = (720, 620)
    POS_RR = (900, 620)
    POS_LS = (720, 640)
    POS_RS = (900, 640)
    POS_31 = (765, 680)
    POS_13 = (720, 720)
    POS_32 = (765, 700)
    POS_23 = (740, 715)
    POS_NONE = (810, 610)
    MOV_R = (1585, 1005)
    MOV_L = (10, 1005)
    MOV_U = (1600, 115)
    MOV_D = (1600, 995)
    POS_ALL_LABEL = (1715, 250)
    POS_LB_NAME = (790, 355)
else:
    print('Laptop')
    POS_OK = (880,385)
    POS_LF = (720, 630)
    POS_RF = (920, 630)
    POS_LR = (720, 650)
    POS_RR = (920, 650)
    POS_LS = (720, 670)
    POS_RS = (920, 670)
    POS_31 = (760, 720)
    POS_13 = (720, 760)
    POS_32 = (760, 740)
    POS_23 = (740, 760)
    POS_NONE = (820, 640)
    MOV_R = (1510, 985)
    MOV_L = (10, 985)
    MOV_U = (1535, 140)
    MOV_D = (1535, 960)
    POS_ALL_LABEL = (1715, 250)
    POS_LB_NAME = (780, 360)

# BASE LABEL CODES
LB_PLATE = 100
LB_BLIGHT = 101
LB_RLIGHT = 105
LB_BSIGN = 200
LB_YSIGN = 201
LB_RSIGN = 202
LB_CAR = '000'
LB_TRUCK ='001'
LB_BUS = '002'
LB_HEAVY = '003'
LB_PED = '009'
LB_RID = '010'
LB_LM_L = 305
LB_LM_LF = 309
LB_LM_F = 304
LB_LM_RF = 310
LB_LM_R = 306
LB_CONE = 401
LB_BIKE = '005'
LB_MOTO = '004'
LB_STOPLINE = 300
LB_CROSSWALK = 301
LB_CURVE = 219
LB_STOP = 205

# MAKE COLOR
print('║\t> Press \'-\' to switch mode')
#-------------------------------------------------------------------------------------------------------------------- SMAL DEFS :)
# GET POSITION OF CLICKED
def get_pos():
    pos = pyautogui.position()
    print(pos)

# SLEEP
def slp(n=1):
    sleep(n*BASE_SLEEP_TIME)

# SHORTER FOR PRESS :D
def press(key):
    pyautogui.press(key)

# DELETE SOMETHING
def delete_enter():
    press('delete')
    slp(0.5)
    press('enter')

# CTRL SOMETHING
def ctrl(key=''):
    pyautogui.keyDown('ctrl')
    pyautogui.hotkey(key)
    pyautogui.keyUp('ctrl')
    
# MOVE TO THERE AND CTRL E :D
def move_ctrl_e_tab():
    r_pos = pyautogui.position()
    pyautogui.moveTo(POS_CTRL_E)
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.hotkey('tab')
    slp()
    pyautogui.moveTo(r_pos)

# MOVE + CTRL E + CLICK THE UNIQUE THING
def move(pos):
    r_pos = pyautogui.position()
    move_ctrl_e_tab()
    pyautogui.moveTo(pos)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    pyautogui.moveTo(POS_OK)
    pyautogui.click(button='left')
    pyautogui.moveTo(r_pos)

# LABEL THINGS :D
def label(lb):
    r_pos = pyautogui.position()
    move_ctrl_e_tab()
    pyautogui.moveTo(POS_LB_NAME)
    pyautogui.click(button='left')
    ctrl('a')
    pyautogui.typewrite(str(lb))
    pyautogui.moveTo(POS_OK)
    pyautogui.click(button='left')
    pyautogui.moveTo(r_pos)

# MOVE TO THERE AND CLICK :D
def move_click(pos, n=1):
    r_pos = pyautogui.position()
    for _ in range(n): pyautogui.click(x=pos[0], y=pos[1])
    pyautogui.moveTo(r_pos)

# MAKE A BOX! :D
def make_box(lb, w=50, h=50):
    ctrl('r')
    x, y = pyautogui.position()
    pyautogui.mouseDown()
    pyautogui.moveTo(x=x+w, y=y+h)
    pyautogui.click()
    slp()
    press('enter')
    slp()
    press('enter')
    pyautogui.hotkey('ctrl','j')
    slp()
    pyautogui.moveTo(x=x+10, y=y+10)
    pyautogui.click()
    slp()
    label(lb)
    pyautogui.moveTo((x, y))
    
# YAH! MAKE A BOX WITHOUT LABE IT :D
def make_box_nolabel(w=50, h=50):
    ctrl('r')
    x, y = pyautogui.position()
    pyautogui.mouseDown()
    pyautogui.moveTo(x=x+w, y=y+h)
    pyautogui.click()
    slp()
    press('enter')
    slp()
    press('enter')
    pyautogui.hotkey('ctrl','j')
    pyautogui.moveTo((x, y))

# SIMPLY CTRL A :)
def collect_all(): 
    r_pos = pyautogui.position()
    pyautogui.moveTo(POS_ALL_LABEL)
    pyautogui.click()
    ctrl('a')
    pyautogui.moveTo(r_pos)

# ALT TAB :D
def alt_tab():
    pyautogui.hotkey('alt', 'tab')

#----------------------------------------------------------------------------------------------------------------------- MAIN 1 :)
# DIVE INTO IT :)
def main():
    print('╠═══════════════════\tMODE\t: main')
    
    # TAB!
    alt_tab(); sleep(0.1)
    
    # BLOCKED KEYS - THAT LL BE UNLOCK IN MAIN_2 =)))
    keyboard.block_key('a')
    keyboard.block_key('d')
    keyboard.block_key('z')
    keyboard.block_key('w')
    keyboard.block_key('left shift')
    keyboard.block_key('capslock')
    keyboard.block_key('tab')
    keyboard.block_key('left alt')
    keyboard.block_key('t')
    
    # I JUST THINK GLOBAL IT WILL FIX SOME BUGS :D
    global BASE_SLEEP_TIME_LIST
    global BASE_SLEEP_TIME

    BASE_SLEEP_TIME_LIST = [0.1,0.15,0.2,0.25,0.3]
    BASE_SLEEP_TIME = BASE_SLEEP_TIME_LIST[0]
    print('║\tBase sleep:\t', BASE_SLEEP_TIME)

    while True:
        # CTRL STUFFS
        if keyboard.is_pressed          ('ctrl'):
            if keyboard.is_pressed('left shift'):
                    pass
            elif keyboard.is_pressed        ('['):
                label(LB_BLIGHT); slp()
            elif keyboard.is_pressed        (']'):
                label(LB_RLIGHT); slp()
            elif keyboard.is_pressed        ('\''):
                label(LB_PLATE); slp()
            elif keyboard.is_pressed        ('d'):
                ctrl('d'); slp()        
            elif keyboard.is_pressed        ('y'):
                make_box(LB_PLATE, 50, 150); slp()
                move(POS_13); slp()
                make_box(LB_RLIGHT, 50, 50); slp(4)
            elif keyboard.is_pressed        ('w'):
                make_box(LB_BSIGN, 50, 50); slp()
            elif keyboard.is_pressed        ('s'):
                ctrl('s'); slp()
            elif keyboard.is_pressed        ('a'):
                ctrl('a'); slp()
            elif keyboard.is_pressed        ('x'):
                label(LB_HEAVY); slp()
            elif keyboard.is_pressed        ('t'):
                label(LB_CROSSWALK); slp()
            elif keyboard.is_pressed        ('h'):
                print(help_lines)
                slp(2)
            else:
                sleep(0.01)
        
        # ALT STUFFS
        elif keyboard.is_pressed          ('alt'):
            if keyboard.is_pressed('tab'):
                alt_tab(); slp()
            elif keyboard.is_pressed('c'):
                make_box(LB_CAR, 200, 150); slp(4)
            elif keyboard.is_pressed('a'):
                collect_all(); slp()
            elif keyboard.is_pressed('w'):
                ctrl('='); slp()
            elif keyboard.is_pressed('s'):
                ctrl('-'); slp()            
            else:
                pass
        
        # OTHERS STUFFS :)
        elif keyboard.is_pressed        ('='):
            BASE_SLEEP_TIME = BASE_SLEEP_TIME_LIST[(BASE_SLEEP_TIME_LIST.index(BASE_SLEEP_TIME)+1) % len(BASE_SLEEP_TIME_LIST)]
            print('║\t', BASE_SLEEP_TIME)
            slp()
        elif keyboard.is_pressed        (';'):
            pyautogui.keyDown('shift')
            sleep(0.3)
            pyautogui.keyUp('shift')
            slp()
        elif keyboard.is_pressed        ('y'):
            make_box(LB_PLATE, 50, 150); slp()
            move(POS_13); slp()
            pyautogui.moveRel(0,100)
            make_box(LB_BLIGHT, 50, 50); slp(4)
        elif keyboard.is_pressed        ('left shift'):
            delete_enter(); slp()
        elif keyboard.is_pressed        ('r'):
            move_ctrl_e_tab(); slp()
        elif keyboard.is_pressed        ('`'):
            get_pos(); slp(2)
        elif keyboard.is_pressed        ('space'):
            ctrl('f'); press('enter'); slp(2)
        elif keyboard.is_pressed        ('z'):
            ctrl('z'); slp()
        elif keyboard.is_pressed        ('0'):
            move(POS_NONE); slp()
        elif keyboard.is_pressed        ('1'):
            move(POS_LF); slp()
        elif keyboard.is_pressed        ('2'):
            move(POS_RF); slp()
        elif keyboard.is_pressed        ('3'):
            move(POS_LR); slp()
        elif keyboard.is_pressed        ('4'):
            move(POS_RR); slp()
        elif keyboard.is_pressed        ('5'):
            move(POS_LS); slp()
        elif keyboard.is_pressed        ('6'):
            move(POS_RS); slp()
        elif keyboard.is_pressed        ('u'):
            move(POS_31); slp()
        elif keyboard.is_pressed        ('i'):
            move(POS_13); slp()
        elif keyboard.is_pressed        ('o'):
            move(POS_32); slp()
        elif keyboard.is_pressed        ('p'):
            move(POS_23); slp()
        elif keyboard.is_pressed('['):
            make_box(LB_BLIGHT, 30, 30); slp(4)
        elif keyboard.is_pressed(']'):
            make_box(LB_RLIGHT, 30, 30); slp(4)
        elif keyboard.is_pressed('\''):
            make_box(LB_PLATE, 50, 150);  slp()
            move(POS_13); slp()
        elif keyboard.is_pressed        ('7'):
            label(LB_BSIGN); slp()
        elif keyboard.is_pressed        ('8'):
            label(LB_YSIGN); slp()
        elif keyboard.is_pressed        ('9'):
            label(LB_RSIGN); slp()
        elif keyboard.is_pressed        ('x'):
            pyautogui.press('t'); slp(2)
        elif keyboard.is_pressed        ('c'):
            label(LB_CAR); slp()
        elif keyboard.is_pressed        ('v'):
            label(LB_TRUCK); slp()
        elif keyboard.is_pressed        ('b'):
            label(LB_BUS); slp()
        elif keyboard.is_pressed        ('n'):
            label(LB_PED); slp()
        elif keyboard.is_pressed        ('m'):
            label(LB_RID); slp()
        elif keyboard.is_pressed        ('/'):
            label(LB_CURVE); slp()
        elif keyboard.is_pressed(';'):
            label(LB_STOP); slp()
        elif keyboard.is_pressed        ('q'):
            press('a'); slp(); press('enter'); slp(2)
        elif keyboard.is_pressed        ('e'):
            press('d'); slp(); press('enter'); slp(2)
        elif keyboard.is_pressed        ('w'):
            move_click(MOV_U, SPEED_MOVE)
        elif keyboard.is_pressed        ('s'):
            move_click(MOV_D, SPEED_MOVE)
        elif keyboard.is_pressed        ('d'):
            move_click(MOV_R, SPEED_MOVE)
        elif keyboard.is_pressed        ('a'):
            move_click(MOV_L, SPEED_MOVE)
        elif keyboard.is_pressed        ('f'):
            label(LB_LM_L); slp()
        elif keyboard.is_pressed        ('g'):
            label(LB_LM_LF); slp()
        elif keyboard.is_pressed        ('h'):
            label(LB_LM_F); slp()
        elif keyboard.is_pressed        ('j'):
            label(LB_LM_RF); slp()
        elif keyboard.is_pressed        ('k'):
            label(LB_LM_R); slp()
        elif keyboard.is_pressed        ('l'):
            label(LB_CONE); slp()
        elif keyboard.is_pressed('capslock'):
            make_box_nolabel(80, 80)
        elif keyboard.is_pressed        (','):
            label(LB_MOTO); slp()
        elif keyboard.is_pressed        ('.'):
            label(LB_BIKE); slp()
        elif keyboard.is_pressed        ('t'):
            label(LB_STOPLINE); slp()
        elif keyboard.is_pressed        ('\\'):
            slp()
            pyautogui.press('backspace')
            print('║\tEnding')
            print('╚══════════════════════════════════════════════════════════════════════════════════════>')
            exit()
        elif keyboard.is_pressed        ('-'):
            break

#----------------------------------------------------------------------------------------------------------------------- MAIN 2 :)
def main_2(): 
    print('╠═══════════════════\tMODE\t: break')
    
    # TAB!
    alt_tab(); sleep(0.1)
    
    # JUST UNBLOCK EVERYTHING FROM MAIN() :D
    keyboard.unblock_key('a')
    keyboard.unblock_key('d')
    keyboard.unblock_key('z')
    keyboard.unblock_key('w')
    keyboard.unblock_key('left shift')
    keyboard.unblock_key('capslock')
    keyboard.unblock_key('tab')
    keyboard.unblock_key('left alt')
    keyboard.unblock_key('t')

#-------------------------------------------------------------- BEG --------------------------------------------------------------
# SET BIAS FLAG :)
main_flag = 0

# NO UNDERSTAND == STUPID
while True:
    if keyboard.is_pressed('-'):
        sleep(0.1)
        main_flag += 1
        if main_flag % 2 == 0   : main_2() 
        else                    : main()
        
#-------------------------------------------------------------- END --------------------------------------------------------------
