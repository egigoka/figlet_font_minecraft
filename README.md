# figlet_font_minecraft

Did not tested on figlet. PR's are very welcome!

If someone knows how get umlauts and eszett to work, feel free to create Issue or PR. Additional languages will be wellcome!

To install and use [pyfiglet](https://pypi.org/project/pyfiglet/):

```pip install pyfiglet``` to install pyfiglet

```git clone https://github.com/egigoka/figlet_font_minecraft``` to download this font

```pyfiglet -L figlet_font_minecraft/minecraft.flf``` to install regular font
```pyfiglet -L figlet_font_minecraft/minecraft_condenced.flf``` to install condenced font

To use regular variant:
```pyfiglet -f minecraft your text here``

Results:
```
                           ▄█▄             ▄█▄   █
 █   █ ▄▀▀▀▄ █   █ █▄▀▀▄    █  ▄▀▀▀▄ ▀▄ ▄▀  █    █▄▀▀▄ ▄▀▀▀▄ █▄▀▀▄ ▄▀▀▀▄
 ▀▄▄▄█ █   █ █   █ █        █  █▀▀▀▀  ▄▀▄   █    █   █ █▀▀▀▀ █     █▀▀▀▀
 ▄▄▄▄▀  ▀▀▀   ▀▀▀▀ ▀         ▀  ▀▀▀▀ ▀   ▀   ▀   ▀   ▀  ▀▀▀▀ ▀      ▀▀▀▀
```

Condenced variant:
```pyfiglet -f minecraft_condenced your text here```

```
             ▗▙      ▗▙ ▐
▐ ▐▗▀▚▐ ▐▐▞▚  ▌▗▀▚▝▖▞ ▌ ▐▞▚▗▀▚▐▞▚▗▀▚
▝▄▟▐ ▐▐ ▐▐    ▌▐▀▀ ▞▖ ▌ ▐ ▐▐▀▀▐  ▐▀▀
▗▄▞ ▀▘ ▀▀▝    ▝ ▀▀▝ ▝ ▝ ▝ ▝ ▀▀▝   ▀▀
```

In proper terminal it looks much better:

![screenshot with text "your text here" written in ascii art](https://raw.githubusercontent.com/egigoka/figlet_font_minecraft/master/example.png)

![screenshot with text "your text here" written in ascii art](https://raw.githubusercontent.com/egigoka/figlet_font_minecraft/master/example_condenced.png)
