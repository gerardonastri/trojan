import os


def run(**args):  # elenca tutti i file presente nella cartella corrente
    print("[*] In dirlister module.")
    files = os.listdir('.')
    return str(files)
