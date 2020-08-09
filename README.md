# saltbot
A WIP Discord bot written with discord.py

### Features
- A manager that starts the bot, allowing for starting and stopping the bot within discord.
- Five cogs: bangs, developer, easter, info and util, two of which currently do nothing.
- Ping fuctions for the bot and the manager.
- Bangs command from Miso bot
- Commands about the bot's github and license
- Released under the GNU AGPL v3.0.
- A README and a changelog.

### Requirements
(Note: The versions given have been tested with the bot. It may work with other versions.)
- UNIX or UNIX-like system*
- Python 3.8.x
- python-dotenv 0.14.0
- discord.py 1.4.0
- aiohttp 3.6.2

### Inviting
The bot will become public in the near future. Its invite link will be here!

### Hosting
This program uses python-dotenv to hide the auth token of the bot. If you wish to self-host, you must create a file called ".env" in the main directory. Paste the following into it, where `<token>` is your bot's auth token.
```
TOKEN="<token>"
```
Run botd.py, and from discord, use the command `&botd start`. To stop the bot, use `&stop` and to stop the manager, use `&botd stop`.

### Issues
Please use GitHub's issue tracker to report any issues and to suggest content!
