<br>
Shows when your hero is visible to the enemy team in any way at all. If box is red the enemy team has vision of your hero, good for dewarding and farming safely and many other advantages.

It works in windowed mode only but you can use it in fullscreen if you have dual monitors to show the box on your other screen.

## Hotkeys: 
	Hold Left Click on box to move it
	Double Click the box to close it

**You can customize box position, size, colors in settings.txt**

## Screenshots:

<p align="center">
    Visible
    <img src="https://i.imgur.com/VPF08Qx.png">
    Not visible
    <img src="https://i.imgur.com/DeQjyH3.png">
    Fullscreen Support for Dual Monitor
    <img src="https://i.imgur.com/EG3AG4u.jpg">
</p>

## Installation Instructions

`python 3.10.6`

`pip install -r requirements.txt`

`python -m nuitka --onefile --enable-plugin=tk-inter --windows-disable-console --windows-icon-from-ico=favicon.ico --include-package=pymeow visionBox.pyw`

After compiling you can drag "visionBox.exe" and "settings.txt" in another folder and run it there.