def alternatingSums(a):
    team1 = []
    team2 = []
    for e,weight in enumerate(a):
        if e%2 == 0:
            team1.append(weight)
        else:
            team2.append(weight)
    return sum(team1), sum(team2)

alternatingSums([50,60,60,45,70])