import urllib2
import json
import time
import ExportCSV

api_key="?api_key=your_api_key" #append your api key here


class Collector:
    def __init__ (self,name_in):
        self.name = name_in
        self.headers = ["timePlayed","win","gameMode","mapId","totalDamageDealt", "magicDamageDealtToChampions",	"playerPosition","subType", "teamId","largestMultiKill","ipEarned",	"magicDamageTaken","totalTimeCrowdControlDealt","trueDamageDealtPlayer","neutralMinionsKilledEnemyJungle", "championId", "item2","item3", "createDate",	"item1","wardPlaced", "invalid", "physicalDamageDealtToChampions", "item6",	"visionWardsBought","neutralMinionsKilledYourJungle", "championsKilled","gameId","trueDamageTaken",	"minionsKilled","assists", "neutralMinionsKilled",	"spell1", "spell2",	"goldSpent","trueDamageDealtToChampions","level","physicalDamageDealtPlayer","totalHeal","gameType","magicDamageDealtPlayer", "goldEarned",	"totalDamageDealtToChampions", "totalUnitsHealed", "team","numDeaths", "totalDamageTaken", "item0", "physicalDamageTaken"
]


    def loadInfo(self):
        name=self.name
        content = json.loads(urllib2.urlopen("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"+name+api_key).read()) #1
        summonerID = content[name.lower()]["id"]
        print summonerID
        game_records = json.loads(urllib2.urlopen("https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/"+str(summonerID)+"/recent"+api_key).read())
        print(str(game_records))
        exporter = ExportCSV.CsvExporter("test.tsv",self.headers)

        for game_info in game_records['games']:
            stat_dict = dict(game_info['stats'])
            game_info.pop("fellowPlayers",None) #we don't care about fellow players
            game_info.pop("stats",None) #we want to flatten stats
            game_dictionary = game_info.copy()
            game_dictionary.update(stat_dict)
            exporter.write_row(game_dictionary)



Collector("enter_Username_here").loadInfo()





