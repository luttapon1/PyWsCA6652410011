import math
def twodigits(x):
    return format( x, ".2f")

def Square():
    print(' -----Square------ ' )
    def doSquare():
        try :
            width = float(input("ป้อนความกว้าง : "))
            length = float(input("ป้อนความยาว : "))
            print(f'พื้นที่สี่เหลี่ยมที่คำนวนได้คือ : {twodigits(width*length)}')

        except ValueError:
            print('โปรดป้อนแต่ตัวเลข......')
            doSquare()
    doSquare()

def Circle() :
    print(' -------Circle------- ')
    def doCircle() :
        try :
            radius = float(input("ป้อนรัศมีวงกลม"))
            print(f'พื้นที่วงกลมที่คำนวนได้คือ : {twodigits(math.pi * radius**2)}')


        except ValueError :
            print('โปรดป้อนแต่ตัวเลข......')
        doCircle()
    doCircle()    