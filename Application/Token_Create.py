import unicodedata

class Tkn:
    
    def __init__(self):
        pass
    
    def TokenSpace(self, Docs):
        return Docs.split()
    
    def Token_Charectre(self, word_list):
        processed_tokens = []
        for word in word_list:
            if '-' in word and all(ch.isalnum() or ch == '-' for ch in word):
                processed_tokens.append(word)
            elif "'" in word:
                processed_tokens.extend(word.split("'"))
            else:
                processed_tokens.append(word)
        
        return [''.join(ch for ch in token if ch.isalnum() or ch == '-') for token in processed_tokens]
    
    def LowerCaseDocs(self, word_list):
        return [element.lower() for element in word_list]
    
    def remove_accents(self, word):
        nfkd_form = unicodedata.normalize('NFKD', word)
        return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    def resultfrom_remove(self, word_list):
        return [self.remove_accents(word) for word in word_list]
    
    def RemovePureNumbers(self, word_list):
        return [word for word in word_list if not word.isdigit()]
    
    def FinalTokens(self, text):
        # Chaining methods properly using self
        tokens = self.TokenSpace(text)
        tokens = self.Token_Charectre(tokens)
        tokens = self.LowerCaseDocs(tokens)
        tokens = self.resultfrom_remove(tokens)
        tokens = self.RemovePureNumbers(tokens)
        
        tokens = [word for word in tokens if len(word) > 1]
        
        tokens = [word for word in tokens if word != ""]

        return tokens 