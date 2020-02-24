class HotCoffee(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class ColdCoffee(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Coffee():
    def __init__(self,temp):
        self.__temp=temp

    def print(self):
        if self.__temp<20:
            #print("cold coffee")
            raise ColdCoffee ('temperature is ' + str(self.__temp))

        if self.__temp<90 and self.__temp>20:
            print("Normal coffee")

        if self.__temp>90:
            #print("hot coffee")
            raise HotCoffee ('temperature is ' + str(self.__temp))

c=Coffee(11)
c.print()