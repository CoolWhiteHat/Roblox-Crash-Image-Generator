
# -----------------------------------------------------------------------------
# Name: Crash image generator for Roblox
# Author: White Hat
# Description: The program generates a crash image for Roblox based on the provided screenshot.
# Requires Python and the Pillow library installed.
# All rights reserved (c) 2024 White Hat.
# 
# Note: The author is not responsible for the use of this code
# and is not responsible for its use for illegal or malicious purposes.
# ------------------------------------------------- ----------------------------
# Nazwa: Generator obrazka z crashem do Robloxa
# Autor: White Hat
# Opis: Program generuje obrazek z crashem do Robloxa na podstawie podanego screena.
#       Wymaga zainstalowanego Pythona i biblioteki Pillow.
#       Wszelkie prawa zastrzeżone (c) 2024 White Hat.
# 
# Uwaga: Autor nie ponosi odpowiedzialności za sposób użytkowania tego kodu
#        i nie odpowiada za jego użycie do niezgodnych z prawem lub złych celów.
# -----------------------------------------------------------------------------

import os
import time
from PIL import Image, ImageFilter

def add_blur_effect(input_path, temp_folder, output_file_name='blurred_image.png', blur_radius=10):
    with Image.open(input_path) as img:
        blurred_image = img.filter(ImageFilter.GaussianBlur(blur_radius))
        
        os.makedirs(temp_folder, exist_ok=True)
        
        output_path = os.path.join(temp_folder, output_file_name)
        
        blurred_image.save(output_path)

    return output_path

def paste_image_center(background_path, image_to_paste_path, output_path):
    with Image.open(background_path) as background, Image.open(image_to_paste_path) as image_to_paste:
        background_width, background_height = background.size
        paste_width, paste_height = image_to_paste.size
        x = (background_width - paste_width) // 2
        y = (background_height - paste_height) // 2
        
        background.paste(image_to_paste, (x, y), image_to_paste if image_to_paste.mode == 'RGBA' else None)
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        background.save(output_path)
        if language == 'en':
            print(f"Generated image saved in {output_path}")
        else:
            print(f"Wygenerowany obraz zapisany w {output_path}")

# Language selection
language = input("Choose your language / Wybierz język ('en' for English, 'pl' for Polish): ").lower()

if language == 'en':
    read_instructions = input("Welcome to the Roblox crash image generator! Our program generates a crash image identical to the one that appears when you are kicked out of Roblox. Please read the user manual located in the READ_ME.txt file. After reading the instructions, please type 'Y' to continue: ").lower()
else:
    read_instructions = input("Witaj w generatorze crashy do Roblox! Nasz program generuje obrazek z crashem identyczny z tym, który pojawia się, gdy zostaniesz wyrzucony z Robloxa. Przeczytaj proszę instrukcję obsługi, która znajduje się w pliku READ_ME.txt. Po zapoznaniu się z instrukcją, proszę napisz 'Y' i kontynuuj: ").lower()

while read_instructions != "y":
    if read_instructions == "n":
        if language == 'en':
            print("Please read the user manual. The program will automatically close in 5 seconds. After reading the manual, please run the program again.")
        else:
            print("Proszę zapoznaj się z instrukcją obsługi. Program zamknie się automatycznie za 5 sekund. Po przeczytaniu instrukcji obsługi uruchom program ponownie.")
        time.sleep(5)
        exit()
    else:
        if language == 'en':
            print("Invalid response. Please type 'Y' or 'N'.")
            read_instructions = input("Did you read the user manual? (Type 'Y' or 'N'): ").lower()
        else:
            print("Niepoprawna odpowiedź. Proszę wpisz 'Y' lub 'N'.")
            read_instructions = input("Czy przeczytałeś instrukcję obsługi? (Wpisz 'Y' lub 'N'): ").lower()

generator_folder = os.path.dirname(os.path.abspath(__file__))

input_image_path = os.path.join(generator_folder, 'put_here', 'enter.png')

temp_folder = os.path.join(generator_folder, 'temp')

blur_radius = 10

blurred_image_path = add_blur_effect(input_image_path, temp_folder, blur_radius=blur_radius)

valid_choices = {
    '-1': '-1.png',
    '268': '268.png',
    '277_en': '277_en.png',
    '277_pl': '277_pl.png',
    '280': '280.png',
    '531': '531.png',
    '534': '534.png'
}

if language == 'en':
    choice = input("Choose the error you want to overlay on your image ('-1', '268', '277_en', '277_pl', '280', '531', '534'): ").lower()
else:
    choice = input("Wybierz błąd jaki chcesz aby został nałożony na twoje zdjęcie ('-1', '268', '277_en', '277_pl', '280', '531', '534'): ").lower()

while choice not in valid_choices:
    if language == 'en':
        print("Invalid file choice.")
        choice = input("Choose the error you want to overlay on your image ('-1', '268', '277_en', '277_pl', '280', '531', '534'): ").lower()
    else:
        print("Niepoprawny wybór pliku do wklejenia.")
        choice = input("Wybierz błąd jaki chcesz aby został nałożony na twoje zdjęcie ('-1', '268', '277_en', '277_pl', '280', '531', '534'): ").lower()

image_to_paste_path = os.path.join(generator_folder, 'source', valid_choices[choice])

output_folder = os.path.join(generator_folder, 'finished')
final_image_path = os.path.join(output_folder, 'final_image.png')

paste_image_center(blurred_image_path, image_to_paste_path, final_image_path)