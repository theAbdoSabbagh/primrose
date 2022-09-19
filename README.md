<h1 align="center">Primrose</h1>

<p align="center">
  <img width="100" height="100" src="https://avatars.githubusercontent.com/u/113864858?s=200&v=4">
</p>

<h4 align="center">A modern, open source Discord selfbot written in Python.</h4>

<p align="center">
  <a href="#planned-features">Planned Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#compile">How To Compile</a> •
  <a href="https://discord.gg/5nqcjV8a">Discord Server</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>


<BR>![Screenshot](https://cdn.discordapp.com/attachments/1021505080584851577/1021505135911899257/Screenshot_2022-09-19_213552.png?size=4096)

## Planned Features

- **Modern look** — Featuring a TUI (text-based user interface) and a modern look, Primrose is easy to use and looks great.
- **Stable operation** —  Primrose is built on top of the Discord.py library, which is known for its stability and reliability.
- **Cross-platform** — Windows, Linux, MacOS
- **GPL-3.0 license**

## Installation
`Important: This is still a work in progress.`

Ensure you have at Python 3.10 64bit installed.
 ```
    git clone
    cd Primrose
    pip install -r requirements.txt
    python entry.py
 ```

You can of course download the latest release from the [releases page] and run it from there.

## Compile
`Important: This is still a work in progress.`

Primrose releases are compiled using [PyInstaller]. To compile Primrose yourself, you will need to install PyInstaller and run the following command:

```
pyinstaller --onefile --icon=primrose.ico entry.py
```

## Credits

- Developed by [Nshout](https://github.com/Nshout), former developer of Luna Selfbot.

- [Rapptz](https://github.com/Rapptz) for the awesome Discord API wrapper - [Discord.py](https://github.com/Rapptz/discord.py).

- [Dolfies](https://github.com/dolfies) for the selfbot features on [Discord.py-self](https://github.com/dolfies/discord.py-self).

## Conclusion

After going around and checking out open source selfbots, I noticed that all of them simply lacked in command separation and proper categorizing.
I can see why no one would do it since most would do it with `load_extension`, and that requires an openly exposed .py file.
Basically compiling with closed source is not possible that way.

Primrose uses a different approach that is organized and compilable without exposed source code.

Primrose like any other selfbot is against Discord's ToS, and I am not responsible for any bans you may get.

This is my first open source project, and I am facing that fact that there will be code I might get laughed at, but I am here to learn and maybe even teach or inspire others.

I am also not a professional programmer, so I am sure there are many things I can improve on, and I am open to suggestions.

I am also known with the fact that people will probably copy my code and make their own selfbot, but I don't allow closed source releases as stated in the license.

## License
Primrose is licensed under the [GPL-3.0 License](https://github.com/primrose-sb/primrose/blob/main/LICENSE).