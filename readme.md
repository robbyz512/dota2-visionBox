<br>

<p align="center" style="font-size:30px; color: #7d1211 ">
This tool and all other visibility cheats do not work anymore they are patched by Valve. When other hackers discover a new method I can update this tool.
</p>

<p align="center" style="font-size:20px">
Shows when your hero is visible to the enemy team in any way at all
</p>

When box is red the enemy team has vision of your hero and green if they don't. Lets you know if you are under a ward or an invisible hero sees you..etc makes rotating/farming/initiating/dewarding all much easier. It's basically like having slark ultimate passive on every hero.

It works in windowed mode only but you can use it in fullscreen if you have dual monitors to show the box on your other screen.

## Hotkeys:

    Hold Left Click on box to move it
    Double Click the box to close it

**You can customize box position, size, colors in settings.txt**

## Screenshots:

<p align="center">
    Visible
    <img src="https://i.imgur.com/FUTJ3dN.png">
    Not visible
    <img src="https://i.imgur.com/RgyCJqx.png">
    Fullscreen Support for Dual Monitor
    <img src="https://i.imgur.com/EG3AG4u.jpg">
</p>

## Download

https://www.unknowncheats.me/forum/other-mmorpg-and-strategy/513393-dota-2-visionbox-customizable-overlay-cheat.html

## Compile Instructions

`python 3.10.6`

`pip install -r requirements.txt`

`python -m nuitka --onefile --enable-plugin=tk-inter --windows-disable-console --windows-icon-from-ico=favicon.ico --include-package=pymeow visionBox.pyw`

After compiling you can drag "visionBox.exe" and "settings.txt" in another folder and run it there.
