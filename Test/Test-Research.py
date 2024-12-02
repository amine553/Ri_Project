import pymongo

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
db = client["Ri_Project"]  # Use the database
collection_db = db["Collection"]  # Use the collection

def retrieve_and_rank_docs(term_list):

    results = []  # Store documents and their scores
    
    # Query all documents from the collection
    documents = collection_db.find()  
    
    # Iterate through documents
    for doc in documents:
        index = doc["index"]
        weights = doc["weights"]
        score = 0  # Initialize the document's score
        for term in term_list:
            if term in index:
                term_index = index.index(term) 
                
                try:
               
                    if isinstance(weights, list):
                        tf_idf_weight = weights[term_index]   
                    elif isinstance(weights, dict):
                        tf_idf_weight = weights.get(term, 0)   
                    else:
                        continue   
                    
                    term_tf = term_list.count(term)  
                    score += tf_idf_weight * term_tf   
                
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

# Example Usage
term_list = ["covid-19",'empire']
ranked_docs = retrieve_and_rank_docs(term_list)

# Display the ranked documents
if len(ranked_docs) > 0 :
    for i,doc in enumerate(ranked_docs):
        print("*******************----------------------------------*******************************************")
        i = i + 1 
        print(f"Document {i}: {doc['document_text']}\n")
else :
    print("no docs correspandant to the query")


