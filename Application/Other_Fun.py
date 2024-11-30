class Other_fun:
    
    def __init__(self):
        
        with open(r"C:\Users\hacia\Desktop\Ri_Project\StopList.txt", "r") as fo:
            self.StopList = [line.strip() for line in fo.readlines() if line.strip() != ""]

    def check_Stop_List(self, stopwords):
        if stopwords in self.StopList:
                return True
        return False
    
    def Check_Size(self,Word):
        return len(Word)
    
    def Extraite(self, word, size):
        # Truncate the word to the given size
        return word[:size]
    
    def voyelle(self,mot):
        voyelles = "aeiouAEIOU"  
        for lettre in mot:
            if lettre in voyelles:
                return True 
        return False  

    def count_voyelle_consonne(self, mot):
        voyelles = "aeiouAEIOU"
        count = 0
        
        for i in range(len(mot) - 1):
            if mot[i] in voyelles and mot[i + 1] not in voyelles:
                count += 1  # Found a vowel-consonant sequence

        return count
    
    def inser(self, word, indexi):
        
        indexi.append(word)  
    
    def inserf(self, freqi):
         
        freqi.append(1)
    
    def postion(self, word, indexi):
    
        if word in indexi:
            return indexi.index(word)
        return -1
    
    def modfief(self, Pos, freqi):
        
        if Pos != -1:
            freqi[Pos] += 1

test = Other_fun()

list = ['amine','amine2','wlid','alger', 'haciane', 'wlid', 'alger', 'qlf', 'amine']
index = []
freqi = []

# for tok in list:
     
#     if tok not in index:   
#         test.inser(tok, index)    
#         test.inserf(freqi)         
#     else:   
#         pos = test.postion(tok, index)   
#         test.modfief(pos, freqi)

 
# print("Index:", index)   
# print("Frequency:", freqi)  

    

         





 

 

