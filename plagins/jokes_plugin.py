import pyjokes


def get_joke():
    return pyjokes.get_joke(language="ru", category="all")