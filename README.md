# Snapper

Snapper was built during the Canadian Open Data Experiance (CODE), a Hackathon that requires the use of open data in the project.

Snapper is a Python built Snapchat bot using [Edmonton public art data](http://namara.io/#/display/51b6af69-fcd9-4517-ac6b-39e89310c1eb).  This project relies on [SnapchatBot](https://github.com/agermanidis/SnapchatBot) to provide a Python interface and some boilerplate for making a bot that resides on Snapchat.  This library is included in this repo - no need to install it seperately.

# Installation

1. clone this repo
2. `$ python setup.py install` (virtualenv, recommended)

# Usage

1. Use the official snapchat app to make an account for the bot
1. cd into `/src`
2. `$ python opendatabot.py -u <account-name> -p <account-password>` to start the bot

The bot will run in the terminal.  As long as the terminal window is open, the bot is active.  Once the terminal window is closed, the bot is no longer active.

# How it works
 
When you send the bot a snapchat - any snapchat - a picture of you're adorable dog, a big chocolate cake, a dolphin dancing.  The bot is selfish and simply doesn't care about your life and what you send it.

Once you send your snap the bot will hit an API endpoint with JSON data on public art in the City of Edmonton.  This RESTful API is provided by [Namara](http://namara.io/#/search), a service for browsing open data.  The bot will then randomly select a piece of art from this JSON response.

It will do a google image search using the title and artist name of the particular piece.  The [Google Search API](https://developers.google.com/image-search/v1/jsondevguide) is used to handle this, and will return another JSON object this time holding a bunch of links to image results.

The bot is bold and trusts that the first image result is a picture of the piece of art.  It will download that image.  And that is it! At this point the SnapchatBot library is used to send this downloaded image back to the original (human) sender.  

Due to Edmonton not having a ton of public art, there is only a handful of possible images that will be send back :)
