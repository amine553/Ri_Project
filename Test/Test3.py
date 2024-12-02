from Token_Create import Tkn
from Other_Fun import Other_fun
import os
from math import log

folder_path = r'C:\Users\hacia\Desktop\Ri_Project\Collection_TIME'
collection = []
# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            # Read the content of the file and add it to the collection list
            collection.append(file.read().strip())

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
    
    # print("Index",indexDi)
    # print("Frequeincei",freqiDi)
    Dict1.append(dict(zip(indexDi, freqiDi)))
    index.append(indexDi)
    freqi.append(freqiDi)
    
# print("The TF Dict",Dict1)
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
# print("The IDF Dict :",IDF_D)

# Initialize an empty list to store the final Wi for all documents
Wi = []

for tf_dict in Dict1:
    # Compute Wi for each document using the TF dictionary and the global IDF dictionary
    wi_dict = FunApp.compute_tf_idf(tf_dict, IDF_D)
    Wi.append(wi_dict)

# Now you can print the results of the weighted TF-IDF (Wi) for each document
print("Le poids des terms dont le document")
print(Wi)



