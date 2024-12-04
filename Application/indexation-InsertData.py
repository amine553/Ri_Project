import pymongo
from Token_Create import Tkn
from Other_Fun import Other_fun
import os
from math import log
 
client = pymongo.MongoClient("mongodb://localhost:27017/")   
db = client["Ri_Project"]   
collection_db = db["Collection"]   

folder_path = r'Collection_TIME'
collection = []
filenames = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
   
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            # Read the content of the file and add it to the collection list
            collection.append(file.read().strip())
            filenames.append(os.path.splitext(filename)[0]+".html")  # Store the filename

Tokeniser = Tkn()
FunApp = Other_fun()
index = []
freqi = []
Dict1 = []

for Di in collection:
    indexDi = []
    freqiDi = []
    Tokens = Tokeniser.FinalTokens(Di)
    
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
    
    Dict1.append(dict(zip(indexDi, freqiDi)))
    index.append(indexDi)
    freqi.append(freqiDi)

IDF_D = {}
for idx_list in index:
    terms_set = set(idx_list)
    for term in terms_set:
        if term not in IDF_D:
            IDF_D[term] = 1
        else:
            IDF_D[term] += 1
for key in IDF_D:
    IDF_D[key] = log(len(index) / IDF_D[key], 10)

Wi = []
for tf_dict in Dict1:
    wi_dict = FunApp.compute_tf_idf(tf_dict, IDF_D)
    Wi.append(wi_dict)

for doc_idx, doc in enumerate(collection):
    document = {
        "document_title": filenames[doc_idx],
        "original_text": doc,
        "index": index[doc_idx],
        "weights": Wi[doc_idx]
    }
    collection_db.insert_one(document)

print("Data has been successfully stored in MongoDB!")

#! ((((((((((((((((((((((((((((((((((((((((((((((((((((((((create HTML FILES))))))))))))))))))))))))))))))))))))))))))))))))))))))))

input_directory = "Collection_Time"
output_directory = "Application/static/Generated_HTML"

os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_directory, filename)
        with open(input_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        file_title = os.path.splitext(filename)[0]   
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{file_title}</title>
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f8f9fa;
        }}
        h1 {{
            color: #007bff;
            font-size: 2.5rem;
        }}
        p {{
            white-space: pre-wrap; /* Preserve line breaks in text */
            font-size: 1.1rem;
            color: #333;
        }}
        .container {{
            max-width: 800px;
            margin: 40px auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
    </style>
</head>
<body>
    <div class="container">
        <center><h1>{file_title}</h1></center>
        <p>{content}</p>
    </div>
</body>
</html>
"""

        
        # Write the HTML content to a new file
        output_file_path = os.path.join(output_directory, f"{file_title}.html")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(html_content)

print("HTML files have been generated successfully.")