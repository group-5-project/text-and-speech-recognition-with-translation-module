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


class TranslatorApp(MDApp):
    def build(self):
        path = "../Fonts"
        font = path + "/NotoSans-Regular.ttf"

        self.change_font(font)
        return

    def get_usertext(self):
        self.root.ids.language1.text = detect(self.root.ids.usertext1.text)

    def dropdown1(self):
        self.myitems = {'ab': 'Abkhaz', 'aa': 'Afar', 'af': 'Afrikaans', 'ak': 'Akan', 'sq': 'Albanian',
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
        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": list(self.myitems.values())[i],
                "on_release": lambda x=list(self.myitems.keys())[i]: self.set_item1(x),
            } for i in range(184)
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.language1,
            items=self.menu_list,
            width_mult=4
        )
        self.menu.open()

    def dropdown2(self):
        self.myitems = {'hi': 'Hindi', 'ab': 'Abkhaz', 'aa': 'Afar', 'af': 'Afrikaans', 'ak': 'Akan', 'sq': 'Albanian',
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
                        'ho': 'Hiri Motu', 'hu': 'Hungarian', 'ia': 'Interlingua', 'id': 'Indonesian',
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
        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": list(self.myitems.values())[i],
                "on_release": lambda x=list(self.myitems.keys())[i]: self.set_item2(x),
            } for i in range(184)
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.language2,
            items=self.menu_list,
            width_mult=4
        )
        self.menu.open()

    def change_font(self, font):
        self.root.ids.usertext1.font_name = font
        self.root.ids.usertext2.font_name = font

    def updateIcon(self, newIcon):
        self.ids.iconButton.icon = newIcon

    def set_item1(self, text):
        self.root.ids.language1.text = text
        self.menu.dismiss()

        print("Language1 selected: ", text)

        path = "../Fonts"
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
        self.root.ids.usertext2.text = ts.google(self.root.ids.usertext1.text,
                                                 from_language=self.root.ids.language1.text, to_language=value)
        print(self.root.ids.usertext2.text)

    def speak(self):
        mytext = self.root.ids.usertext2.text
        myobj = gTTS(text=mytext, lang=self.root.ids.language2.text, slow=False)

        temp_filename = 'test.mp3'
        myobj.save(temp_filename)
        playsound(temp_filename)
        os.remove(temp_filename)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
        try:
            txt = r.recognize_google(audio, language=self.root.ids.language1.text)
            self.root.ids.usertext1.text = txt
        except:
            # self.root.ids.usertext1.text = "Could not understand audio!"
            messagebox.showerror("Error Encountered", "Could not understand audio!")

    def readtxt(self):
        filetypes = (
            ('image files', '*.jpg'), ('image files', '*.png'), ('image files', '*.jpeg'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)

        selectedlang = self.root.ids.language1.text

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

                text = ''
                for result in results:
                    text += result[1] + ''

                self.root.ids.usertext1.text = text

            except:
                print("Invalid Path selected or Something went wrong")
                # messagebox.showerror("Invalid Path selected or Something went wrong")

        else:
            # print("Either Language is not Supported or User did not selected any Language")
            messagebox.showerror("Error Encountered", "Doesn't Support this Language")

    def swap_lang(self):
        temp = self.root.ids.language2.text
        self.root.ids.language2.text = self.root.ids.language1.text
        self.root.ids.language1.text = temp
        temp = self.root.ids.usertext2.text
        self.root.ids.usertext2.text = self.root.ids.usertext1.text
        self.root.ids.usertext1.text = temp


TranslatorApp().run()
