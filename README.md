![Arkwork](https://github.com/vertyco/Vertyco/blob/main/.github/resources/vrt-cogs-01.png)

Various useful and fun cogs for Red V3.

![Py](https://img.shields.io/badge/python-v3.11-orange?style=for-the-badge)
![black](https://img.shields.io/badge/style-black-000000?style=for-the-badge&?link=https://github.com/psf/black)
![license](https://img.shields.io/github/license/Vertyco/Vrt-Cogs?style=for-the-badge)

![Red-DiscordBot](https://img.shields.io/badge/Red%20DiscordBot-V3.5-red?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Vertyco/Vrt-Cogs?color=blueviolet&style=for-the-badge)


I enjoy working with APIs and making cogs for game servers or other helpful use cases. Check out some of my projects
below!

| Cog                                    | Status | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------|:------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Assistant](assistant/README.md)       |   ✓    | <details><summary>Get your own AI assistant in Discord</summary> Automate your server with OpenAI's ChatGPT language model (or [self-host your own!](https://github.com/vertyco/gpt-api)). Configure a prompt with condensed information about your server, along with other options to make answering questions easier. Setup embeddings to optimize token usage, and even write custom functions to extend the functionality of what the assistant can do!</details> |
| [AutoDocs](autodocs/README.md)         |   ✓    | <details><summary>Document your cogs with ease!</summary> Easily generate documentation for any cog in Markdown format.</details>                                                                                                                                                                                                                                                                                                                                      |
| [EconomyTrack](economytrack/README.md) |   ✓    | <details><summary>Track your economy's total balance and member count over time.</summary> Visualize the total market cap of your Red economy. Note: Having bank set to local on a public bot will cause much heavier I/O load than using a global bank.</details>                                                                                                                                                                                                     |
| [Cartographer](cartographer/README.md) |   ✓    | <details><summary>Discord Server Backup/Restore</summary> Create backups of your Discord server and restore them easily.</details>                                                                                                                                                                                                                                                                                                                                     |
| [BankDecay](bankdecay/README.md)       |   ✓    | <details><summary>Inactivity-based economy credit decay with customizable settings</summary> Introduces an economy decay system to Discord servers, automatically reducing inactive users' currency to stimulate engagement. Admins can customize and oversee decay settings, fostering active participation within the community.</details>                                                                                                                           |
| [EmojiTracker](emojitracker/README.md) |   ✓    | <details><summary>Simple emoji tracker with leaderboards.</summary> Track reactions in your server and get leaderboards for emojis that are most used, or users that have reacted the most.</details>                                                                                                                                                                                                                                                                  |
| [Events](events/README.md)             |   ✓    | <details><summary>Host events in your Discord.</summary> Create and manage events easily with a variety of entry types and requirements. Event submissions will be posted and counted with a winner or winners announced automatically when the event is complete.</details>                                                                                                                                                                                           |
| [Fluent](fluent/README.md)             |   ✓    | <details><summary>Easy to use translation tools.</summary> Translate messages or set a channel and both languages, if a message is in language 1 it gets converted to language 2 and vice versa using googles free api.</details>                                                                                                                                                                                                                                      |
| [GuildLock](guildlock/README.md)       |   ✓    | <details><summary>Manage what kind of servers the bot can join.</summary> Manage what kind of servers the bot can join. A stripped down rewrite of Phen's Baron cog.</details>                                                                                                                                                                                                                                                                                         |
| [GuildLog](guildlog/README.md)         |   ✓    | <details><summary>Set a channel to log guilds the bot leaves/joins.</summary> Configure a join/leave message of your choice and whether you want to use embeds or not, the bot will log when it joins or leaves a guild. All guilds can use this cog to see what servers the bot is joining(Guild Name/Bot Name/Total Servers)</details>                                                                                                                               |
| [Hunting](hunting/README.md)           |   ✓    | <details><summary>Hunt birds in your server!</summary> Originally created by Paddo for red v2, then ported to v3 by aikaterna#1393, and now maintained by me. This cog allows you to 'hunt' birds in your server via reactions or text.</details>                                                                                                                                                                                                                      |
| [LevelUp](levelup/README.md)           |   ✓    | <details><summary>Streamlined Discord Leveling System.</summary> An intuitive full-featured leveling system with prestige features, customizable backgrounds, toggleable embed/image profiles, and extensive voice tracking options.</details>                                                                                                                                                                                                                         |                                                                                    |
| [Meow](meow/README.md)                 |   ✓    | <details><summary>Meow</summary> Replaces the word "now" with "meow" in someone's latest message, if word doesnt exist in the most recent 2 messages, it sends a random cat unicode emoji. Yall have a good day meow.</details>                                                                                                                                                                                                                                        |
| [NoBot](nobot/README.md)               |   ✓    | <details><summary>Filter certain messages from other bots.</summary> (ONLY checks messages from other bots), Add a bot to be filtered and a key phrase to check for. When that bot sends a message containing that phrase the message will be auto-deleted.</details>                                                                                                                                                                                                  |
| [NoNuke](nonuke/README.md)             |   ✓    | <details><summary>A very straightforward Anti-Nuke cog.</summary> Set a cooldown and overload count(X events in X seconds), if any user with perms exceeds them, you can set an action to be taken and logged. Events include Kicks/Bans, Channel Creation/Edit/Deletion, Role Creation/Edit/Deletion. Events are not counted separately so any action taken in any order applies to the cooldown bucket.</details>                                                    |
| [Pixl](pixl/README.md)                 |   ✓    | <details><summary>Guess pictures with friends and earn points.</summary> Start a game to have a mostly blank image pop up. Every few seconds a few blocks will show up and the goal is to guess what it is before the image is completed or time runs out. You are also competing with everyone else in the channel the game is running in!</details>                                                                                                                  |
| [Pupper](pupper/README.md)             |   ✓    | <details><summary>Pet the doggo!</summary> Originally created by aikaterna#1393, now maintained by me. This cog has pet that comes around on an on_message listener and waits for someone to pet it (react with a standard wave emoji), and rewards with credits. Many attributes are configurable.</details>                                                                                                                                                          |
| [Tickets](tickets/README.md)           |   ✓    | <details><summary>Customizable Multi-Panel support ticket system.</summary> 'Tickets' is an easy to use, fully customizable multi-panel ticketing system with a variety of options and features including modals, logging, transcripts, multi-button panels and more!</details>                                                                                                                                                                                        |
| [UpgradeChat](upgradechat/README.md)   |   ✓    | <details><summary>API Integration for the Upgrade.Chat API.</summary> Allows you to add your api key and products to the bot and set a dollar to credit conversion ratio. When a user makes a purchase, they can claim it in your Discord to receive economy credits.</details>                                                                                                                                                                                        |
| [VrtUtils](vrtutils/README.md)         |   ✓    | <details><summary>Random utility commands.</summary> Small collection of commands used for my personal bot.</details>                                                                                                                                                                                                                                                                                                                                                  |
| [XTools](xtools/README.md)             |   ✓    | <details><summary>Access your xbox profile and much more.</summary> Various tools for Xbox using Microsoft's XSAPI. View your Xbox profile, friends, screenshots and game clips using simple commands and interactive menus. (You will need to register a Microsoft Azure application to use this cog. Type "[p]apiset help" after install for more info)</details>                                                                                                    |


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/vertyco)<br/>

# Installation

Run the following commands with your Red instance, replacing `[p]` with your prefix:

If you haven't loaded the Downloader cog already, go ahead and do that first with: `[p]load downloader`. Then,

```ini
[p]repo add vrt-cogs https://github.com/vertyco/vrt-cogs
[p]cog install vrt-cogs <list of cogs>
[p]load <list of cogs>
```

# Credits

- Obi-Wan3 for holding my hand through a lot of my issues and questions I've had in the very beginning while learning
  python, and providing me with tips for finding things by myself.
- All the Red staff members for being so damn helpful and having valuable insight.
- The Red discord coding channel for having lots of helpful cog creators!

# Contact

For support with my cogs, feel free to hit me up in [#support_othercogs](https://discord.com/channels/240154543684321280/1039309390785810493/1039310040101818439) in
the [Red Cog Support](https://discord.gg/GET4DVk) server.

# Contributing

If you have any suggestions, or found any bugs, please ping me in Discord (Vertyco#0117)
or [open an issue](https://github.com/vertyco/vrt-cogs/issues) on my repo!

If you would like to contribute, please talk to me on Discord first about your ideas before opening a PR.

# Translate my cogs

If you are interested in contributing to translations for my cogs, [Click Here](https://crowdin.com/project/vrt-cogs)!

# Feature Requests

I am open to ideas or suggestions for new cogs and features!
<br/>
<br/>
---

<a href="https://star-history.com/#vertyco/vrt-cogs&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=vertyco/vrt-cogs&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=vertyco/vrt-cogs&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=vertyco/vrt-cogs&type=Date" />
  </picture>
</a>

![Forks](https://img.shields.io/github/forks/Vertyco/Vrt-Cogs?style=for-the-badge&color=9cf)
![Stars](https://img.shields.io/github/stars/Vertyco/Vrt-Cogs?style=for-the-badge&color=yellow)
[![Visitors](https://api.visitorbadge.io/api/daily?path=https%3A%2F%2Fgithub.com%2Fvertyco%2Fvrt-cogs&label=Visitors%20Today&countColor=%230015b3)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fvertyco%2Fvrt-cogs)
[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fvertyco%2Fvrt-cogs&label=Total&countColor=%239085b3)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fvertyco%2Fvrt-cogs)

![](.github/ASSETS/Bottom_down.svg)