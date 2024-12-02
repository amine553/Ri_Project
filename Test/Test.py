from Token_Create import Tkn
from Other_Fun import Other_fun
from collections import Counter
from math import log
collection = [
    "The abdominal  abdominal abdominal external oblique muscle forms the superficial layer of the abdominal wall. algereies Covid-19 19, farwell he's wlid alger 19 alger-19 alger-19 l'agregartionn covid-19",
    "This world shall Know The True pain of Alger 91 and the most unique one is alger-19 alger-19 abdominal","wlid wlid alger covid-19 alger-19"
]

Tokeniser = Tkn()
FunApp = Other_fun()
index = []
freqi = []
Dict1 = []
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
    
    print("Index",indexDi)
    print("Frequeincei",freqiDi)
    Dict1.append(dict(zip(indexDi, freqiDi)))
    index.append(indexDi)
    freqi.append(freqiDi)
    
print("The TF Dict",Dict1)
print("----------------------------------------------------------------------------------\n\n\n\n")

# Initialize an empty dictionary to store the merged terms and frequencies
IDF_D = {}

# Process the lists
for idx_list in index:
    # Create a set for the current list to track unique terms
    terms_set = set(idx_list)
    
    # For each unique term in the current list, add it to the dictionary
    for term in terms_set:
        if term not in IDF_D:
            IDF_D[term] = 1  # Add the term with frequency 1
        else:
            IDF_D[term] += 1  # Increment the frequency if the term exists already

for key in IDF_D:
    IDF_D[key] = log(len(index) / IDF_D[key] ,10)


print("----------------------------------------------------------------------------------\n\n\n\n")
print("The IDF Dict :",IDF_D)

Wi = FunApp.compute_tf_idf(Dict1,IDF_D)

print("New Weighted TF-IDF (Wi) Dictionary:")
print(Wi)



