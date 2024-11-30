class Other_fun:
    
    def __init__(self):
        
        with open(r"C:\Users\hacia\Desktop\Ri_Project\StopList.txt", "r") as fo:
            self.StopList = [line.strip() for line in fo.readlines() if line.strip() != ""]

    def check_Stop_List(self, stopwords):
        
        for word in stopwords:
            if word in self.StopList:
                return False
        return True
    
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
        
    def inserf(self,freqi):
        
        freqi.append(1)
        
    def postion(self,word,indexi,list):
        for tk,tk2 in indexi ,list:
            if word == tk2 :
                return True
        return False

test = Other_fun()

list = ['amine','haciane','wlid','alger','qlf','amine']
index = []
freqi = []

for tok in list:
    print(test.postion(tok,index))
    test.inser(tok,index)
    test.inserf(freqi)
    
    
print(index)
print(freqi)

    

         





 

 

