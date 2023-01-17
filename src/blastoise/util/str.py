"""String utils."""

def remove_head(sentence, remove_word):
    """Remove the word in the sentence.
    
        Args:
            sentence (str): sentence
            remove_word (str): remove word
        Return: str
    """
    if sentence is None or remove_word is None:
        return None
    return sentence.replace(f'{remove_word}.', '')
    