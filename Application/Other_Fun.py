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
                count += 1   

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

    def compute_tf_idf(self,tf_dict, idf_dict):
        wi_dict = {}

        for word, tf_value in tf_dict.items():
            if word in idf_dict:   
                idf_value = idf_dict[word]
                wi_dict[word] = tf_value * idf_value  

        return wi_dict



    

         





 

 

