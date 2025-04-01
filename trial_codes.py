import json


import json

def player_generator():
    with open("players.json", "r") as file:
        player_json_list = json.load(file)
    
    player_list_values = [list(dictionaries.values())[0] for dictionaries in player_json_list]
    
    # Remove "player0" if it exists
    if player_list_values and player_list_values[0] == "player0":
        player_list_values.pop(0)
    
    players = {
        "Andrew": "",
        "Kesler": "",
        "Utomi": "",
        "Eddy": ""
    }
    
    player_names = list(players.keys())
    
    for i, value in enumerate(player_list_values[:4]):
        players[player_names[i]] = value
    
    return players

# Example usage
assigned_players = player_generator()
for player, value in assigned_players.items():
    print(f"{player} = {value}")

