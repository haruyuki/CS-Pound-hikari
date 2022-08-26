# CS Pound Discord Bot

[![hikari-py](https://img.shields.io/badge/hikari-v2.0.0.dev105-de4f91.svg)](https://github.com/hikari-py/hikari)
[![tanjun](https://img.shields.io/badge/tanjun-v2.3.0a1-blue.svg)](https://github.com/FasterSpeeding/Tanjun)
[![Python 3.9](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/github/license/haruyuki/CS-Pound-hikari.svg)](https://github.com/haruyuki/CS-Pound-hikari/blob/main/LICENSE)

---

Due to the discontinuation of Discord.py (Read more about it [here](https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1)), this repository is a rewrite of the original CS-Pound discord.py code from [here](https://github.com/haruyuki/CS-Pound). To continue support and maintenance of this bot, it is being rewritten to use [Hikari](https://github.com/hikari-py/hikari) and [Tanjun](https://github.com/FasterSpeeding/Tanjun), which has support for the new Slash Commands.

---

A Discord bot for the virtual pet adoption website [Chicken Smoothie](https://www.chickensmoothie.com). With this bot you can view information on pets and pound opening times straight from Discord without accessing the website.

## Features

| Command       | Description                                                                        | Example                                                                       |
|-------------  |----------------------------------------------------------------------------------  |---------------------------------------------------------------------------    |
| ,autoremind   | Setup an autoremind for when the pound opens                                       | ,autoremind 5m                                                                |
| ,cs           | Given an amount of C$, returns the equivalent amount in FR gems and treasure       | ,cs 100                                                                       |
| ,gems         | Given an amount of FR gems, returns the equivalent amount in treasure and C$       | ,gems 623<br>,fr 1                                                            |
| ,help         | Displays the help message of all or a specific command.                            | ,help<br>,help autoremind                                                     |
| ,identify     | Tells you the archive page where a pet or item is located                          | ,identify <https://www.chickensmoothie.com/viewpet.php?id=109085729>          |
| ,invite       | Sends you a link to where you can invite CS Pound to your Discord server           | ,invite                                                                       |
| ,news         | Allows you to show or opt in to announcements on the Chicken Smoothie              | ,news on<br>,news off<br>,news latest                                         |
| ,poundpets    | Searches through the pound account for rare pets and display them all in an image  | ,poundpets<br>,poundpets get                                                  |
| ,remindme     | Pings you after specified amount of time. Maximum reminding time is 24h            | ,remindme 1h6m23s<br>,remindme 12m<br>,remindme 1h10s                         |
| ,statistics   | Displays CS Pound bot statistics                                                   | ,statistics                                                                   |
| ,support      | PM's you the link to the CS Pound Development Server                               | ,support                                                                      |
| ,time         | Tells you how long before the pound opens                                          | ,time                                                                         |
| ,treasure     | Given an amount of FR treasure, returns the equivalent amount in gems and C$       | ,treasure 752642<br>,tr 6463                                                  |

## Usage
I would prefer if you don't your run own instance of my bot, but rather use the already existing instance. Head to [https://haruyuki.moe/cs-pound/](https://haruyuki.moe/cs-pound/) and click the "Invite to Discord" button to invite the bot to your server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

All pet rarity images are property of [Chicken Smoothie](https://www.chickensmoothie.com).
