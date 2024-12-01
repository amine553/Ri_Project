from Token_Create import Tkn
from Other_Fun import Other_fun

collection = [
    "The abdominal external oblique muscle forms the superficial layer of the abdominal wall. algereies Covid-19 19, farwell he's wlid alger 19 l'agregartionn covid-19",
    "This world shall Know The True pain of Alger 91 and the most unique one is ALger-19"
]

Tokeniser = Tkn()
FunApp = Other_fun()
index = []
freqi = []
for Di in collection:
    indexDi = []
    freqiDi = []
    Tokens = Tokeniser.FinalTokens(Di)
    
    # FunApp.inser(Tokj,index)
    # FunApp.inserf(freqi)
    for Tokj in Tokens:
        if not FunApp.check_Stop_List(Tokj):
            Mot = Tokj
            L = FunApp.Check_Size(Tokj)
            
            if L > 3:
                if Mot[L-1] == 's' and Mot[L-2] == 'e' and Mot[L-3] == 'i':
                    Mot = FunApp.Extraite(Mot, L-2)
                    L = L-2
                
                if Mot[L-1] == 's':
                    Mot = FunApp.Extraite(Mot, L-1)
                    L = L-1
                
                if Mot[L-1] == 'd' and Mot[L-2] == 'e' and FunApp.voyelle(FunApp.Extraite(Mot, L-2)):
                    Mot = FunApp.Extraite(Mot, L-1)
                    L = L-1
                
                if Mot[L-1] == 'y':
                    Mot = FunApp.Extraite(Mot, L-1)
                    L = L-1
                    Mot = Mot + 'i'
                
                if FunApp.Check_Size(Mot) > 6:
                    if Mot[L-1] == 'n' and Mot[L-2] == 'o' and Mot[L-3] == 'i' and Mot[L-4] == 't' and Mot[L-5] == 'a' and FunApp.count_voyelle_consonne(Mot):
                        Mot = FunApp.Extraite(Mot, L-5) + 'ate'
                        L = L-2
                    
                    if Mot[L-1] == 't' and Mot[L-2] == 'n' and Mot[L-3] == 'a' and FunApp.count_voyelle_consonne(Mot) > 1:
                        Mot = FunApp.Extraite(Mot, L-3)
                        L = L-3
                    
                    if Mot[L-1] == 'e' and Mot[L-2] == 't' and Mot[L-3] == 'a' and FunApp.count_voyelle_consonne(Mot) > 1:
                        Mot = FunApp.Extraite(Mot, L-3)
                        L = L-3
                    
                    if Mot[L-1] == 's' and Mot[L-2] == 's' and FunApp.count_voyelle_consonne(Mot) > 1:
                        Mot = FunApp.Extraite(Mot, L-1)
                        L = L-1
                    
                    if Mot[L-1] == 'l' and Mot[L-2] == 'a' and FunApp.count_voyelle_consonne(Mot) > 1:
                        Mot = FunApp.Extraite(Mot, L-2)
                        L = L-2
                    
                    if Mot[L-1] == 'e' and FunApp.count_voyelle_consonne(Mot) > 1:
                        Mot = FunApp.Extraite(Mot, L-1)
                        L = L-1
                    
                    if Mot[L-1] == 't' and FunApp.count_voyelle_consonne(FunApp.Extraite(Mot, L-1)) > 1:
                        Mot = FunApp.Extraite(Mot, L-1)
                        L = L-1
            
            if Mot not in indexDi:
                FunApp.inser(Mot, indexDi)
                FunApp.inserf(freqiDi)
            else:
                pos = FunApp.postion(Mot, indexDi)
                FunApp.modfief(pos, freqiDi)
    
    # print(indexDi)
    # print(freqiDi)
    index.append(indexDi)
    freqi.append(freqiDi)


print(index)
print(freqi)
print("----------------------------------------------------------------------------------\n\n\n\n")
Uniqe_Term = []
for List in index :
    for word in List :
        Uniqe_Term.append(word)

print(Uniqe_Term)
print("----------------------------------------------------------------------------------\n\n\n\n")
Uniqe_Term = list(set(Uniqe_Term))   
print(Uniqe_Term)
 