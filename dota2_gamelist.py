


import dota2api
#https://github.com/joshuaduffy/dota2api
#https://dota2api.readthedocs.io/en/latest/

#如何获取API_KEY
def get_live_game_live():
    api = dota2api.Initialise("API_KEY")
    test = api.get_live_league_games()
    print(test)



test = get_live_game_live()

