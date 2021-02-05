import csv
from tabulate import tabulate
# Отобразить турнирную таблицу[1] всех команд игравших в 2016 году
final_dict = {}


def get_raw_data():
    needed_years = ['2016']
    teams_raw_data = get_team_stats(needed_years)

    return sorted(teams_raw_data.values(), reverse=True)


def get_table():
    raw_data = get_raw_data()
    array = []
    for row in raw_data:
        in_array = [row.team_id, row.get_name(row), row.points, row.win, row.loss, row.scored_goals, row.missed_goals]
        array.append(in_array)
    return tabulate(array, headers=('ID', 'Name', 'Points', 'W', 'L', 'SG', 'MG'))


#collect team statistics
class TeamStat:
    def __init__(self,team_id):
        self.team_id = team_id #атрибут обьекта
        self.points= 0
        self.win = 0
        self.loss = 0
        self.scored_goals = 0
        self.missed_goals = 0

    @staticmethod
    def get_name(self):
        id = self.team_id
        name = ''
        for row in csv.DictReader(open('teams.csv')):
            if row['id'] == id:
                name = row['name']
        return name

    def __add__(self, other):
        return self.team_id

    def __lt__(self, other):
        if self.points != other.points:
            return self.points < other.points
        elif find_the_score(self.team_id, other.team_id) == 0:
            if self.win != other.win:
                return self.win < other.win
            elif (self.scored_goals - self.missed_goals) != (other.scored_goals - other.missed_goals):
                return (self.scored_goals - self.missed_goals) < (other.scored_goals - other.missed_goals)
            else:
                return self.scored_goals < other.scored_goals
        else:
            if find_the_score(self.team_id, other.team_id) == 1:
                return True
            else:
                return False


def get_team_stats(years):
    stats = {}
    matches = {}

    for row in csv.DictReader(open('football_teams.csv')):
        for year in years:
            if year not in row['date']:
                continue

        a,b = row['score'].split(':')
        a,b = int(a),int(b)
        a_stats = stats.get(row['team_a'], TeamStat(row['team_a']))
        a_stats.scored_goals += a
        a_stats.missed_goals += b
        b_stats = stats.get(row['team_b'], TeamStat(row['team_b']))
        b_stats.scored_goals += b
        b_stats.missed_goals += a
        key = row['team_a'] + ':' + row['team_b']
        key_reversed = row['team_b'] + ':' + row['team_a']
        value = 0
        if key not in matches.keys() and key_reversed not in matches.keys():
            if a > b:
                value = 1
            elif b > a:
                value = - 1
            matches[key] = value
        else:
            if key in matches.keys() and key_reversed not in matches.keys():
                if a > b:
                    value += 1
                elif b > a:
                    value -= 1
            elif key not in matches.keys() and key_reversed in matches.keys():
                if a > b:
                    value -= 1
                elif b > a:
                    value += 1
                matches[key_reversed] = value

        if a < b:
            b_stats.win += 1
            a_stats.loss += 1
            b_stats.points+= 3
        elif b < a:
            a_stats.win += 1
            b_stats.loss += 1
            a_stats.points += 3
        else:
            a_stats.points+= 1
            b_stats.points+= 1
        stats[row['team_a']] = a_stats
        stats[row['team_b']] = b_stats
    final_dict.update(matches)
    return stats


def find_the_score(s,o):
    search = s + ':' + o
    reversed_search = o + ':' + s
    number = 0
    if search not in final_dict.keys() and reversed_search not in final_dict.keys():
        return False
    if search in final_dict.keys() or reversed_search in final_dict.keys():
        if search in final_dict.keys():
            number = final_dict[search]
        else:
            number = final_dict[reversed_search]
    if number < 0:
        return 1
    elif number > 0:
        return -1
    else:
        return 0


print(get_table())
