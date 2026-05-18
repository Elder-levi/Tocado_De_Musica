import time
from threading import Thread, Lock
import sys

lock = Lock()


def animacao_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animacao_text(lyric, speed)


def sing_song():

    lyrics = [
        ("\nDe onde eu venho, a maioria é preto", 0.06),
        ("E a minoria também é", 0.06),
        ("Eu sou o negro lindo que você quer", 0.05),
        ("É, é, é...", 0.08),

        ("\nE quando me vê passa mal", 0.06),
        ("Lindo, maravilhoso, sensual", 0.05),
        ("Daquele jeito que você gosta", 0.06),
        ("Balança a cabeça e não diz não, dá a resposta", 0.05),

        ("\nSou negão, sou negão, sou negão", 0.07),
        ("Tenho orgulho da minha cor", 0.07),
        ("Sou eu, o negro lindo que você quer", 0.06),
        ("Sou o seu amor", 0.07),

        ("\nLute, minha raça, lute", 0.06),
        ("Não deixe o preconceito te abalar", 0.06),
        ("Mostre a sua força, o seu valor", 0.06),
        ("O negro é lindo, sim senhor!", 0.05)
    ]

    delays = [
        0.5, 3.2, 5.8, 9.0,  # Bloco 1 (Introdução/Verso)
        12.2, 14.8, 17.5, 20.1,  # Bloco 2 (Pre-refrão)
        24.0, 26.5, 29.2, 32.0,  # Bloco 3 (Refrão)
        36.5, 39.2, 42.0, 44.8  # Bloco 4 (Mensagem/Luta)
    ]

    threads = []

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]

        t = Thread(
            target=sing_lyric,
            args=(lyric, delays[i], speed)
        )

        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    sing_song()