import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw4_extra.settings")

import django
django.setup()

from myapp.models import Color, State, Team, Player

def addState():
    f = open('state.txt')
    for l in f:
        omit, name = l.split(' ')
        obj = State(name = name[:-1])
        obj.save()
    f.close()
    return

def addColor():
    f = open('color.txt')
    for l in f:
        omit, name = l.split(' ')
        obj = Color(name = name[:-1])
        obj.save()
    f.close()
    return

def addTeam():
    f = open('team.txt')
    for l in f:
        omit, name, state_id, color_id, wins, losses = l.split(' ')
        obj = Team(name = name, state_id = State.objects.get(state_id= state_id), color_id = Color.objects.get(color_id= color_id), wins = wins, losses = losses)
        obj.save()
    f.close()
    return

def addPlayer():
    f = open('player.txt')
    for l in f:
        omit, team_id, uniform_num, first_name, last_name, mpg, ppg, rpg, apg, spg, bpg = l.split(' ')
        obj = Player(team_id=Team.objects.get(team_id=team_id), uniform_num=uniform_num, first_name=first_name, last_name=last_name, mpg=mpg, ppg = ppg, rpg = rpg, apg = apg, spg = spg, bpg = bpg)
        obj.save()
    f.close()
    return

def query1(use_mpg, min_mpg, max_mpg,
            use_ppg, min_ppg, max_ppg,
            use_rpg, min_rpg, max_rpg,
            use_apg, min_apg, max_apg,
            use_spg, min_spg, max_spg,
            use_bpg, min_bpg, max_bpg):
    mod = Player.objects
    used = 0
    if use_mpg==1:
        mod = mod.filter(mpg__gte=min_mpg)
        used = 1
        mod = mod.filter(mpg__lte=max_mpg)

    if use_ppg==1:
        mod = mod.filter(ppg__gte=min_ppg)
        used = 1
        mod = mod.filter(ppg__lte=max_ppg)

    if use_rpg==1:
        mod = mod.filter(rpg__gte=min_rpg)
        used = 1
        mod = mod.filter(rpg__lte=max_rpg)

    if use_apg==1:
        mod = mod.filter(apg__gte=min_apg)
        used = 1
        mod = mod.filter(apg__lte=max_apg)

    if use_spg==1:
        mod = mod.filter(spg__gte=min_spg)
        used = 1
        mod = mod.filter(spg__lte=max_spg)

    if use_bpg==1:
        mod = mod.filter(bpg__gte=min_bpg)
        used = 1
        mod = mod.filter(bpg__lte=max_bpg)

    if used == 0:
        mod = Player.objects.all()

    flag = 0
    for a in mod:
        if flag == 0:
            print("PLAYER_ID TEAM_ID UNIFORM_NUM FIRST_NAME LAST_NAME MPG PPG RPG APG SPG BPG")
        print(a.player_id, a.team_id_id, a.uniform_num, a.first_name, a.last_name, a.mpg, a.ppg, a.rpg, a.apg, a.spg, a.bpg)
        flag = 1

def query2(uni_color):
    mod = Team.objects
    ans = mod.filter(color_id__name=uni_color)
    flag = 0
    for a in ans:
        if flag == 0:
            print("NAME")
        print(a.name)
        flag = 1

def query3(teamName):
    mod = Player.objects
    ans = mod.filter(team_id__name=teamName).order_by('-ppg')
    flag = 0
    for a in ans:
        if flag == 0:
            print("FIRST_NAME LAST_NAME")
        print(a.first_name, a.last_name)
        flag = 1

def query4(stateName, colorName):
    mod = Player.objects
    ans = mod.filter(team_id__state_id__name=stateName)
    ans = ans.filter(team_id__color_id__name=colorName)
    flag = 0
    for a in ans:
        if flag == 0:
            print("FIRST_NAME LAST_NAME UNIFORM_NUM")
        print(a.first_name, a.last_name, a.uniform_num)
        flag = 1

def query5(wins_num):
    mod = Player.objects
    ans = mod.filter(team_id__wins__gt=wins_num)
    flag = 0
    for a in ans:
        if flag == 0:
            print("FIRST_NAME LAST_NAME NAME WINS")
        print(a.first_name, a.last_name, a.team_id.name, a.team_id.wins)
        flag = 1


def main():
    addState()
    addColor()
    addTeam()
    addPlayer()
    #query1(1, 35, 40, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    #query1(0, 35, 40, 0, 0, 0, 1, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    #query2("Green")
    #query2("Orange")
    #query3("Duke")
    #query3("UNC")
    #query4("MA", "Maroon")
    #query4("NC", "DarkBlue")
    #query5(13)
    #query5(10)
if __name__ == "__main__":
    main()