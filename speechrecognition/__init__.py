from pythonforandroid.recipe import Recipe


class SPEECHRECOGNITIONPRecipe(Recipe):
    version = "v3.8.1"
    name = "speechrecognition"

    depends: ['pyaudio']


recipe = SPEECHRECOGNITIONPRecipe()
