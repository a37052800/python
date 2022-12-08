from pprint import pprint
players = {'James': 202, 'Curry': 193, 'Durant': 205, 'Jordan': 199, 'David': 211,
           'Edie': 195, 'Santi': 200, 'Jarret': 194, 'Cole': 207, 'Ryan': 192}
pprint(players)
limit = int(input("請輸入一個球員身高的門檻值:"))
result = {key: value for key, value in players.items() if value >= limit}
for player in result.items():
    print("{:<s}\t{:d}".format(player[0], player[1]))
input("Press the \"Enter\" key to continue...")