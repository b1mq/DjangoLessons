import json

class MyDictionary:
    def __init__(self,name:str):
        self.name = name
        self.Md: dict[str,str] = {}
    def CheckWord(self,word:str)->bool:
        if(not word):
            return False
        return word
    def AddWord(self,word:str,translated:str)->bool:
         if(not self.CheckWord(word) ) or (not self.CheckWord(word)):
             return False
         self.Md[word] = translated
         return True
    def RemoveWord(self,word:str)->bool:
        if not self.CheckWord(word) or word not in self.Md:
            return False

        del self.Md[word]
        return True
    def EditWord(self,word,editedWord)->bool:
        if(not self.CheckWord(word) ) or word not in self.Md or not editedWord:
            return False
        self.Md[word] = editedWord
        return True
    def ShowDictionary(self):
        for word in self.Md:
            print(f"{word } -> {self.Md[word]}")
    def SaveDictionary(self) -> bool:
        try:
            with open(f"{self.name}.json", "w", encoding="utf-8") as file:
                json.dump(self.Md, file, ensure_ascii=False, indent=4)
            return True
        except (OSError, TypeError):
            return False



if __name__ == "__main__":
    
    # md = MyDictionary("First")
    # md.AddWord("Hello","Привет")

    # if md.SaveDictionary():
    #     print("Dictionary saved!")
    # else:
    #     print("Error saving dictionary!")
    
    