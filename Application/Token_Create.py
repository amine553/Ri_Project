import unicodedata

class Tkn:
    
    def __init__(self):
        pass
    
    def TokenSpace(self, Docs):
        # Tokenize the text by spaces
        return Docs.split()  
    
    def Token_Charectre(self, word_list):
        # Remove non-alphanumeric characters from each word
        return [''.join(ch for ch in word if ch.isalnum()) for word in word_list]
    
    def LowerCaseDocs(self, word_list):
        # Convert all words to lowercase
        return [element.lower() for element in word_list]
    
    def remove_accents(self, word):
        # Normalize the word to remove accents
        nfkd_form = unicodedata.normalize('NFKD', word)
        return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    def resultfrom_remove(self, word_list):
        # Apply the accent removal function to each word in the list
        return [self.remove_accents(word) for word in word_list]

    def FinalTokens(self, text):
        # Chaining methods properly using self
        tokens = self.TokenSpace(text)
        tokens = self.Token_Charectre(tokens)
        tokens = self.LowerCaseDocs(tokens)
        tokens = self.resultfrom_remove(tokens)
        
        # Remove any empty strings from the list
        tokens = [word for word in tokens if word != "" and word != '']
        
        print(tokens)
        return tokens



        
       