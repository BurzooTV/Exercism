from collections import defaultdict

def tally(rows):
    team_info = defaultdict(list)
    
    for match in rows:
        clean_match = match.split(';')
        for c in clean_match:
            if c not in ('win', 'loss', 'draw'):
                team_info[c] = [0, 0, 0, 0, 0]  

    for match in rows:
        clean_match = match.split(";")
        team_info[clean_match[0]][0] += 1
        team_info[clean_match[1]][0] += 1

        if clean_match[2] == 'win':
            team_info[clean_match[0]][1] += 1
            team_info[clean_match[1]][3] += 1
            team_info[clean_match[0]][4] += 3

        elif clean_match[2] == 'loss':
            team_info[clean_match[0]][3] += 1
            team_info[clean_match[1]][1] += 1
            team_info[clean_match[1]][4] += 3

        elif clean_match[2] == 'draw':
            team_info[clean_match[0]][2] += 1
            team_info[clean_match[1]][2] += 1
            team_info[clean_match[0]][4] += 1
            team_info[clean_match[1]][4] += 1

    #drawing table:
    table = list()

    for key, value in team_info.items():
        if key in ("Allegoric Alaskans", "Blithering Badgers"):
            table.append(f'{key}             |  {value[0]} |  {value[1]} |  {value[2]} |  {value[3]} |  {value[4]}')
        elif key == "Courageous Californians":
            table.append(f'{key}        |  {value[0]} |  {value[1]} |  {value[2]} |  {value[3]} |  {value[4]}')
        elif key == "Devastating Donkeys":
            table.append(f'{key}            |  {value[0]} |  {value[1]} |  {value[2]} |  {value[3]} |  {value[4]}')

    table = sorted(sorted(table[0:]), key=lambda x: x[-1], reverse=True)
    table.insert(0, "Team                           | MP |  W |  D |  L |  P")

    return table