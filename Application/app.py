from flask import Flask, render_template, request
import json
from Search_Algo import retrieve_and_rank_docs
# Assuming the MongoDB collection and the necessary functions (e.g., Tokeniser, FunApp) are already set up.
# Replace this with your actual import or initialization code for MongoDB and other components
# from your_module import retrieve_and_rank_docs, Tokeniser, FunApp, collection_db

app = Flask(__name__)

# This function is assumed to already be defined in your code
# def retrieve_and_rank_docs(term_list):
#     # Your existing function implementation...

@app.route("/", methods=["GET", "POST"])
def index():
    ranked_docs = []
    if request.method == "POST":
        # Get the input from the form (a single string)
        user_input = request.form['search_terms']
        
        # Call the retrieve_and_rank_docs function with the string directly
        ranked_docs = retrieve_and_rank_docs(user_input)

    return render_template("index.html", ranked_docs=ranked_docs)

if __name__ == "__main__":
    app.run(debug=True)

