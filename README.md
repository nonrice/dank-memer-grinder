# Dank Memer Grinder
An automessaging script made to automatically get items and money in the ever-popular [Dank Memer Discord Bot](https://www.dankmemer.lol)

## Details
* Will repeatedly cycle through a user-written list of commands
* Will automatically type out prompts, e.g. `get the camera ready` when encountering a legendary fish whilst using `pls fish`
* It is not advised to use `horseshoes` as they break very fast when this bot is operating
* The bot has a feature that stores necessary data in a file so you do not need to keep filling it out.

## How to Use
Download the code and unzip it. Then, open the Command Line, navigate to inside the folder `dank_memer_grinder`, and run `grinder.py`. The commands to perform this are listed below. Enter them line by line:
```
cd ~/Downloads/dank-memer-grinder-main/dank_memer_grinder
python3 grinder.py
```
Follow the instructions carefully. When using for the first time, the program asks you for identification info, so it can automate sending messages from your account. The parameters it asks for and how to obtain them are listed:
* `User Agent`: This identifies your platform to Discord in the HTTP request. A [google search](https://www.google.com/search?q=what+is+my+user+agent) will give it to you. Copy and paste it.
* `Discord Token`: This authorizes the Python script to have use of your Discord account. This is a little tricky to get, though there are plently of tutorials readily availible online. Paste it directly into the field.
* `Channel URL`: This tells the bot which channel it should send the message in. On the browser version, navigate to the desired channel, and copy the URL from the suarch bar. 
* `Channel ID`: Same purpose as above. Right click on the channel (from the menu), and press `Copy ID`. If you don't see the `Copy ID` option, go into settings and turn on `Developer` from the Advanced menu.

## Final Words
Thank you for using my program! It makes me happy to see other people using my work. 

Do take note that leaving this program running for long times (around 6+ hours) and many consecutive days will earn you a blacklist or a ban from the bot. That said, it is usually fine to use it for a few hours, ocassionally. 
