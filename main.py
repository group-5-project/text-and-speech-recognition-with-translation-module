from kivymd.app import MDApp
from langdetect import detect
import translators as ts
from kivymd.uix.menu import MDDropdownMenu

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from tkinter import filedialog as fd
from tkinter import messagebox

import easyocr
import os


class TextHandler():
    str = 'Enter Text:'

    def detector(self, str):
        return detect(str)


class Translator():
    translated_text = ''

    def translator(self, txt, lang1, lang2):
        if lang1 == "Detected Language" or lang2 == "Select Language":
            return " "

        return ts.google(txt, from_language=lang1, to_language=lang2)


class languageManager():
    def input_language(self):
        myitems = {'ab': 'Abkhaz', 'aa': 'Afar', 'af': 'Afrikaans', 'ak': 'Akan', 'sq': 'Albanian',
                   'am': 'Amharic', 'ar': 'Arabic', 'an': 'Aragonese', 'hy': 'Armenian', 'as': 'Assamese',
                   'av': 'Avaric', 'ae': 'Avestan', 'ay': 'Aymara', 'az': 'Azerbaijani', 'bm': 'Bambara',
                   'ba': 'Bashkir', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bh': 'Bihari',
                   'bi': 'Bislama', 'bs': 'Bosnian', 'br': 'Breton', 'bg': 'Bulgarian', 'my': 'Burmese',
                   'ca': 'Catalan; Valencian', 'ch': 'Chamorro', 'ce': 'Chechen', 'ny': 'Chichewa; Chewa; Nyanja',
                   'zh': 'Chinese', 'cv': 'Chuvash', 'kw': 'Cornish', 'co': 'Corsican', 'cr': 'Cree',
                   'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'dv': 'Divehi; Maldivian;', 'nl': 'Dutch',
                   'dz': 'Dzongkha', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'ee': 'Ewe',
                   'fo': 'Faroese', 'fj': 'Fijian', 'fi': 'Finnish', 'fr': 'French', 'ff': 'Fula',
                   'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gn': 'Guaraní',
                   'gu': 'Gujarati', 'ht': 'Haitian', 'ha': 'Hausa', 'he': 'Hebrew modern', 'hz': 'Herero',
                   'hi': 'Hindi', 'ho': 'Hiri Motu', 'hu': 'Hungarian', 'ia': 'Interlingua', 'id': 'Indonesian',
                   'ie': 'Interlingue', 'ga': 'Irish', 'ig': 'Igbo', 'ik': 'Inupiaq', 'io': 'Ido',
                   'is': 'Icelandic', 'it': 'Italian', 'iu': 'Inuktitut', 'ja': 'Japanese', 'jv': 'Javanese',
                   'kl': 'Kalaallisut', 'kn': 'Kannada', 'kr': 'Kanuri', 'ks': 'Kashmiri', 'kk': 'Kazakh',
                   'km': 'Khmer', 'ki': 'Kikuyu: Gikuyu', 'rw': 'Kinyarwanda', 'ky': 'Kirghiz: Kyrgyz',
                   'kv': 'Komi', 'kg': 'Kongo', 'ko': 'Korean', 'ku': 'Kurdish', 'kj': 'Kwanyama: Kuanyama',
                   'la': 'Latin', 'lb': 'Luxembourgish', 'lg': 'Luganda', 'li': 'Limburgish', 'ln': 'Lingala',
                   'lo': 'Lao', 'lt': 'Lithuanian', 'lu': 'Luba-Katanga', 'lv': 'Latvian', 'gv': 'Manx',
                   'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese',
                   'mi': 'Māori', 'mr': 'Marathi Marāṭhī', 'mh': 'Marshallese', 'mn': 'Mongolian', 'na': 'Nauru',
                   'nv': 'Navajo: Navaho', 'nb': 'Norwegian Bokmål', 'nd': 'North Ndebele', 'ne': 'Nepali',
                   'ng': 'Ndonga', 'nn': 'Norwegian Nynorsk', 'no': 'Norwegian', 'ii': 'Nuosu',
                   'nr': 'South Ndebele', 'oc': 'Occitan', 'oj': 'Ojibwe: Ojibwa', 'cu': 'Old Church Slavonic',
                   'om': 'Oromo', 'or': 'Oriya', 'os': 'Ossetian: Ossetic', 'pa': 'Panjabi: Punjabi', 'pi': 'Pāli',
                   'fa': 'Persian', 'pl': 'Polish', 'ps': 'Pashto: Pushto', 'pt': 'Portuguese', 'qu': 'Quechua',
                   'rm': 'Romansh', 'rn': 'Kirundi', 'ro': 'Romanian: Moldavan', 'ru': 'Russian',
                   'sa': 'Sanskrit Saṁskṛta', 'sc': 'Sardinian', 'sd': 'Sindhi', 'se': 'Northern Sami',
                   'sm': 'Samoan', 'sg': 'Sango', 'sr': 'Serbian', 'gd': 'Scottish Gaelic', 'sn': 'Shona',
                   'si': 'Sinhala: Sinhalese', 'sk': 'Slovak', 'sl': 'Slovene', 'so': 'Somali',
                   'st': 'Southern Sotho', 'es': 'Spanish; Castilian', 'su': 'Sundanese', 'sw': 'Swahili',
                   'ss': 'Swati', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 'tg': 'Tajik', 'th': 'Thai',
                   'ti': 'Tigrinya', 'bo': 'Tibetan', 'tk': 'Turkmen', 'tl': 'Tagalog', 'tn': 'Tswana',
                   'to': 'Tonga', 'tr': 'Turkish', 'ts': 'Tsonga', 'tt': 'Tatar', 'tw': 'Twi', 'ty': 'Tahitian',
                   'ug': 'Uighur: Uyghur', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 've': 'Venda',
                   'vi': 'Vietnamese', 'vo': 'Volapük', 'wa': 'Walloon', 'cy': 'Welsh', 'wo': 'Wolof',
                   'fy': 'Western Frisian', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'za': 'Zhuang: Chuang',
                   'zu': 'Zulu'}
        return myitems

    def output_language(self):
        myitems = {'ab': 'Abkhaz', 'aa': 'Afar', 'af': 'Afrikaans', 'ak': 'Akan', 'sq': 'Albanian',
                   'am': 'Amharic', 'ar': 'Arabic', 'an': 'Aragonese', 'hy': 'Armenian', 'as': 'Assamese',
                   'av': 'Avaric', 'ae': 'Avestan', 'ay': 'Aymara', 'az': 'Azerbaijani', 'bm': 'Bambara',
                   'ba': 'Bashkir', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bh': 'Bihari',
                   'bi': 'Bislama', 'bs': 'Bosnian', 'br': 'Breton', 'bg': 'Bulgarian', 'my': 'Burmese',
                   'ca': 'Catalan; Valencian', 'ch': 'Chamorro', 'ce': 'Chechen', 'ny': 'Chichewa; Chewa; Nyanja',
                   'zh': 'Chinese', 'cv': 'Chuvash', 'kw': 'Cornish', 'co': 'Corsican', 'cr': 'Cree',
                   'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'dv': 'Divehi; Maldivian;', 'nl': 'Dutch',
                   'dz': 'Dzongkha', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'ee': 'Ewe',
                   'fo': 'Faroese', 'fj': 'Fijian', 'fi': 'Finnish', 'fr': 'French', 'ff': 'Fula',
                   'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gn': 'Guaraní',
                   'gu': 'Gujarati', 'ht': 'Haitian', 'ha': 'Hausa', 'he': 'Hebrew modern', 'hz': 'Herero',
                   'hi': 'Hindi', 'ho': 'Hiri Motu', 'hu': 'Hungarian', 'ia': 'Interlingua', 'id': 'Indonesian',
                   'ie': 'Interlingue', 'ga': 'Irish', 'ig': 'Igbo', 'ik': 'Inupiaq', 'io': 'Ido',
                   'is': 'Icelandic', 'it': 'Italian', 'iu': 'Inuktitut', 'ja': 'Japanese', 'jv': 'Javanese',
                   'kl': 'Kalaallisut', 'kn': 'Kannada', 'kr': 'Kanuri', 'ks': 'Kashmiri', 'kk': 'Kazakh',
                   'km': 'Khmer', 'ki': 'Kikuyu: Gikuyu', 'rw': 'Kinyarwanda', 'ky': 'Kirghiz: Kyrgyz',
                   'kv': 'Komi', 'kg': 'Kongo', 'ko': 'Korean', 'ku': 'Kurdish', 'kj': 'Kwanyama: Kuanyama',
                   'la': 'Latin', 'lb': 'Luxembourgish', 'lg': 'Luganda', 'li': 'Limburgish', 'ln': 'Lingala',
                   'lo': 'Lao', 'lt': 'Lithuanian', 'lu': 'Luba-Katanga', 'lv': 'Latvian', 'gv': 'Manx',
                   'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese',
                   'mi': 'Māori', 'mr': 'Marathi Marāṭhī', 'mh': 'Marshallese', 'mn': 'Mongolian', 'na': 'Nauru',
                   'nv': 'Navajo: Navaho', 'nb': 'Norwegian Bokmål', 'nd': 'North Ndebele', 'ne': 'Nepali',
                   'ng': 'Ndonga', 'nn': 'Norwegian Nynorsk', 'no': 'Norwegian', 'ii': 'Nuosu',
                   'nr': 'South Ndebele', 'oc': 'Occitan', 'oj': 'Ojibwe: Ojibwa', 'cu': 'Old Church Slavonic',
                   'om': 'Oromo', 'or': 'Oriya', 'os': 'Ossetian: Ossetic', 'pa': 'Panjabi: Punjabi', 'pi': 'Pāli',
                   'fa': 'Persian', 'pl': 'Polish', 'ps': 'Pashto: Pushto', 'pt': 'Portuguese', 'qu': 'Quechua',
                   'rm': 'Romansh', 'rn': 'Kirundi', 'ro': 'Romanian: Moldavan', 'ru': 'Russian',
                   'sa': 'Sanskrit Saṁskṛta', 'sc': 'Sardinian', 'sd': 'Sindhi', 'se': 'Northern Sami',
                   'sm': 'Samoan', 'sg': 'Sango', 'sr': 'Serbian', 'gd': 'Scottish Gaelic', 'sn': 'Shona',
                   'si': 'Sinhala: Sinhalese', 'sk': 'Slovak', 'sl': 'Slovene', 'so': 'Somali',
                   'st': 'Southern Sotho', 'es': 'Spanish; Castilian', 'su': 'Sundanese', 'sw': 'Swahili',
                   'ss': 'Swati', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 'tg': 'Tajik', 'th': 'Thai',
                   'ti': 'Tigrinya', 'bo': 'Tibetan', 'tk': 'Turkmen', 'tl': 'Tagalog', 'tn': 'Tswana',
                   'to': 'Tonga', 'tr': 'Turkish', 'ts': 'Tsonga', 'tt': 'Tatar', 'tw': 'Twi', 'ty': 'Tahitian',
                   'ug': 'Uighur: Uyghur', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 've': 'Venda',
                   'vi': 'Vietnamese', 'vo': 'Volapük', 'wa': 'Walloon', 'cy': 'Welsh', 'wo': 'Wolof',
                   'fy': 'Western Frisian', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'za': 'Zhuang: Chuang',
                   'zu': 'Zulu'}
        return myitems


