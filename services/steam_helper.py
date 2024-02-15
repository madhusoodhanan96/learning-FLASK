import requests
import json

API_KEY: str = ''
BASE_URL: str = ''

with open('../config_keys.json') as config_file:
    config_data = json.load(config_file)
    steam_values = config_data['steam']
    API_KEY = steam_values["API_KEY"]
    BASE_URL = steam_values["BASE_URL"]


def get_game_list():
    url = f"{BASE_URL}/ISteamApps/GetAppList/v0002/?key={API_KEY}&format=json"
    response = requests.get(url)
    data = response.json()
    return data


def get_player_summary(steam_id):
    """
    Get the player summary for a given Steam ID.
    """
    url = f"{BASE_URL}/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={steam_id}&format=json"
    response = requests.get(url)
    data = response.json()
    return data

# Example usage
# entire_game_list = list(get_game_list()["applist"]["apps"])
