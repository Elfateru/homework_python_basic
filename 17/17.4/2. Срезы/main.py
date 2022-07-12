members = int(input('Кол-во участников: '))
teams = int(input('Кол-во человек в команде: '))
member = []
num = 1
if members % teams == 0:
    for _ in range(members // teams):
        member.append(list(range(num, num + teams)))
        num += teams
    print(member)
else:
    print(members, 'участников невозможно поделить на команды по', teams, 'человек!')