import pymongo
from Token_Create import Tkn
from Other_Fun import Other_fun

# MongoDB setup

def retrieve_and_rank_docs(term_list):
    client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
    db = client["Ri_Project"]  # Use the database
    collection_db = db["Collection"]  # Use the collection
    """
    Retrieve documents based on a list of terms, calculate a score for each, and rank them.
    
    :param term_list: List of terms to base the retrieval on.
    :return: Sorted list of documents and their scores.
    """
    # Tokenizer and other helper methods
    Tokeniser = Tkn()
    FunApp = Other_fun()
    term_list = Tokeniser.FinalTokens(term_list)
    index = []   # To store unique terms
    freqi = []   # To store frequencies of terms in the query

    # Tokenize and process the user query
    for Tokj in term_list:
        if not FunApp.check_Stop_List(Tokj):
            Mot = Tokj
            L = FunApp.Check_Size(Tokj)
            
            # Apply stemming and transformations based on rules
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
    
    # Now, retrieve documents from MongoDB and calculate scores
    results = []  # Store documents and their scores
    
    # Query all documents from the collection
    documents = collection_db.find()
    
    # Iterate through documents
    for doc in documents:
        doc_index = doc["index"]
        weights = doc["weights"]
        score = 0  # Initialize the document's score
        
        # Ensure that weights are accessible correctly
        if isinstance(weights, list):
            if len(doc_index) != len(weights):
                print(f"Skipping document with ID {doc['_id']} due to mismatched lengths.")
                continue
        elif isinstance(weights, dict):
            print(f"Document with ID {doc['_id']} has weights as a dictionary.")
        else:
            print(f"Skipping document with ID {doc['_id']} due to unknown weights structure.")
            continue
        
        # Calculate the score for the current document based on the query terms
        for term in index:
            if term in doc_index:
                term_index = doc_index.index(term)  # Get the term's index position
                
                try:
                    # Access weights based on its structure
                    if isinstance(weights, list):
                        tf_idf_weight = weights[term_index]  # List-based access
                    elif isinstance(weights, dict):
                        tf_idf_weight = weights.get(term, 0)  # Dictionary-based access
                    else:
                        continue  # Skip if weights structure is not supported
                    
                    term_tf = freqi[index.index(term)]  # Get term frequency from the query
                    score += tf_idf_weight * term_tf  # Add to the document's score
                
                except (IndexError, KeyError):
                    print(f"Skipping term '{term}' in document {doc['_id']} due to access error.")
                    continue
        
        # If the score is greater than 0, include the document in the results
        if score > 0:
            results.append({
                "document_text": doc["original_text"],
                "score": score
            })
    
    # Sort the results by score in descending order
    results.sort(key=lambda x: x["score"], reverse=True)
    
    return results

# # Example Usage
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
