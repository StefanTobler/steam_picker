'''
 @Author Stefan Tobler
 @Date April 10, 2020
'''
import os
import requests as req
import json
import random

API_KEY = os.environ.get('STEAM_KEY')
STEAM_ID = '76561198063166582'
running = True

# http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{hash}.jpg
# ICON: http://media.steampowered.com/steamcommunity/public/images/apps/7000/df2e4400b953ab62c43ddd590684ecafd339134d.jpg
# LOGO: http://media.steampowered.com/steamcommunity/public/images/apps/7000/a7e20f47f52a72173ee28bd29c09a459b5689744.jpg

def load_steam():
    response = req.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + API_KEY + '&steamid='+ STEAM_ID + '&format=json&include_appinfo=true')
    data = response.json()

    if response.status_code == 200: # checking that data was retrieved
        with open('steam.json', 'w+') as f:
            f.write(json.dumps(data, indent=2))

if __name__ == '__main__':
    while running:
        os.system('clear; figlet -w 160 STEAM GAME INDEX v0.1')
        print('Welcome to Steam Game Index!')
        print()
        user_response = input('Would you like to reload your game library? (y/n) ')
        print()
        print('Loading games...')
        if user_response == 'y':
            load_steam()

        with open('steam.json') as f: # loading game json
            data = json.load(f)['response']
        
        print()
        print('Picking a game for you to play...')

        games = data['games']

        game_picked = games[random.randint(0, len(games))]

        print('\t' + game_picked['name'])
        print('\t' + 'Playtime: ' + str(game_picked['playtime_forever']) + ' minutes')
        print('\t' + 'Store page: https://steamcommunity.com/app/' + str(game_picked['appid']))

        running = False
