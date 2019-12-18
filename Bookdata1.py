
class Book:
    def __init__(self,id=0,nm="",price=0.0):   #constructer
        self.__id=id                         #private variable
        self.__name=nm                      #private variable
        self.__price=price                  #private variable

    def __str__(self):                        #to-string
        return "Id : "+str(self.__id)+"\nName : "+self.__name+"\nPrice : "+str(self.__price)

    def setName(self,nm):      
        self.__name=nm
    def setPrice(self,price):
        self.__price=price
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    
    def calcAmt(self,n):
        return self.__price*n

if __name__=="__main__":
    b=Book(123,"python",234.00)
    print(b)
    print("Amount : ",b.calcAmt(5))
