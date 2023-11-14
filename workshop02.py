import random
try :
    correctnumber = random.randint(1,100)
    def inputnumber():
        try :
            n = int(input("ป้อนตัวเลขที่ต้องการทาย (1-100): "))    
            if n == correctnumber:
                print("ยินดีด้วยคุณทายถูก")
            elif n > correctnumber:
                print("คุณทายผิดตัวเลขที่ป้อนมากไป")
                inputnumber()
            elif n < correctnumber:
                print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
                inputnumber() 

        except ValueError:
            print("โปรดป้อนแต่ตัวเลข..........")


    inputnumber()

except Exception:
   print("Exception found...")