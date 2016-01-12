import urllib2
import json
import time

def getMostFrequentlyPlayed(info):
	counter=dict()
	for e in info:
		if e not in counter.keys():
			counter[e]=0
		else:
			counter[e] = counter[e]+1
	maximum=0
	name=""
	for k in counter.keys():
		if counter[k] > maximum:
			maximum = counter[k]
			name=k
	return name

api_key="?api_key=" #append your api key here

class Collector:
	def __init__ (self,name_in):
		self.name = name_in


	def loadInfo(self):
		name=self.name
		content = json.loads(urllib2.urlopen("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"+name+api_key).read()) #1
		summonerID = content[name.lower()]["id"]
		print summonerID

		currentgame=json.loads(urllib2.urlopen("https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/"+str(summonerID)+api_key).read()) #2

		players = currentgame["participants"]

		player_records=dict()
		counter=0
		for player in players:
			player_records[counter]=list()

			player_name = str(player["summonerName"])
			summonerId = str(player["summonerId"])
			teamId = str(player["teamId"])
			game_records = json.loads(urllib2.urlopen("https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/"+summonerId+"/recent"+api_key).read())
			win = 0
			playerPosition=[]
			playerRole=[]
			player_info=[]
			for game in game_records["games"]:
				temp1=""
				if game["stats"]["win"]:
					win = win+1
					temp1="win"
				else:
					temp1="loss"
				try:			
					if game["stats"]["playerRole"] == 1:
						playerRole.append("Duo")
						temp1=temp1+"-"+"Duo"
					elif game["stats"]["playerRole"] == 2:
						playerRole.append("Support")
						temp1=temp1+"-"+"Support"
					elif game["stats"]["playerRole"] == 3:
						playerRole.append("Carry")
						temp1=temp1+"-"+"Carry"
					elif game["stats"]["playerRole"] == 4:
						playerRole.append("Solo")
						temp1=temp1+"-"+"Solo"

					if game["stats"]["playerPosition"] == 1:
						playerPosition.append("Top")
						temp1=temp1+"-"+"Top"
					elif game["stats"]["playerPosition"] == 2:
						playerPosition.append("Mid")
						temp1=temp1+"-"+"Mid"
					elif game["stats"]["playerPosition"] == 3:
						playerPosition.append("Jungle")
						temp1=temp1+"-"+"Jungle"
					elif game["stats"]["playerPosition"] == 4:
						playerPosition.append("Bot")
						temp1=temp1+"-"+"Bot"
					player_info.append(temp1)
				except:
					pass

			player_records[counter].append(player_name)
			player_records[counter].append(float(win)/10)
			player_records[counter].append(str(getMostFrequentlyPlayed(playerPosition)))
			player_records[counter].append(str(getMostFrequentlyPlayed(playerRole)))
			player_records[counter].append(str(player_info))
			counter=counter+1
			time.sleep(1)
		return player_records
				

#print currentgame



