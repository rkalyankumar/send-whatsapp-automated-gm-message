# Automated Good Morning Message Sender

If you are like me, bored to send/reply to good morning messages to your friends, this is the solution you have.
I have tried to automate using [_pywhatkit_](https://github.com/Ankit404butfound/PyWhatKit), so you will need it
to install it using the pip command:

```sh
    pip3 install pywhatkit
```

You will also need to automate it using your system scheduler. I use linux and hence I use crontab:

```sh
10 12 * * * * DISPLAY=:0 /path/to/script/send_gm.py <your friend's whatsapp number> >> ~/cron.log 2>&1
```

For example above crontab entry will run the script everyday at 12:10pm.

You have to do additional things if you are in linux:

```sh
$ cd ~/
$ touch .Xauthority
$ xhost +
```

Ensure you use single screen/monitor and single webbrowser window. This is a limitation of _pywhatkit_.

Enjoy this script at your own risk.

