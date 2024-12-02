import pymongo

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
db = client["document_database"]  # Use the database
collection_db = db["document_collection"]  # Use the collection

def retrieve_and_rank_docs(term_list):
    """
    Retrieve documents based on a list of terms, calculate a score for each, and rank them.
    
    :param term_list: List of terms to base the retrieval on.
    :return: Sorted list of documents and their scores.
    """
    results = []  # Store documents and their scores
    unique_terms = set(term_list)  # Consider each term only once
    
    # Query all documents from the collection
    documents = collection_db.find()  
    
    # Iterate through documents
    for doc in documents:
        index = doc["index"]
        weights = doc["weights"]
        score = 0  # Initialize the document's score
        
        # Ensure that weights are accessible correctly
        if isinstance(weights, dict):
            for term in unique_terms:  # Iterate through unique terms only
                if term in index:
                    tf_idf_weight = weights.get(term, 0)  # Dictionary-based access
                    term_tf = term_list.count(term)  # Frequency of the term in the input list (TF)
                    score += tf_idf_weight * term_tf  # Add to the document's score
        else:
            print(f"Skipping document with ID {doc['_id']} due to unsupported weights structure.")
        
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
term_list = ["covid-19", "covid-19","algerei"]  # List can include duplicates for testing
ranked_docs = retrieve_and_rank_docs(term_list)

# Display the ranked documents
for idx, doc in enumerate(ranked_docs):
    print(f"Rank {idx + 1}:")
    print(f"Score: {doc['score']}")
    print(f"Document: {doc['document_text']}\n")
