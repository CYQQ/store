#1
# class cooker:
#     __name=""
#     __age=""
#     def setname(self,name):
#         self.__name=name
#     def setage(self,age):
#         self.__age=age
#     def getname(self):
#         return self.__name
#     def getage(self):
#         return self.__age
#     def cook(self):
#         print(self.__name,self.__age,"做饭")
# class cookerson(cooker):
#     def cook(self):
#         super().cook()
#         print("做一道炒菜")
# class cookergrandson(cookerson):
#     age=""
#     name=""
# cook=cookergrandson()
# cook.name="wang"
# cook.age="12"
# cook.setage("13")
# cook.setname("zhao")
# cook.cook()


#2
class person:
    age=""
    sex=""
    name=""
class worker(person):
    def work(self):
        print("工人信息为",self.name,self.sex,self.age,"在工作")
class student(person):
    STUnumber=""
    def study(self,number):
        self.STUnumber=number
        print(self.name,self.sex,self.age,self.STUnumber,"开始学习")
    def ring(self):
        print(self.name, self.sex, self.age, "开始唱歌")
# worker=worker()
# worker.age="22"
# worker.name="qian"
# worker.sex="man"
# worker.work()
stu=student()
stu.sex="man"
stu.age="11"
stu.age="999"
stu.study(input("请输入学号："))