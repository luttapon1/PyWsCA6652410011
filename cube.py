import math
def twodigits(x):
    return format( x, ".2f")


def vSquare() :
    print(' -------- vSquare ---------')
    def dovSquare():
       try:
           width = float(input("ป้อนความกว้าง: "))
           length = float(input("ป้อนความยาว: "))
           height = float(input("ป้อนความสูง: "))
           print(f"ปริมาตรทรงสี่เหลี่ยมที่คำนวณได้คือ: {twodigits(width*length*height)}")
           print("**************************************")
       except ValueError:
            print('โปรดป้อนแต่ตัวเลข......')
            dovSquare()
    dovSquare()

def vCircle():
    print( ' ---------vcircle---------- ')
    def doCircle():
        try:
           radius = float(input("ป้อนรัศมี: "))
           print(f"ปริมาตรทรงกลมที่คำนวณได้คือ: {twodigits(4/3 * math.pi * radius**3)}")
           print("**************************************")
        except ValueError:
            print("Please put in numbers...")
            doCircle()
    doCircle()
