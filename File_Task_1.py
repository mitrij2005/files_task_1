import json


class CookBookString:
    def __init__ (self, file_name ):
        self.file_name = file_name
        self.curr_str_type = 0
        self.curr_str_count = 1
        self.cook_book = {}
        self.ingridient = {'ingredient_name': None, 'quantity': None, 'measure': None}

        self.f = open (file_name, 'r', encoding='utf-8')

    def getstr (self) -> bool: 
        self.str = self.f.readline()
        if len(self.str) == 0:
            return False

        match self.curr_str_type:
            case 2:
                self.str = self.str.split("|")
            case _:
                self.str = " ".join(self.str.split())

        self.putstr()

        match self.curr_str_type:
            case 0:
                self.curr_str_type = 1
                self.curr_str_count = 1
        
            case 1:
                self.curr_str_type = 2
                self.curr_str_count = int (self.str)
    
            case 2:
                self.curr_str_count -= 1
                if self.curr_str_count == 0:
                    self.curr_str_type = 3
                    self.str_count = 1
            
            case 3:
                self.curr_str_type = 0
                self.str_count = 1
            
        return True

    def putstr(self):
        match self.curr_str_type:
            case 0:
                self.dish = str(self.str)
                self.cook_book[self.dish] = []

            case 2:
                j = 0
                for k, i in self.ingridient.items():
                    self.ingridient[k] = self.str[j].strip()
                    j += 1
                self.x = self.ingridient.copy()
                self.cook_book[self.dish].append(self.x)

    
    def __del__(self):
        self.f.close()        

    def get_cook_book(self) -> dict:
        while self.getstr() == True:    
            pass

        return self.cook_book
        
c_b =  CookBookString("recipes.txt")
print (json.dumps(c_b.get_cook_book(), indent=4, ensure_ascii=False))
pass
        
