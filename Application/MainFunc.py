    # this part used to append a char to list
    # truncated_word = CheckOut.Extraite(Word, 4)  # Call the 'Extraite' method correctly
    # index.append(truncated_word)  # Append the truncated word to the index list
from Token_Create import Tkn
from Other_Fun import  Other_fun
Di = 'The abdominal external oblique muscle forms the superficial layer of the abdominal wall. algereies'
Tokeniser = Tkn()
Tokens = Tokeniser.FinalTokens(Di)
FunApp = Other_fun()

index = []
freqi = []

        # FunApp.inser(Tokj,index)
        # FunApp.inserf(freqi)
for Tokj in Tokens :
    if not FunApp.check_Stop_List(Tokj):
        Mot = Tokj 
        L = FunApp.Check_Size(Tokj)
        if L > 3:
            if Mot[L-1] == 's' and Mot[L-2] == 'e' and Mot[L-3] == 'i' :
                Mot = FunApp.Extraite(Mot,L-2)
                L = L-2
            if Mot[L-1] == 's':
                Mot = FunApp.Extraite(Mot,L-1) 
                L = L-1
            if Mot[L-1] == 'd' and Mot[L-2] == 'e' and FunApp.voyelle(FunApp.Extraite(Mot,L-2)):
               Mot = FunApp.Extraite(Mot,L-1)
               L = L-1
            if Mot[L-1] == 'y':
                Mot = FunApp.Extraite(Mot,L-1)
                L = L - 1
                Mot = Mot + 'i'
            if FunApp.Check_Size(Mot) > 6 :
                if Mot[L-1] == 'n' and Mot[L-2] == 'o' and Mot[L-3] == 'i' and Mot[L-4] == 't' and Mot[L-5] == 'a' and FunApp.count_voyelle_consonne(Mot):
                    Mot = FunApp.Extraite(Mot,L-5) + 'ate'
                    L = L - 2
                if Mot[L-1] == 't' and Mot[L-2] == 'n' and Mot[L-3] == 'a' and FunApp.count_voyelle_consonne(Mot) > 1:
                    Mot = FunApp.Extraite(Mot,L-3)
                    L = L - 3
                if Mot[L-1] == 'e' and Mot[L-2] == 't' and Mot[L-3] == 'a' and FunApp.count_voyelle_consonne(Mot) > 1:
                    Mot = FunApp.Extraite(Mot,L-3)
                    L = L - 3 
                if Mot[L-1] == 's' and Mot[L-2] == 's' and FunApp.count_voyelle_consonne(Mot) > 1:
                    Mot = FunApp.Extraite(Mot,L-1)
                    L = L - 1
                if Mot[L-1] == 'l' and Mot[L-2] == 'a' and FunApp.count_voyelle_consonne(Mot) > 1:
                    Mot = FunApp.Extraite(Mot,L-2)
                    L = L - 2
                if Mot[L-1] == 'e' and FunApp.count_voyelle_consonne(Mot) > 1:
                    Mot = FunApp.Extraite(Mot,L-1)
                    L = L - 1
                if Mot[L-1] == 't' and FunApp.count_voyelle_consonne(FunApp.Extraite(Mot,L-1)) > 1:
                    Mot = FunApp.Extraite(Mot,L-1)
                    L = L - 1      
                
        if Mot not in index:                   
            FunApp.inser(Mot,index)
            FunApp.inserf(freqi)      
        else:   
            pos = FunApp.postion(Mot, index)   
            FunApp.modfief(pos, freqi)
        
print(index)
print(freqi)



 









 