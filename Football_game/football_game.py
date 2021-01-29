import csv
from tabulate import tabulate

def id_to_name(names):
    name_by_id = {}
    for row in csv.DictReader(names):
        team_ids = int(row['id'])
        team_names = row['name']
        name_by_id[team_ids] = team_names
    #team_name = name_by_id[team_id]
    #print(team_name)
    return name_by_id


#print(id_to_name(open('teams.csv')))

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
    team_name_most_goals = id_to_name(names)[team_id_most_goals]
    return team_name_most_goals


#print(most_goals(open('football_teams.csv'),open('teams.csv')))


# Какая команда имела больше всех побед за всю историю лиги?
def wins(games):
    winners = []
    team_by_wins = {}
    for row in csv.DictReader(games):
        if int(row['score'].split(':')[0]) < int(row['score'].split(':')[1]):
            winners.append(int(row['team_b']))
        elif int(row['score'].split(':')[0]) > int(row['score'].split(':')[1]):
            winners.append(int(row['team_a']))
        else:
            pass
    for w in winners:
        if w in team_by_wins:
            team_by_wins[w] += 1
        else:
            team_by_wins[w] = 1
    return team_by_wins

def most_wins(games, names):
    team_by_wins = wins(games)
    print(team_by_wins)
    team_id_most_wins = max(team_by_wins, key=team_by_wins.get)
    team_name_most_wins = id_to_name(names)[team_id_most_wins]
    return team_name_most_wins


#print(most_wins(open('football_teams.csv'),open('teams.csv')))

# Какая разница в количестве побед между лучшей и второй командой?
def diff_wins(games):
    team_by_wins = wins(games)
    team_id_most_wins = max(team_by_wins, key=team_by_wins.get)
    team_most_wins = max(team_by_wins.values())
    team_by_wins.pop(team_id_most_wins)
    team_id_most_wins2 = max(team_by_wins, key=team_by_wins.get)
    team_most_wins2 = max(team_by_wins.values())
    difference_win = team_most_wins - team_most_wins2
    return difference_win

#print(diff_wins(open('football_teams.csv')))

# Какие 10 команд имели больше всех побед в 2016ом году?
def ten_winners(games, names):
    team_by_wins_2016 = {}
    winners_2016 = []
    for row in csv.DictReader(games):
        if '2016' in row['date']:
            if int(row['score'].split(':')[0]) < int(row['score'].split(':')[1]):
                winners_2016.append(int(row['team_b']))
            elif int(row['score'].split(':')[0]) > int(row['score'].split(':')[1]):
                winners_2016.append(int(row['team_b']))
            else:
                pass
    for w in winners_2016:
        if w in team_by_wins_2016:
            team_by_wins_2016[w] += 1
        else:
            team_by_wins_2016[w] = 1
    #print(team_by_wins_2016)
    sorted_team2016 = sorted(team_by_wins_2016.items(), key=lambda x: x[1], reverse=True)
    best_10id_2016 = [x[0] for x in sorted_team2016[0:10]]
    best_10names_2016 = []
    print(best_10id_2016)
    all_names = id_to_name(names)
    for id in best_10id_2016:
        name = all_names[id]
        best_10names_2016.append(name)

    return best_10names_2016

#print(ten_winners(open('football_teams.csv'), open('teams.csv')))

#Пропущенный вс забитый гол
def goals(games):
    scored_goals_by_id = {}
    missed_goals_by_id = {}
    for row in csv.DictReader(games):
        scored_goals_by_id[int(row['team_a'])] = int(row['score'].split(':')[0])
        scored_goals_by_id[int(row['team_b'])] = int(row['score'].split(':')[1])
        missed_goals_by_id[int(row['team_a'])] = int(row['score'].split(':')[1])
        missed_goals_by_id[int(row['team_b'])] = int(row['score'].split(':')[0])
    return scored_goals_by_id, missed_goals_by_id
print(goals(open('football_teams.csv')))



def points(games):
    points_by_id = {}
    for row in csv.DictReader(games):
        if int(row['score'].split(':')[0]) < int(row['score'].split(':')[1]):
            key = int(row['team_b'])
            if key in points_by_id.keys():
                points_by_id[key] += 3
            else:
                points_by_id[key] = 3

        elif int(row['score'].split(':')[0]) > int(row['score'].split(':')[1]):
            key = int(row['team_a'])
            if key in points_by_id:
                points_by_id[key] += 3
            else:
                points_by_id[key] = 3
        else:
            if int(row['team_a']) in points_by_id.keys() and int(row['team_b']) in points_by_id.keys():
                points_by_id[int(row['team_a'])] +=1
                points_by_id[int(row['team_b'])] +=1
            elif int(row['team_a']) in points_by_id.keys() and int(row['team_b']) not in points_by_id.keys():
                points_by_id[int(row['team_a'])] += 1
                points_by_id[int(row['team_b'])] = 1
            elif int(row['team_a']) not in points_by_id.keys() and int(row['team_b']) in points_by_id.keys():
                points_by_id[int(row['team_a'])] = 1
                points_by_id[int(row['team_b'])] += 1
            else:
                points_by_id[int(row['team_a'])] = 1
                points_by_id[int(row['team_b'])] = 1

    return points_by_id
print(points(open('football_teams.csv')))

# Отобразить турнирную таблицу[1] всех команд игравших в 2016 году
def tournament_table(games,names):
    name_by_id = id_to_name(names)

    print(tabulate(name_by_id.items(), headers=['ID', 'Name'], tablefmt="grid"))

#print(tournament_table(open('football_teams.csv'),open('teams.csv')))
