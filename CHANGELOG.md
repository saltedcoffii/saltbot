# Changelog
All notable changes to this project will be documented in this file.

## [0.0.3] - 2020-08-09
### Added
- Duckduckgo bang feature invoked with `&!<bang> <search> [terms]`.
    - Bangs cog, associated with Duckduckgo bang feature
    - Learn more about Duckduckgo bangs at [duckduckgo.com/bangs](https://duckduckgo.com/bangs)
    - Feature ported from [Miso bot](https://github.com/joinemm/miso-bot) under the [MIT License](https://mit-license.org/).
### Changed
- Fixed minor spelling errors
- Changed license and github commands slightly
- Updated README
- Updated CHANGELOG
  - Capitalized filename



## [0.0.2] - 2020-08-08
### Added
- Bot reacts with 👋 to messages that start with words like "hello" and "sup".
- Bot responds to "stfu" with "no u".
- Easter cog, currently does nothing and isn't loaded by the main script.
- Info cog.
- Github command in info cog
- License command with pretty embed in info cog
- Echo command in util cog
### Changed
- Bot status 🤭
- Updated README
- Updated changelog
### Removed
- Base cog, along with 0 features

## [0.0.1] - 2020-08-07 - Initial Release
### Features
- A manager that starts the bot, allowing for starting and stopping the bot within discord.
- Ping fuctions for the bot and the manager.
- Three cogs (base, developer and util) that currently do nothing.
- Released under the GNU AGPL v3.0.
- A README and a changelog.

### Requirements
(Note: The versions given have been tested with the bot. It may work with other versions.)
- UNIX or UNIX-like system
- Python 3.8.x
- python-dotenv 0.14.0
- discord.py 1.4.0
