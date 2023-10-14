list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = len(list_players)
# team_1 = list_players[0::2]
# team_2 = list_players[1::2]
# team_1 = list_players[0:3]
# team_2 = list_players[3:]
team_1 = list_players[0 : int(count/2)]
team_2 = list_players[int(count/2) : int(count)]
print(team_1)
print(team_2)
