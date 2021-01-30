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
    # print(team_by_wins)
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
    # print(best_10id_2016)
    all_names = id_to_name(names)
    for id in best_10id_2016:
        name = all_names[id]
        best_10names_2016.append(name)

    return best_10names_2016

#print(ten_winners(open('football_teams.csv'), open('teams.csv')))




# Отобразить турнирную таблицу[1] всех команд игравших в 2016 году
def get_table():
    teams_raw_data = get_teams_raw_data(open('teams.csv'))
    out = {}

    for id, values in teams_raw_data.items():
        points = values['points']
        position = int(get_position(points, id))
        if position in out.keys():
            i = 1
            while position + i in out.keys():
                i += 1
            position = position + i
            if position not in out.keys():
                out[position] = int(id)
                # print(out)
        else:
            out[position] = int(id)
    # print(out)
    out = sorted(out.items())
    return out

#get team position in the final table
def get_position(points, id):
    teams_raw_data = get_teams_raw_data(open('teams.csv'))
    position = 1
    for current_id, values in teams_raw_data.items():
        if values['points'] > points:
            position += 1
        elif values['points'] == points:
            if id in values.keys():
                wins_current = values['wins_record'][id]
                wins_requested = get_wins_by_competitor(id, current_id)
                if wins_requested < wins_current:
                    position += 1
                elif wins_current == wins_requested:
                    current_general_wins = values['wins']
                    requested_general_wins = get_field_by_team_id(id, 'wins')
                    if requested_general_wins < current_general_wins:
                        position += 1
                    elif current_general_wins == requested_general_wins:
                        current_goal_diff = values['wins']
                        requested_goal_diff = get_field_by_team_id(id, 'goals_difference')
                        if requested_goal_diff < current_goal_diff:
                            position += 1
                        elif current_goal_diff == requested_goal_diff:
                            current_scored_goals = values['scored_goals']
                            requested_scored_goals = get_field_by_team_id(id, 'scored_goals')
                            if requested_scored_goals < current_scored_goals:
                                position += 1
    # print(position)
    return position

#get wins in match with particular competitor
def get_wins_by_competitor(team_id, competitor_id):
    teams_raw_data = get_teams_raw_data(open('teams.csv'))
    wins = 0
    for id, values in teams_raw_data.items():
        if id == team_id and competitor_id in values['wins_record'].keys():
            wins = values['wins_record'][competitor_id]
    return wins

#get the value from stats by field
def get_field_by_team_id(team_id, field):
    teams_raw_data = get_teams_raw_data(open('teams.csv'))
    value = 0
    for id, values in teams_raw_data.items():
        if id == team_id and field in values.keys():
            value = values[field]
    return value

#get raw data with name
def get_teams_raw_data(names):
    raw_table = {}
    for row in csv.DictReader(names):
        raw_table[row['id']] = get_team_stats(row['id'])
        raw_table[row['id']]['name'] = row['name']
    return raw_table

#collect team statistics
def get_team_stats(id):
    stats = {}
    win = 0
    draws = 0
    losses = 0
    scored_goals = 0
    missed_goals = 0
    for row in csv.DictReader(open('football_teams.csv')):
        if '2016' not in row['date']:
            print('load' + id + row['team_b'])
            if id == row['team_b'] or id == row['team_a']:

                if 'wins_record' not in stats.keys():
                    stats['wins_record'] = {}

                if id == row['team_b']:
                    scored_goals += int(row['score'].split(':')[1])
                    missed_goals += int(row['score'].split(':')[0])
                else:
                    scored_goals += int(row['score'].split(':')[0])
                    missed_goals += int(row['score'].split(':')[1])

                if (id == row['team_a'] and int(row['score'].split(':')[0]) > int(row['score'].split(':')[1])) or (
                        id == row['team_b'] and int(row['score'].split(':')[0]) < int(row['score'].split(':')[1])):
                    win += 1
                    if id == row['team_b']:
                        if row['team_a'] in stats.keys():
                            stats['wins_record'][row['team_a']] += 1
                        else:
                            stats['wins_record'][row['team_a']] = 1
                    else:
                        if row['team_b'] in stats.keys():
                            stats['wins_record'][row['team_b']] += 1
                        else:
                            stats['wins_record'][row['team_b']] = 1

                elif int(row['score'].split(':')[0]) == int(row['score'].split(':')[1]):
                    draws += 1
                else:
                    losses += 1
    stats['wins'] = win
    stats['losses'] = losses
    stats['draws'] = draws
    stats['scored_goals'] = scored_goals
    stats['goals_difference'] = scored_goals - missed_goals
    stats['points'] = int(stats['wins']) * 3 + int(stats['draws'])

    return stats



# def prn():
    # return get_team_stats(87)
print(get_table())
    # print(get_team_wins(open('football_teams.csv')))
#def tournament_table(games,names):
# print(get_team_stats('87'))
    #name_by_id = id_to_name(names)

    #print(tabulate(name_by_id.items(), headers=['ID', 'Name'], tablefmt="grid"))

#print(tournament_table(open('football_teams.csv'),open('teams.csv')))
