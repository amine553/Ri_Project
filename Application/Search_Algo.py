import pymongo
from Token_Create import Tkn
from Other_Fun import Other_fun


def retrieve_and_rank_docs(term_list):
    client = pymongo.MongoClient("mongodb://localhost:27017/") 
    db = client["Ri_Project"] 
    collection_db = db["Collection"] 

    Tokeniser = Tkn()
    FunApp = Other_fun()
    term_list = Tokeniser.FinalTokens(term_list)
    index = []   
    freqi = []  

    for Tokj in term_list:
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
            if Mot not in index:
                FunApp.inser(Mot, index)
                FunApp.inserf(freqi)
            else:
                pos = FunApp.postion(Mot, index)
                FunApp.modfief(pos, freqi)
    
    results = []   
    
    documents = collection_db.find()
    
    for doc in documents:
        doc_index = doc["index"]
        weights = doc["weights"]
        score = 0  
        for term in index:
            if term in doc_index:
                term_index = doc_index.index(term)   
                
                try:
                    if isinstance(weights, list):
                        tf_idf_weight = weights[term_index]  
                    elif isinstance(weights, dict):
                        tf_idf_weight = weights.get(term, 0)   
                    else:
                        continue   
                    
                    term_tf = freqi[index.index(term)]  
                    score += tf_idf_weight * term_tf   
                
                except (IndexError, KeyError):
                    print(f"Skipping term '{term}' in document {doc['_id']} due to access error.")
                    continue
        
        if score > 0:
            results.append({
                "document_text": doc["original_text"],
                "score": score,
                "document_title" : doc["document_title"]
            })
    
    results.sort(key=lambda x: x["score"], reverse=True)
    
    return results

# # Example
# term_list = ["covid-19", "covid-19","print"]
# ranked_docs = retrieve_and_rank_docs(term_list)

# # Display the ranked documents
# if ranked_docs:
#     for idx, doc in enumerate(ranked_docs):
#         print(f"Rank {idx + 1}:")
#         print(f"Score: {doc['score']}")
#         print(f"Document: {doc['document_text']}\n")
# else:
#     print("No relevant documents found.")
