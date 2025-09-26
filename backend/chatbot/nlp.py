from googletrans import Translator

translator = Translator()

def detect_and_translate(text):
    lang = translator.detect(text).lang
    translated = translator.translate(text, src=lang, dest="en").text
    return lang, translated

def translate_to_lang(text, lang):
    if lang == "en":
        return text
    return translator.translate(text, src="en", dest=lang).text
