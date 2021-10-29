# Frwd-Tag-Remover

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  <br>
  <a href="https://tx.me/DevelopedBots">
    &nbsp;<img src="https://img.shields.io/badge/Developed%20%20Bots-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://tx.me/DevelopedBotz">
    &nbsp;<img src="https://img.shields.io/badge/Developed%20%20Botz-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/Kunal-Diwan/Frwd-Tag-Remover/stargazers">
    <img src="https://img.shields.io/github/stars/Kunal-Diwan/Frwd-Tag-Remover?style=social">
  </a>
  <a href="https://github.com/Kunal-Diwan/Frwd-Tag-Remover/fork">
    <img src="https://img.shields.io/github/forks/Kunal-Diwan/Frwd-Tag-Remover?label=Fork&style=social">
  </a>  
</p>


Telegram Bot to Remove forward tag from any Post .

**If you need any more modes in repo or If you find out any bugs, mention in [@DevelopedBotz](https://www.telegram.dog/DevelopedBotz)**

### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- Remove forwarded tag from media also
- Can be deployed on heroku directly.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Kunal-Diwan/Frwd-Tag-Remover)</br>

#### Deploy in your VPS
````bash
git clone https://github.com/Kunal-Diwan/Frwd-Tag-Remover
cd Frwd-Tag-Remover
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/users - view bot statistics

/broadcast - broadcast any messages to bot users
```

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `API_ID` Your API ID from my.telegram.org
* `BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- [CodeXBotz](https://github.com/CodeXBotz/File-Sharing-Bot/) - for his File-Sharing-Bot database .

### © Copyright

           Copyright (C) 2021 by Kunal-Diwan ❤️️

        Licence under the terms of the AGPL-3.0 License

#### Star this Repo if you Liked it ⭐⭐⭐

