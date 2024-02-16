import requests
import json

link = 'https://pelada-sesc-default-rtdb.firebaseio.com/peladas'

def get_active_party():
    req = requests.get(f'{link}/.json')
    all_party = req.json()
    for party in all_party:
        if all_party[party]['active'] == True:
            return party  
    return None
    
def update_players():
    active_party = get_active_party()
    players_list = []
    if active_party != None:
        req = requests.get(f'{link}/{active_party}/players/.json').json()
        for players in req:
            players_list.append(req[players])
        return players_list
    else:
        return None
    
def add_new_player(player):
    
    pass
    