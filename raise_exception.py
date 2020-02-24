class Coffee:
    def __init__(self,temp):
        self.__temp=temp

    def print(self):
        if self.__temp<20:
            #print("cold coffee")
            raise Exception ('Cold coffee')

        if self.__temp<90 and self.__temp>20:
            print("Normal coffee")
        if self.__temp>90:
            #print("hot coffee")
            raise ZeroDivisionError('hot coffee')

c=Coffee(55)
c.print()