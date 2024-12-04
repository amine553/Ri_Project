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
    search_terms = None
    if request.method == "POST":
        search_terms = request.form.get('search_terms', None)
        if search_terms:
            ranked_docs = retrieve_and_rank_docs(search_terms)
    return render_template("index.html", ranked_docs=ranked_docs, search_terms=search_terms)


if __name__ == "__main__":
    app.run(debug=True)

