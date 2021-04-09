from googletrans import Translator, LANGUAGES

translator = Translator()

def translate(string):
    # on the list of things to fix in this clusterfuck of a code :(
    if ":" in string:
        # translating to another language or translating between languages
        l = string.split(":")
        string = l[1].strip()
        if len(l[0].split())>1:
            (slang, dlang) = l[0].strip().split()
        else: 
            slang, dlang = "en", l[0].strip()
        if dlang not in LANGUAGES or slang not in LANGUAGES:
            return("Please enter valid languages!")
        results = translator.translate(string, dest=dlang, src=slang)

    else: 
        results = translator.translate(string)
    return(results.text, results.src, results.dest)