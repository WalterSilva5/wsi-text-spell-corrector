import spacy
import hunspell

class NLPProcessor:
    def __init__(self, model_name: str, dictionary_path: str, aff_path: str):
        self.nlp = self.load_nlp_model(model_name)
        self.hobj = self.load_hunspell(dictionary_path, aff_path)

    def load_nlp_model(self, model_name: str):
        return spacy.load(model_name)

    def load_hunspell(self, dictionary_path: str, aff_path: str):
        return hunspell.HunSpell(dictionary_path, aff_path)

    def spell_check_token(self, token: str) -> str:
        if not self.hobj.spell(token):
            suggestions = self.hobj.suggest(token)
            return suggestions[0] if suggestions else token
        return token

    def correct_text(self, text: str) -> str:
        doc = self.nlp(text)
        corrected_tokens = []
        for token in doc:
            corrected_token = self.spell_check_token(token.text)
            print(f"Original: {token.text}, Corrected: {corrected_token}")  # Debug print
            corrected_tokens.append(corrected_token)
        return ' '.join(corrected_tokens)