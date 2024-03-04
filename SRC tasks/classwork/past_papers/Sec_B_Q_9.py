class Treausure ():

    def __init__ (self,value:int,level:str) -> None:
        self.__value = value # private
        self.__level = level # private
    # end constructor function
        
    def getValue(self) -> int:
        return self.__value
    # end fucntion

    def getLevel(self) -> str:
        return self.__level
    # end function

    def setValue(self,value:int) -> None:
        self.__value = value
    # end fucntion

    def setLevel(self, level: str) -> None:
        self.__level = level
    # end function
        
goldCup = Treausure(500,'gold')

print(goldCup.getValue(), goldCup.getLevel())