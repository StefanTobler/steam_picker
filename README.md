# Steam Game Picker

This is a small CLI program that picks a random game from your steam library to play. My goal was to create a GUI program that displayed me my games across UPLAY, Origin, Epic, Steam, and Battle.net, but it looks like a few of these companies choose to not have publicly facing apis. So instead I decided to learn a bit about JSONs and python. Here are the results.

## How to Use

First, get your Steam API key by going to this [Steam API link](https://steamcommunity.com/dev/apikey).

Next, set the API key to an environment variable using this command:

`export STEAM_KEY="APIKEY"`

Finally you will need to enter your Steam ID, no this is not that thing after `/id/` in your steamcommunity url. I know it is silly, however if you do not have a vanity url, then that is you Steam ID. Otherwise please visit [SteamIDfinder](https://steamidfinder.com/) and type in your vanity url to get your real Steam ID. Then copy that into the code.

## How to Run        

To run this program type:

`python3 steam.py`

If running for the first time, enter 'y' when prompted. Otherwise, enter 'n', unless you have recently added new games to your Steam library. That's it, enjoy!
