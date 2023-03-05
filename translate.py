import googletrans
from time import sleep

frase = "Grunus, O Goblin"
"""
idiomas = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs",
           "bg", "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", "cs",
           "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl",
           "ka", "de", "el", "gu", "ht", "ha", "haw", "iw", "he", "hi",
           "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn",
           "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb",
           "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne",
           "no", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm",
           "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es",
           "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur",
           "ug", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]
"""
idiomas = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs"]
trad = dict()

for idioma in idiomas:
    trans = googletrans.Translator()
    try:
        guardar = trans.translate(frase, dest=idioma).text
    except:
        print(ValueError())
    else:
        trad[googletrans.LANGUAGES[idioma]] = trans.translate(frase, dest=idioma).text


print(trad)

"""
for chave in googletrans.LANGUAGES.keys():
    print(f"{googletrans.LANGUAGES[chave]}: {trans.translate(frase, dest=chave).text}")
    print(f"{chave} ==> {googletrans.LANGUAGES[chave]}")

texto = "Grunus, O Goblin"
translator = Translator()
acquirer = TokenAcquirer()
acquirer.do(texto)
texto_pt = translator.translate(texto, src="pt", dest="en")
print(texto_pt.text)
texto = Translator()
texto.translate(frase, dest='en')
print(texto)

for keys in googletrans.LANGUAGES:
    print(f"{keys} - {googletrans.LANGUAGES[keys]}")
"""