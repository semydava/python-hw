import csv
#Какая команда забила больше всех голов за всю историю лиги?
with open('football_teams.csv') as f:
    #reader = csv.DictReader(f)
    #your_list = list(reader)
    #print(your_list)
    goals_by_teams = {}
    for row in csv.DictReader(f):
        team_a_goals = int(row['score'].split(':')[0])
        team_b_goals = int(row['score'].split(':')[1])
        team_a_id = int(row['team_a'])
        team_b_id = int(row['team_b'])
        goals_by_teams[team_a_id] = goals_by_teams.get(team_a_id, 0) + team_a_goals
        if team_b_id not in goals_by_teams:
            goals_by_teams[team_b_id] = 0 + team_b_goals
        else:
            goals_by_teams[team_b_id] = goals_by_teams[team_b_id] + team_b_goals
    team_id_most_goals = max(goals_by_teams, key=goals_by_teams.get)
    #print(team_id_most_goals)
with open('teams.csv') as t:
    name_by_id = {}
    for row in csv.DictReader(t):
        team_ids = int(row['id'])
        team_names = row['name']
        name_by_id[team_ids] =  team_names
    #print(name_by_id)
    team_name_most_goals = name_by_id[team_id_most_goals]
    print(team_name_most_goals)
#Какая команда имела больше всех побед за всю историю лиги?
with open('football_teams.csv') as f:
    team_by_wins = {}
    winners = []
    for row in csv.DictReader(f):
        if int(row['score'].split(':')[0]) < int(row['score'].split(':')[1]):
            winners.append(int(row['team_b']))
        else:
            winners.append(int(row['team_a']))
    for w in winners:
        if w in team_by_wins:
            team_by_wins[w] += 1
        else:
            team_by_wins[w] = 1
    #print(team_by_wins)
    team_id_most_wins = max(team_by_wins, key=team_by_wins.get)
    team_most_wins = max(team_by_wins.values())
    team_name_most_wins = name_by_id[team_id_most_wins]
    print(team_id_most_wins,team_name_most_wins)
#Какая разница в количестве побед между лучшей и второй командой?
team_by_wins.pop(team_id_most_wins)
team_id_most_wins2 = max(team_by_wins, key=team_by_wins.get)
team_most_wins2 = max(team_by_wins.values())
difference_win = team_most_wins - team_most_wins2
print(difference_win)
#Какие 10 команд имели больше всех побед в 2016ом году?
with open('football_teams.csv') as f:
    team_by_wins_2016 = {}
    winners_2016 = []
    for row in csv.DictReader(f):
        if '2016' in row['date']:
            if int(row['score'].split(':')[0]) < int(row['score'].split(':')[1]):
                winners_2016.append(int(row['team_b']))
            else:
                winners_2016.append(int(row['team_a']))
    for w in winners_2016:
        if w in team_by_wins_2016:
            team_by_wins_2016[w] += 1
        else:
            team_by_wins_2016[w] = 1
    sorted_team2016 = sorted(team_by_wins_2016.items(), key=lambda x: x[1], reverse=True)
    best_10id_2016 = [x[0] for x in sorted_team2016[0:10]]
    best_10names_2016 = []
    for i in best_10id_2016:
        if i in name_by_id.keys():
            best_10names_2016.append(name_by_id[i])

    print(best_10names_2016)
#Отобразить турнирную таблицу[1] всех команд игравших в 2016 году
#with open('football_teams.csv') as f:
    #def points(file):













