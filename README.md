# Discord-Command-Bot
Dieser Bot ist für mein eigenen Server, kann aber umgeschrieben werden und benutzt werden.
## Voruassetzungen

- Der Bot benutzt Python als Programmier spache, um in zu benutzten muss Python auf dem Gerät insterliert sein, wo der Bot drauf ausgeführt wird.

     ### **Windows**

     ◟ Lade und Installiere dir dazu die Neuste Version von Python runter. (https://www.python.org/downloads/)

     ### **Linux**

     ◟ Um Python zu installier nutze deisen Command im Terminal:
        
    ```
    sudo apt install python3.11
    ```
- Wenn du den Bot dauerhaft laufen haben willst, brauchst du ein Server, oder ein PC der immer angeschaltet ist, und eine Konstante Internet verbindung hat. Auf einem Linux Server solltest du ein Programm wie z.B. **"[screen](https://linuxize.com/post/how-to-use-linux-screen/)"** benutzen.

-Du brauchst ebenso ein Discord Accound um einen Bot zu erstellen.
## Bot Einrichten

Um den Bot zubenutzen, musst du auf dem Dicord Developer Portal (https://discord.com/developers/applications) eine neue Application erstellen.
Dafür druckst du auf den Knopf __"New Application"__
![Opera Momentaufnahme_2023-05-07_213841_discord com](https://user-images.githubusercontent.com/98546933/236699138-2125fd6e-71ab-4d40-a76c-9aaf82049cd1.png)

Anschliißend musst du deiner App einen namen geben und den **TOS** (https://discord.com/developers/docs/policies-and-agreements/terms-of-service) sowie **Developer Policy** (https://discord.com/developers/docs/policies-and-agreements/developer-policy) zustimmen.
![Opera Momentaufnahme_2023-05-07_214106_discord com](https://user-images.githubusercontent.com/98546933/236699342-01d16e6c-bf61-4499-bcab-6d53f87e6cea.png)

Nun musst du ein Bot der Application hinzufügen, gehe dazu auf Bot.![Opera Momentaufnahme_2023-05-07_214735_discord com](https://user-images.githubusercontent.com/98546933/236699652-398d7af7-e5db-4545-b10b-646e58a327a1.png)

Um deinen Bot-Tocken zu bekommen, drücke den Knopf: __"Reset Token"__. Dann erhälst du ein Tocken, den du dir Kopieren oder aufschreiben musst, da er später benötigt wird. ebenso solltest du mit niemanden teilen, da man mit ihn alles mit deinem Bot tun kann.
![Opera Momentaufnahme_2023-05-07_215112_discord com](https://user-images.githubusercontent.com/98546933/236699883-4d0664ff-47ec-4287-94de-d7ed08470fd5.png)

Danach kannst du den Tab wieder schißen.
## __Jetzt kommt es daruf an, ob du den Bot auf Windows oder Linux laufen haben willst.__

### **Windows**
- Gehe zuerst in den Übergeortneten Ordner, wo der Ortner ligt, wo der Bot seine Datein hat. (Wenn es noch eine ZIP-datei ist, entpacke sie zuerst.
- Mache Nun ein Rechts-Klick auf den Ordner, wo der Bot seine Datein hat und wähle __"In Terminal öffnen"__
- Im nun geöffneten Fenster gibst du den command ein.
```
pip install -r requirements.txt
```

- Bei Windows musst du nun einfach ein doppelklick auf die bei liegende __**start_windows.bat**__ machen, un der Bot solte starten.

### **Linux**
- Zuerst, musst du in dem Ordner, wo der Bot seine Datein hat, kommen. Dazu öffne das Terminal, und führe den Command  aus.
```
pip install -r requirements.txt
```

- Bei Linux musst du einfach die beiligende __**start_linux.sh**__ ausführen, entweder mit einen Doppelklick, oder per Command in dem Terminal:
```
./start_linux.sh
```
(Wenn [screen](https://linuxize.com/post/how-to-use-linux-screen/) insterliert ist, nutze den Command):
```
screen -S Discord-Bot ./start_linux.sh
```
Alle optionen setzen vorausgesetz, dass du im richtigen Ordner bist. Um zum Order zugelangen, benutze: ```cd /pfad/``` (z.B. ```cd /home/DC-Bot/```)

## Den Bot auf den Server bekommen
Nun wo der Bot gestartet ist, musst du den Bot-Tocken von vorhin per Rechtsklick im Terminal einfügen. Wenn alles richtig gelaufen ist, sollte der Botnach ein paar sekunden ein Link im Terminal augeben. Diesen musst du dir Kopiern, indem du in einfach mit der Maus auswählst. Anschlißend, gibst du ihn in deinem Browser ein. Dort musst du den Server auswählen, wo der Bot drauf Joinen soll.
![Opera Momentaufnahme_2023-05-07_221244_discord com](https://github.com/AlmarBlock/Discord-Command-Bot/assets/98546933/b032482a-23fd-4b21-8f3c-67d4261d899c)


Und dan auf __"Autorisieren"__ klicken.

![Opera Momentaufnahme_2023-05-08_213358_discord com](https://github.com/AlmarBlock/Discord-Command-Bot/assets/98546933/1a0b9ca1-b738-496d-be53-0289d23ded6a)


Nun ist der Bot auf deinem Server, und du kannst mit ```/test``` testen ob der Bot funktionirt.

![Opera Momentaufnahme_2023-05-08_214454_discord com](https://user-images.githubusercontent.com/98546933/236920382-8e507f3a-8280-4001-b860-d11db0472b3e.png)



## Ein eigenen Command Hinzufügen

Ein Command ist wie Folgt aufgebaut:
```
@client.tree.command()
async def command(interaction: Interaction):
    """ Infos zum Command """
    await interaction.response.send_message(content=f"Antwort des Bots", ephemeral=True)
```
-Hier an der stelle __"command"__ gibt man an, welchen kommand man in DC eingeben soll, um etwas aufzurufen.

```async def command(interaction: Interaction):```

-Hier an der stelle __"Infos zum Command"__ gibt man an, welchen kommand man in DC eingeben soll, um etwas aufzurufen.

```""" Infos zum Command """```

![Opera Momentaufnahme_2023-05-08_220454_discord com](https://user-images.githubusercontent.com/98546933/236922900-1a213128-c3a6-402f-abce-fe21e1327fed.png)


-Hier an der stelle __"Antwort des Bots"__ gibt man an, was der Bot antworten soll, wenn man ihn einen Command sendet. Wenn man die antwort über mehrere zeilen schreiben will, muss man ```\n``` verwenden anstat von ENTER. Bei der antwort, kann mit Formatieren von Text gearbeitet werden. (https://support.discord.com/hc/de/articles/210298617-Markdown-Text-101-Chat-Formatierung-Fett-Kursiv-Unterstrichen-) Um den namen des Absenders zu benutzen, versende  die Variable ```{interaction.user}```.

-Hier an der stelle __"ephemeral=True"__ gibt man an, ob die Nachricht nur von der Person, die den Command gesendet hat```True```, oder von allen gesehen werden soll```False```.

```await interaction.response.send_message(content=f"Antwort des Bots", ephemeral=True)```

Wenn du weitere Funktionen wie Embeds verwenden willst schaue dir DieDukumentation von dicord.py an. (https://discordpy.readthedocs.io/en/latest/index.html)

Bei Fragen bitte unter 
