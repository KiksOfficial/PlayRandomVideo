import tkinter as tk
import webbrowser
import random

norepeat = []


def lugu():
    global norepeat
    valik = random.randint(1, 7)

    while valik in norepeat:
        valik = random.randint(1, 7)

    norepeat.append(valik)
    if 1 in norepeat and 2 in norepeat and 3 in norepeat and 4 in norepeat and 5 in norepeat and 6 in norepeat and 7 in norepeat:
        norepeat.clear()

    if valik == 1:
        loonimi = 'watch?v=5u7jTuDBgA4'
    elif valik == 2:
        loonimi = 'watch?v=_p9WQlyVPrA'
    elif valik == 3:
        loonimi = 'watch?v=ZSgGZGt4r7Y'
    elif valik == 4:
        loonimi = 'watch?v=2l-H6eG2SsY'
    elif valik == 5:
        loonimi = 'watch?v=e0CBzwjRsY4&list=PLMpJiUztFSJ56TSlpm6S63rdt1T'
    elif valik == 6:
        loonimi = 'watch?v=UCIx07t14jw'
    elif valik == 7:
        loonimi = 'watch?v=qqPs8_Svg80'

    url = f"https://www.youtube.com/{loonimi}"
    webbrowser.open(url)
    print(valik)


muusika = tk.Tk()

btn_random = tk.Button(muusika, text='Random lugu', command=lugu)
btn_random.pack()

muusika.geometry('500x500')

muusika.mainloop()
