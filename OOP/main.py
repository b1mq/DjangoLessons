# class House:
#     def __init__(self,number:int,adress:str,countOfPeople:int,countOfStocks:int,color:str,freePlacesInHouse:int)->None:
#         self.number = number
#         self.adress = adress
#         self.countOfPeopleInHouse = countOfPeople
#         self.countOfStocks = countOfStocks
#         self.houseColor = color
#         self.freePlaces = freePlacesInHouse
#     def change_House_Color(self,countOfAcceptedPeople:int,newColor:str)->bool:
#         if(countOfAcceptedPeople == self.countOfPeopleInHouse or countOfAcceptedPeople >self.countOfPeopleInHouse/2):
#             self.houseColor = newColor
#             print("YEESS you have a new house color")
#             return True
#         return False
#     def add_people_to_house(self,amount:int) ->True:
#         if(amount > 0 and amount <= self.freePlaces):
#             self.countOfPeopleInHouse += amount
#             self.freePlaces -= amount
#             return True
#         return False
#     def get_house_info(self)->None:
#         print(f"Hello im house on the  {self.adress}\n My House number is {self.number} \n Count of people in my house is {self.countOfPeopleInHouse} \n My color is {self.houseColor} \n Count of free place in house is {self.freePlaces} \n Count of stocks is {self.countOfStocks} \n Goodbye)")
        
# myNewHouse = House(19,"Altstadt",12,3,"white",5)
# myNewHouse.get_house_info()
from Gruppa import Grupp
if __name__ == "__main__":
    gruppa =  Grupp()
    print(gruppa.__str__())