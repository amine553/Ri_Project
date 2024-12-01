import unicodedata

class Tkn:
    
    def __init__(self):
        pass
    
    def TokenSpace(self, Docs):
        # Tokenize the text by spaces
        return Docs.split()
    
    def Token_Charectre(self, word_list):
        # Allow alphanumeric tokens with hyphens or apostrophes
        processed_tokens = []
        for word in word_list:
            # Check if the word is a valid hyphenated word (like covid-19)
            if '-' in word and all(ch.isalnum() or ch == '-' for ch in word):
                processed_tokens.append(word)
            # Special handling for words with apostrophes (like l'ageration)
            elif "'" in word:
                # Split on the apostrophe and keep the parts separately
                processed_tokens.extend(word.split("'"))
            else:
                processed_tokens.append(word)
        
        # Clean up tokens by removing non-alphanumeric characters except hyphens
        return [''.join(ch for ch in token if ch.isalnum() or ch == '-') for token in processed_tokens]
    
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
    
    def RemovePureNumbers(self, word_list):
        # Remove tokens that are purely numeric but keep alphanumeric combinations
        return [word for word in word_list if not word.isdigit()]
    
    def FinalTokens(self, text):
        # Chaining methods properly using self
        tokens = self.TokenSpace(text)
        tokens = self.Token_Charectre(tokens)
        tokens = self.LowerCaseDocs(tokens)
        tokens = self.resultfrom_remove(tokens)
        tokens = self.RemovePureNumbers(tokens)
        
        # Remove any single character tokens
        tokens = [word for word in tokens if len(word) > 1]
        
        # Remove any empty strings from the list
        tokens = [word for word in tokens if word != ""]

        return tokens 