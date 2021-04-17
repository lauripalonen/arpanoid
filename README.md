# ARPANOID  

Dice rolling bot for [discord](https://discord.com).

## Installation

Clone project: ```git clone git@github.com:lauripalonen/arpanoid.git```  

To run in a virtual environment, see [venv](https://docs.python.org/3/tutorial/venv.html).  

Install requirements: ```python -m pip install -r requirements.txt``` in project root.  

## Discord API  

For detailed directions to configure your bot on discord, please see [discord developer portal](https://discord.com/developers/docs/intro).  

Quick start: 
1. create an [app](https://discord.com/developers/applications)
2. get the bot token (navigate from application menu to Bot tab)
3. create .env file in root containing the token: ```BOT_TOKEN=your_token_here```
4. make sure .env is in your .gitignore. Do not share your token!
5. navigate to OAuth2 tab in the application menu and generate URL
6. follow that URL to connect your bot to your selected channel  

## Usage

Start Arpanoid: ```python3 arpanoid.py```  

Arpanoid commands on discord:  
* !help - display help
* !roll \<throws\>d\<die\> - roll a die (e.g. !roll 3d4)

## Etymology  

> **arpa** \['ɑrpɑ\] \(noun, Finnish\):  
> 1. lot (for example dice)  
> 2. (informal) lottery ticket  
> 
> Source: https://en.wiktionary.org/wiki/arpa#Finnish
