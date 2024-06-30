# Roblox-Crash-Image-Generator

---

The program came about when I was playing on Roblox RP servers where people were breaking the RP rules, which led to my frustration and ultimately getting banned for leaving the game during RP. This program was created to generate fake "crash" screenshots to prevent such situations.
The program is available in two languages, Polish and English.

---

**User manual for the crash image generator for Roblox**

1. **System Requirements:**
   - Make sure you have Python installed (preferably the latest version) and the `pip` tool for managing Python libraries. If you don't have them, you can install them from https://www.python.org/downloads/ or through the Microsoft Store. To install `pip`, execute the `install pip` command in the console or visit https://kt.academy/pl/article/py-instalacja-pakietow and follow the instructions.

2. **Installation of necessary libraries:**
   - Run `install_req.bat` to install required Python libraries such as `pillow`. Wait until the installation is complete.

3. **Starting the program:**
   - After installing the libraries, make sure you have a properly prepared input image (full screen game screen, saved as `enter.png`). Place it in the `put_here` directory, which is located in the generator folder.

4. **Generating a crash image:**
   - Run the `generator.py` script.
   - The program will ask you to read the user manual located in the `READ_ME.txt` file (what you are currently reading). Type `Y` to continue or `N` to close the program and read the instructions.
   - After reading the instructions, the program will automatically start generating the image.

5. **Crash language selection:**
   - The program will ask you to select the language in which you want to generate the crash image (`PL` - Polish or `EN` - English).
   - Enter the appropriate option (`PL` or `EN`). If you make a mistake, the program will ask again.

6. **Generating the final image:**
   - Based on the selected language, the program will insert the appropriate crash image (`crash_pl.png` or `crash_en.png`) from the `source` folder into the center of the previously generated blurred image.
   - The final image will be saved in the `finished` folder as `final_image.png` (the name can be changed).

7. **End of program:**
   - After the program finishes, you will find the final image in the `finished` folder.

8. **Warning:**
- **DO NOT** rename any Python folder or file in the program structure. Touching files in the `source` folder may cause the program to malfunction. For the program to work properly, the file in the `put_here` folder must be named `enter.png`.

9. **Preparing to restart the program:**
   - To restart the program, delete the image from the `put_here` folder and place a new image there called `enter.png` if you want to generate an image based on another screenshot. Also make sure the `finished` folder is clean to avoid overwriting the new image with the old one.
   - The `temp` folder contains temporary blurry images and does not require manual intervention, however it can be cleaned to save disk space.

---

**Instrukcja obsługi generatora obrazka z crashem do Robloxa**

1. **Wymagania systemowe:**
   - Upewnij się, że masz zainstalowany Python (najlepiej najnowszą wersję) oraz narzędzie `pip` do zarządzania bibliotekami Pythona. Jeśli ich nie masz, możesz je zainstalować ze strony https://www.python.org/downloads/ lub przez Microsoft Store. Aby zainstalować `pip`, wykonaj polecenie `install pip` w konsoli lub odwiedź stronę https://kt.academy/pl/article/py-instalacja-pakietow i postępuj zgodnie z wytycznymi.

2. **Instalacja niezbędnych bibliotek:**
   - Uruchom plik `install_req.bat`, aby zainstalować wymagane biblioteki Pythona, takie jak `pillow`. Poczekaj, aż instalacja się zakończy.

3. **Uruchomienie programu:**
   - Po zainstalowaniu bibliotek upewnij się, że masz odpowiednio przygotowany obraz wejściowy (screen z gry na pełnym ekranie, zapisany jako `enter.png`). Umieść go w katalogu `put_here`, który znajduje się w folderze generatora.

4. **Generowanie obrazka z crashem:**
   - Uruchom skrypt `generator.py`.
   - Program poprosi Cię o zapoznanie się z instrukcją obsługi, znajdującą się w pliku `READ_ME.txt` (to co właśnie czytasz). Wpisz `Y`, aby kontynuować, lub `N`, aby zamknąć program i zapoznać się z instrukcją.
   - Po zapoznaniu się z instrukcją program automatycznie rozpocznie generowanie obrazka.

5. **Wybór języka crasha:**
   - Program poprosi Cię o wybór języka, w którym chcesz wygenerować obrazek z crashem (`PL` - Polski lub `EN` - Angielski).
   - Wpisz odpowiednią opcję (`PL` lub `EN`). Jeśli się pomylisz, program zapyta jeszcze raz.

6. **Generowanie finalnego obrazka:**
   - Na podstawie wybranego języka program wstawi odpowiedni obrazek z crashem (`crash_pl.png` lub `crash_en.png`) z folderu `source` na środek wcześniej wygenerowanego rozmytego obrazka.
   - Finalny obrazek zostanie zapisany w folderze `finished` jako `finalny_obraz.png` (nazwę można zmienić).

7. **Zakończenie programu:**
   - Po zakończeniu działania programu znajdziesz finalny obrazek w folderze `finished`.

8. **Ostrzeżenie:**
   - **NIE WOLNO** zmieniać nazwy żadnego folderu ani pliku Pythona w strukturze programu. Dotykanie plików w folderze `source` może prowadzić do nieprawidłowego działania programu. Aby program działał poprawnie, plik w folderze `put_here` musi być nazwany `enter.png`.

9. **Przygotowanie do ponownego uruchomienia programu:**
   - Aby ponownie uruchomić program, usuń obrazek z folderu `put_here` i umieść tam nowy obrazek o nazwie `enter.png`, jeśli chcesz wygenerować obrazek na podstawie innego screena. Upewnij się również, że folder `finished` jest czysty, aby uniknąć nadpisania nowego obrazka starym.
   - Folder `temp` zawiera tymczasowe obrazy rozmyte i nie wymaga ręcznej interwencji, jednak można go wyczyścić, aby oszczędzić miejsce na dysku.

---
