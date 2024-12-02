import pymongo

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
db = client["Ri_Project"]  # Use the database
collection_db = db["Collection"]  # Use the collection

def retrieve_and_rank_docs(term_list):
    """
    Retrieve documents based on a list of terms, calculate a score for each, and rank them.
    
    :param term_list: List of terms to base the retrieval on.
    :return: Sorted list of documents and their scores.
    """
    results = []  # Store documents and their scores
    
    # Query all documents from the collection
    documents = collection_db.find()  
    
    # Iterate through documents
    for doc in documents:
        index = doc["index"]
        weights = doc["weights"]
        score = 0  # Initialize the document's score
        
        # # Ensure that weights is accessible correctly
        # if isinstance(weights, list):
        #     if len(index) != len(weights):
        #         # print(f"Skipping document with ID {doc['_id']} due to mismatched lengths.")
        #         continue
        # elif isinstance(weights, dict):
        #     # print(f"Document with ID {doc['_id']} has weights as a dictionary.")
        # else:
        #     # print(f"Skipping document with ID {doc['_id']} due to unknown weights structure.")
        #     continue
        
        # Calculate the score for the current document
        for term in term_list:
            if term in index:
                term_index = index.index(term)  # Get the term's index position
                
                try:
                    # Access weights based on its structure
                    if isinstance(weights, list):
                        tf_idf_weight = weights[term_index]  # List-based access
                    elif isinstance(weights, dict):
                        tf_idf_weight = weights.get(term, 0)  # Dictionary-based access
                    else:
                        continue  # Skip if weights structure is not supported
                    
                    term_tf = term_list.count(term)  # Frequency of the term in the input list (TF)
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

# Example Usage
term_list = ["bus","covid-19"]
ranked_docs = retrieve_and_rank_docs(term_list)

# Display the ranked documents
for i,doc in enumerate(ranked_docs):
   print("*******************----------------------------------*******************************************")
   i = i + 1 
   print(f"Document {i}: {doc['document_text']}\n")


