from threading import Thread
import time
cake=0
money=3000
class cooker(Thread):
    def run(self) -> None:
        global cake
        global money
        while True :
            if cake==300:
                time.sleep(3)
            if cake<300:
                cake += 1
            print(f"蛋糕的数量为:{cake}")
            if money==0:
                break
class eat(Thread):
    eatname=""
    count=0
    def run(self) -> None:
        global money
        global cake
        while money>=2:
            if cake>0:
                money=money-2
                cake=cake-1
                self.count+=1
            elif cake==0:
                time.sleep(3)
            print(f"{self.eatname}买了多少{self.count}余额:{money}")

c1=cooker()
c2=cooker()
c3=cooker()

e1=eat()
e2=eat()
e3=eat()
e4=eat()
e5=eat()
e6=eat()

e1.eatname="a"
e2.eatname="b"
e3.eatname="c"
e3.eatname="d"
e4.eatname="e"
e5.eatname="f"
e6.eatname="g"



c1.start()
c2.start()
c3.start()

e1.start()
e2.start()
e3.start()
e4.start()
e5.start()
e6.start()

