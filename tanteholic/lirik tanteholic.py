import time
import sys
import os

# Fungsi efek mengetik
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # ganti baris setelah selesai

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

lyrics = [
    "Oh, dengannya...",
    "Dengan dia langkahku sempurna",
    "Jatuh cinta memang manis...",
    "Apalagi ada kamu di sini",
    "Genggam tanganku sayang",
    "Kota ini tak sama tanpamu",
]

for i, line in enumerate(lyrics):

    delay = 0.1

    if   i == 3:      # baris ke-4
        delay = 0.1
    elif i == 4:    # baris ke-5
        delay = 0.08
    elif i == 5:    # baris ke-6
        delay = 0.08

    # Ketik baris
    typewriter(line, delay=delay)

    # Jeda setelah baris ke-1
    if i == 0:
        time.sleep(0.01)
    else:
        time.sleep(1)

    # Jeda setelah baris ke-2
    if i == 1:
        time.sleep(5)
    else:
        time.sleep(1)

    # Jeda setelah baris ke-3
    if i == 2:
        time.sleep(2)
    else:
        time.sleep(1)