class SpeechRecognizer():
    speech = sr.Recognizer()
    text = ''

    def recordSpeech(self):
        print("Listening")

        with sr.Microphone() as source:
            self.speech.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.speech.record(source, duration=4)

        print("Finalizing")
        return audio

    def recognizeText(self, lang):
        try:
            self.text = self.speech.recognize_google(self.recordSpeech(), language=lang)
        except:
            messagebox.showerror("Error Encountered", "Could not understand audio!")
            return self.text
        return self.text


class OpticalCharacterRecognizer():
    text = ''

    def captureImage(self, selectedlang):
        filetypes = (
            ('image files', '*.jpg'), ('image files', '*.png'), ('image files', '*.jpeg'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        supportedlanglist = ['abq', 'ady', 'af', 'ang', 'ar', 'as', 'ava', 'az', 'be', 'bg', 'bh', 'bho', 'bn', 'bs',
                             'ch_sim', 'ch_tra', 'che', 'cs', 'cy', 'da', 'dar', 'de', 'en', 'es', 'et', 'fa', 'fr',
                             'ga', 'gom', 'hi', 'hr', 'hu', 'id', 'inh', 'is', 'it', 'ja', 'kbd', 'kn', 'ko', 'ku',
                             'la', 'lbe', 'lez', 'lt', 'lv', 'mah', 'mai', 'mi', 'mn', 'mr', 'ms', 'mt', 'ne', 'new',
                             'nl', 'no', 'oc', 'pi', 'pl', 'pt', 'ro', 'ru', 'rs_cyrillic', 'rs_latin', 'sck', 'sk',
                             'sl', 'sq', 'sv', 'sw', 'ta', 'tab', 'te', 'th', 'tjk', 'tl', 'tr', 'ug', 'uk', 'ur', 'uz',
                             'vi']

        if selectedlang in supportedlanglist:
            try:
                reader = easyocr.Reader([selectedlang], gpu=False)
                results = reader.readtext(filename)
                for result in results:
                    self.text += result[1] + ''
                return self.text

            except:
                print("Invalid Path selected or Something went wrong")
                # messagebox.showerror("Invalid Path selected or Something went wrong")

        else:
            # print("Either Language is not Supported or User did not selected any Language")
            messagebox.showerror("Error Encountered", "Doesn't Support this Language")


class User(MDApp):
    def build(self):
        path = "Fonts"
        font = path + "/NotoSans-Regular.ttf"

        self.change_font(font)
        return

    def change_font(self, font):
        self.root.ids.usertext1.font_name = font
        self.root.ids.usertext2.font_name = font

    def returnText(self):
        txt_handler = TextHandler()
        self.root.ids.language1.text = txt_handler.detector(self.root.ids.usertext1.text)

    def dropdown1(self):
        langMan = languageManager()

        menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": list(langMan.input_language().values())[i],
                "on_release": lambda x=list(langMan.input_language().keys())[i]: self.set_item1(x),
            } for i in range(184)
        ]

        self.menu = MDDropdownMenu(
            caller=self.root.ids.language1,
            items=menu_list,
            width_mult=4
        )
        self.menu.open()

    def set_item1(self, text):
        self.root.ids.language1.text = text
        self.menu.dismiss()

    def dropdown2(self):
        langMan = languageManager()

        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": list(langMan.output_language().values())[i],
                "on_release": lambda x=list(langMan.output_language().keys())[i]: self.set_item2(x),
            } for i in range(184)
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.language2,
            items=self.menu_list,
            width_mult=4
        )
        self.menu.open()

    def set_item1(self, text):
        self.root.ids.language1.text = text
        self.menu.dismiss()

        path = "Fonts"

        font = path + "/NotoSans-Regular.ttf"

        if text == 'zh':
            font = path + "/NotoSansSC-Regular.otf"
        elif text == 'ja':
            font = path + "/NotoSansJP-Regular.otf"
        elif text == 'ar':
            font = path + "/NotoSansArabic-Regular.ttf"
        elif text == 'ko':
            font = path + "/NotoSansKR-Regular.otf"
        elif text == 'ta':
            font = path + "/NotoSansTamil-Regular.ttf"

        self.root.ids.usertext1.font_name = font

    def set_item2(self, text):
        self.root.ids.language2.text = text
        self.menu.dismiss()

        font = "Fonts/NotoSans-Regular.ttf"

        if text == 'zh':
            font = "Fonts/NotoSansSC-Regular.ttf"
        elif text == 'ja':
            font = "Fonts/NotoSansJP-Regular.otf"
        elif text == 'ar':
            font = "Fonts/NotoSansArabic-Regular.ttf"
        elif text == 'ko':
            font = "Fonts/NotoSansKR-Regular.otf"
        elif text == 'ta':
            font = "Fonts/NotoSansTamil-Regular.otf"

        self.root.ids.usertext2.text = ""
        self.root.ids.usertext2.font_name = font

    def translate_text(self, value):
        translator = Translator()
        self.root.ids.usertext2.text = translator.translator(self.root.ids.usertext1.text,
                                                             self.root.ids.language1.text, value)

    def speak(self):
        mytext = self.root.ids.usertext2.text
        myobj = gTTS(text=mytext, lang=self.root.ids.language2.text, slow=False)
        temp_filename = 'test.mp3'
        myobj.save(temp_filename)
        playsound(temp_filename)
        os.remove(temp_filename)

    def listen(self):
        speech_recognizer = SpeechRecognizer()
        self.root.ids.usertext1.text = speech_recognizer.recognizeText(self.root.ids.language1.text)

    def readtxt(self):
        ocr = OpticalCharacterRecognizer()
        self.root.ids.usertext1.text = ocr.captureImage(self.root.ids.language1.text)

    def swap_lang(self):
        temp_font1 = self.root.ids.usertext1.font_name
        temp_font2 = self.root.ids.usertext2.font_name

        self.root.ids.usertext2.font_name = temp_font1
        self.root.ids.usertext1.font_name = temp_font2

        temp = self.root.ids.language2.text
        self.root.ids.language2.text = self.root.ids.language1.text
        self.root.ids.language1.text = temp

        temp = self.root.ids.usertext2.text
        self.root.ids.usertext2.text = self.root.ids.usertext1.text
        self.root.ids.usertext1.text = temp


User().run()
