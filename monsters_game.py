def weak_monster(monsters):
    monster_health = [m[0] for m in monsters]
    attack_monster = min(monster_health)
    pos = monster_health.index(attack_monster)
    return attack_monster, pos


def main(monsters):
    """
    See https://codeforces.com/contest/1334/problem/C
    >>> main([(7, 15), (2, 14), (5, 3)])
    6
    """
    shot_result = []
    while len(monsters) > 0:
        shot, pos = weak_monster((monsters))
        shot_result.append(shot)
        if pos < len(monsters)-1:
            monsters[pos+1][0] -= monsters[pos][1]
        else:
            monsters[0][0] -= monsters[pos][1]
        monsters.remove(monsters[pos])
    shot_result = [s for s in shot_result if s >0]
    return sum(shot_result)

print(main([[1,2], [2,4], [5,3]]))
