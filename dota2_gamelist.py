


import dota2api,json
#https://github.com/joshuaduffy/dota2api
#https://dota2api.readthedocs.io/en/latest/

#如何获取API_KEY
def get_live_game_list():

    API_KEY = "BAF729E344FED5C902E36A75FC753271"
    api = dota2api.Initialise(API_KEY,raw_mode=True)
    try:
        #test1 = api.get_heroes()
        test2 = api.get_league_listing()
        #test = api.get_live_league_games()
        print(test2)
        json_str = json.dumps(test2)
        print(json_str)
        file_name = open("C:\\pro\\LX\\testfile\\game_list.txt",'w',)
        file_name.write(json_str)
        file_name.close()
    except :

        get_live_game_list()



test = get_live_game_list()


def writefile():
    file_name = open("C:\\pro\\LX\\testfile\\game_list.txt", 'w')
    file_name.write('test')
    file_name.close()

#test1 = writefile()

