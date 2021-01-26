import csv


def id_to_name(names, team_id):
    print(team_id)
    name_by_id = {}
    for row in csv.DictReader(names):
        team_ids = int(row['id'])
        team_names = row['name']
        name_by_id[team_ids] = team_names
    team_name = name_by_id[team_id]
    print(team_name)
    return team_name


# print(id_to_name(open('teams.csv'),950))

# Какая команда забила больше всех голов за всю историю лиги?
def most_goals(games, names):
    goals_by_teams = {}
    for row in csv.DictReader(games):
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
    team_name_most_goals = id_to_name(names, team_id_most_goals)
    return team_name_most_goals


# print(most_goals(open('football_teams.csv'),open('teams.csv')))
# with open('teams.csv') as t:
# name_by_id = {}
# for row in csv.DictReader(t):
# team_ids = int(row['id'])
# team_names = row['name']
# name_by_id[team_ids] =  team_names
# print(name_by_id)
# team_name_most_goals = name_by_id[team_id_most_goals]
# print(team_name_most_goals)

# Какая команда имела больше всех побед за всю историю лиги?
def most_wins(games, names):
    team_by_wins = {}
    winners = []
    for row in csv.DictReader(games):
        if int(row['score'].split(':')[0]) < int(row['score'].split(':')[1]):
            winners.append(int(row['team_b']))
        else:
            winners.append(int(row['team_a']))
    for w in winners:
        if w in team_by_wins:
            team_by_wins[w] += 1
        else:
            team_by_wins[w] = 1
    team_id_most_wins = max(team_by_wins, key=team_by_wins.get)
    team_name_most_wins = id_to_name(names, team_id_most_wins)
    return team_name_most_wins


# print(most_wins(open('football_teams.csv'),open('teams.csv')))

# Какая разница в количестве побед между лучшей и второй командой?
def diff_wins(games):
    team_by_wins = {}
    winners = []
    for row in csv.DictReader(games):
        if int(row['score'].split(':')[0]) < int(row['score'].split(':')[1]):
            winners.append(int(row['team_b']))
        else:
            winners.append(int(row['team_a']))
    for w in winners:
        if w in team_by_wins:
            team_by_wins[w] += 1
        else:
            team_by_wins[w] = 1
    team_id_most_wins = max(team_by_wins, key=team_by_wins.get)
    team_most_wins = max(team_by_wins.values())
    team_by_wins.pop(team_id_most_wins)
    team_id_most_wins2 = max(team_by_wins, key=team_by_wins.get)
    team_most_wins2 = max(team_by_wins.values())
    difference_win = team_most_wins - team_most_wins2
    return difference_win


# print(diff_wins(open('football_teams.csv')))

# Какие 10 команд имели больше всех побед в 2016ом году?
def ten_winners(games, names):
    team_by_wins_2016 = {}
    winners_2016 = []
    for row in csv.DictReader(games):
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
    i = 0

    for id in sorted_team2016[0:10][0]:
        id_to_name(names, 647)
    best_10names_2016.append(id_to_name(names,id))

    return best_10names_2016


print(ten_winners(open('football_teams.csv'), open('teams.csv')))

# Отобразить турнирную таблицу[1] всех команд игравших в 2016 году
# def points(file):