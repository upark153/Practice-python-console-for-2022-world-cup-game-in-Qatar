import random

def group_fight_16(round_16):

    win_8 = []
    oneSeed = ["파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공"]  # 1시드 이길 확률 70%, 질 확률 30%
    twoSeed = ["파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공", "빨간공"]

    # print(f'\n{team_fight}조 16강 경기 시작합니다.\n')
    i = 1
    for j in range(0, 8, 2):
        print(f'\n16강 {i}번째 경기\n{team_fight[j]}조 1위 : {round_16[j * 2][0]} vs {team_fight[i * 2 - 1]}조 2위 : {round_16[j * 2 + 3][0]} ')
        for k in range(0, 10):
            print(f'\n{k * 10}분 지났습니다.\n')
            a = random.choice(oneSeed)
            b = random.choice(twoSeed)
            if a == "파란공" and b == "빨간공":
                round_16[j*2][2] += 1
                print("화려한 중거리슛으로 경기를 장식합니다.")
            if b == "파란공" and a == "빨간공":
                round_16[j*2+3][2] += 1
                print("헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
            if a == "빨간공" and b == "빨간공":
                print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
            if a == "파란공" and b == "파란공":
                print("선수들 이제는 더 분발해야 됩니다.")
            round_16[j*2][3] += round_16[j*2][2]
            round_16[j*2+3][3] += round_16[j*2+3][2]
        if round_16[j*2][2] > round_16[j*2+3][2]:
            print(f"\n{i}번째 경기 : \n {round_16[j*2][0]}가 {round_16[j*2][2]} 대 {round_16[j*2+3][2]}로 이겼습니다. 8강 진출합니다.\n")
            win_8.append(round_16[j*2])
        elif round_16[j*2][2] < round_16[j*2+3][2]:
            print(f"\n{i}번째 경기 : \n {round_16[j*2+3][0]} {round_16[j*2+3][2]} 대 {round_16[j*2][2]}로 이겼습니다. 8강 진출합니다.\n")
            win_8.append(round_16[j*2+3])
        else:
            print("동점입니다. 재경기 진행합니다.")
            while True:
                a = random.choice(oneSeed)
                b = random.choice(twoSeed)
                if a == "파란공" and b == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*2][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2])
                    break
                elif b == "파란공" and a == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*2+3][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2 + 3])
                    break
        i += 1
    i = 5
    for j in range(1, 8, 2):
        print(f'\n16강 {i}번째 경기\n{team_fight[j]}조 1위 : {round_16[j * 2][0]} vs {team_fight[j - 1]}조 2위 : {round_16[j * 2 - 1][0]} ')
        for k in range(0, 10):
            print(f'\n{k * 10}분 지났습니다.\n')
            a = random.choice(oneSeed)
            b = random.choice(twoSeed)
            if a == "파란공" and b == "빨간공":
                round_16[j*2][2] += 1
                print("화려한 중거리슛으로 경기를 장식합니다.")
            if b == "파란공" and a == "빨간공":
                round_16[j*2-1][2] += 1
                print("헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
            if a == "빨간공" and b == "빨간공":
                print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
            if a == "파란공" and b == "파란공":
                print("선수들 이제는 더 분발해야 됩니다.")
            round_16[j*2][3] += round_16[j*2][2]
            round_16[j*2-1][3] += round_16[j*2-1][2]
        if round_16[j*2][2] > round_16[j*2-1][2]:
            print(f"\n{i}번째 경기 : \n {round_16[j*2][0]}가 {round_16[j*2][2]} 대 {round_16[j*2-1][2]}로 이겼습니다. 8강 진출합니다.\n")
            win_8.append(round_16[j*2])
        elif round_16[j*2][2] < round_16[j*2-1][2]:
            print(f"\n{i}번째 경기 : \n {round_16[j*2-1][0]} {round_16[j*2-1][2]} 대 {round_16[j*2][2]}로 이겼습니다. 8강 진출합니다.\n")
            win_8.append(round_16[j*2-1])
        else:
            print("동점입니다. 재경기 진행합니다.")
            while True:
                a = random.choice(oneSeed)
                b = random.choice(twoSeed)
                if a == "파란공" and b == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*2][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2])
                    break
                elif b == "파란공" and a == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*-1][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2 -1])
                    break
        i += 1
    print("\n카타르 월드컵 16강 경기 선수들 부상 없이 무사히 종료되었습니다.\n")
    print("8강 진출을 위해 골 득점과 합산을 다시 초기화하겠습니다. \n")
    for i in range(0, 8):
        for j in range(1, 4):
            win_8[i][j] = 0
    for i in range(0, 8):
        print(win_8[i])
    print("\n카타르 월드컵 8강을 시작 하겠습니다.\n")
    print("캡틴 박지성 해설위원, 8강에 진출한 국가들의 승률은 어떻게 되는 건가요?\n")
    print("8강 이후부터는 여러가지 변수가 많아 승률을 예측하기 어렵다고 볼 수 있습니다.\n")
    print("이에 따라 각 국가별의 승률은 70%로 고정되어 경기가 진행됩니다.\n")
    print("그렇군요. 각 국가 별 운명의 여신이 함께하길 기원합니다.\n")
    # print(f'1번째 경기 : {win_8[0]} vs {win_8[1]}')
    # print(f'2번째 경기 : {win_8[4]} vs {win_8[5]}')
    # print(f'3번째 경기 : {win_8[2]} vs {win_8[3]}')
    # print(f'4번째 경기 : {win_8[6]} vs {win_8[7]}')
    win_4 = []
    i=1
    for j in range(0, 13, 4):
        if i>=3:
            print(f'8강 {i}번째 경기 : {win_8[j-6][0]} vs {win_8[(j+1)-6][0]}')
            for k in range(0, 10):
                print(f'\n{k * 10}분 지났습니다.\n')
                a = random.choice(oneSeed)
                b = random.choice(oneSeed)
                if a == "파란공" and b == "빨간공":
                    win_8[j-6][2] += 1
                    print("화려한 중거리슛으로 경기를 장식합니다.")
                if b == "파란공" and a == "빨간공":
                    win_8[(j+1)-6][2] += 1
                    print("헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
                if a == "빨간공" and b == "빨간공":
                    print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
                if a == "파란공" and b == "파란공":
                    print("선수들 이제는 더 분발해야 됩니다.")
                win_8[j-6][3] += win_8[j-6][2]
                win_8[(j+1)-6][3] += win_8[(j+1)-6][2]
            if win_8[j-6][2] > win_8[(j+1)-6][2]:
                print(f"\n{i}번째 경기 : \n {win_8[j-6][0]}가 {win_8[j-6][2]} 대 {win_8[(j+1)-6][2]}로 이겼습니다. 4강 진출합니다.\n")
                win_4.append(win_8[j-6])
            elif win_8[j-6][2] < win_8[(j+1)-6][2]:
                print(f"\n{i}번째 경기 : \n {win_8[(j+1)-6][0]} {win_8[(j+1)-6][2]} 대 {win_8[j-6][2]}로 이겼습니다. 4강 진출합니다.\n")
                win_4.append(win_8[(j+1)-6])
            else:
                print("동점입니다. 재경기 진행합니다.")
                while True:
                    a = random.choice(oneSeed)
                    b = random.choice(oneSeed)
                    if a == "파란공" and b == "빨간공":
                        print(f"\n{i}번째 경기 : \n {win_8[j-6][0]} 4강 진출합니다. ")
                        win_4.append(win_8[j-6])
                        break
                    elif b == "파란공" and a == "빨간공":
                        print(f"\n{i}번째 경기 : \n {win_8[(j+1)-6][0]} 4강 진출합니다. ")
                        win_4.append(win_8[(j+1)-6])
                        break
        else:
            print(f'8강{i}번째 경기 : {win_8[j][0]} vs {win_8[j+1][0]}')
            for k in range(0, 10):
                print(f'\n{k * 10}분 지났습니다.\n')
                a = random.choice(oneSeed)
                b = random.choice(oneSeed)
                if a == "파란공" and b == "빨간공":
                    win_8[j][2] += 1
                    print("화려한 중거리슛으로 경기를 장식합니다.")
                if b == "파란공" and a == "빨간공":
                    win_8[j+1][2] += 1
                    print("헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
                if a == "빨간공" and b == "빨간공":
                    print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
                if a == "파란공" and b == "파란공":
                    print("선수들 이제는 더 분발해야 됩니다.")
                win_8[j][3] += win_8[j][2]
                win_8[j+1][3] += win_8[j+1][2]
            if win_8[j][2] > win_8[j+1][2]:
                print(f"\n{i}번째 경기 : \n {win_8[j][0]}가 {win_8[j][2]} 대 {win_8[j+1][2]}로 이겼습니다. 4강 진출합니다.\n")
                win_4.append(win_8[j])
            elif win_8[j][2] < win_8[j+1][2]:
                print(f"\n{i}번째 경기 : \n {win_8[j+1][0]} {win_8[j+1][2]} 대 {win_8[j][2]}로 이겼습니다. 4강 진출합니다.\n")
                win_4.append(win_8[j+1])
            else:
                print("동점입니다. 재경기 진행합니다.")
                while True:
                    a = random.choice(oneSeed)
                    b = random.choice(oneSeed)
                    if a == "파란공" and b == "빨간공":
                        print(f"\n{i}번째 경기 : \n {win_8[j][0]} 4강 진출합니다. ")
                        win_4.append(win_8[j])
                        break
                    elif b == "파란공" and a == "빨간공":
                        print(f"\n{i}번째 경기 : \n {win_8[j+1][0]} 4강 진출합니다. ")
                        win_4.append(win_8[j+1])
                        break
        i += 1
    print("\n카타르 월드컵 8강 경기 선수들 부상 없이 무사히 종료되었습니다.\n")
    print("4강 진출을 위해 골 득점과 합산을 다시 초기화하겠습니다. \n")
    for i in range(0, 4):
        for j in range(1, 4):
            win_4[i][j] = 0
    for i in range(0, 4):
        print(win_4[i])
    print("\n카타르 월드컵 준결승전을 시작 하겠습니다.\n")
    print("캡틴 박지성 해설위원, 준결승전에 진출한 국가들의 승률은 어떻게 되는 건가요?\n")
    print("준결승전 이후부터는 여러가지 변수가 많아 승률을 예측하기 어렵다고 볼 수 있습니다.\n")
    print("이에 따라 각 국가별의 승률은 70%로 고정되어 경기가 진행됩니다.\n")
    print("그렇군요. 각 국가 별 운명의 여신이 함께하길 기원합니다.\n")
    # print(f'준결승전 1경기 {win_4[0][0]} vs {win_4[1][0]}')
    # print(f'준결승전 2경기 {win_4[2][0]} vs {win_4[3][0]}')
    win_2= []
    i=1
    for j in range(0, 3, 2):
        print(f'준결승전 {i}번째 경기 : {win_4[j][0]} vs {win_4[j+1][0]}')
        for k in range(0, 10):
            print(f'\n{k * 10}분 지났습니다.\n')
            a = random.choice(oneSeed)
            b = random.choice(oneSeed)
            if a == "파란공" and b == "빨간공":
                win_4[j][2] += 1
                print("화려한 중거리슛으로 경기를 장식합니다.")
            if b == "파란공" and a == "빨간공":
                win_4[j+1][2] += 1
                print("헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
            if a == "빨간공" and b == "빨간공":
                print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
            if a == "파란공" and b == "파란공":
                print("선수들 이제는 더 분발해야 됩니다.")
            win_4[j][3] += win_4[j][2]
            win_4[j + 1][3] += win_4[j + 1][2]
        if win_4[j][2] > win_4[j + 1][2]:
            print(f"\n{i}번째 경기 : \n {win_4[j][0]}가 {win_4[j][2]} 대 {win_4[j + 1][2]}로 이겼습니다. 결승전 진출합니다.\n")
            win_2.append(win_4[j])
        elif win_4[j][2] < win_4[j + 1][2]:
            print(f"\n{i}번째 경기 : \n {win_4[j + 1][0]} {win_4[j + 1][2]} 대 {win_4[j][2]}로 이겼습니다. 결승전 진출합니다.\n")
            win_2.append(win_4[j + 1])
        else:
            print("동점입니다. 재경기 진행합니다.")
            while True:
                a = random.choice(oneSeed)
                b = random.choice(oneSeed)
                if a == "파란공" and b == "빨간공":
                    print(f"\n{i}번째 경기 : \n {win_4[j][0]} 결승전 진출합니다. ")
                    win_2.append(win_4[j])
                    break
                elif b == "파란공" and a == "빨간공":
                    print(f"\n{i}번째 경기 : \n {win_4[j + 1][0]} 결승전 진출합니다. ")
                    win_2.append(win_4[j + 1])
                    break
        i += 1
    print("\n카타르 월드컵 준결승전 경기 선수들 부상 없이 무사히 종료되었습니다.\n")
    print("결승전 진출을 위해 골 득점과 합산을 다시 초기화하겠습니다. \n")
    for i in range(0, 2):
        for j in range(1, 4):
            win_2[i][j] = 0
    for i in range(0, 2):
        print(win_2[i])
    print("\n카타르 월드컵 결승전을 시작 하겠습니다.\n")
    print("캡틴 박지성 해설위원, 2022 카타르 월드컵도 벌써 막바지에 이르렀습니다.\n")
    print("월드컵 우승은 어느 국가가 하실것이라고 생각하십니까?\n")
    print("개인적으로 월드컵 우승은 참여한 모두에게 돌리고 싶네요 \n")
    print("그렇군요. 정말 고생하셨습니다.\n")
    win_1 = []
    print(f'결승전 마지막 경기 : {win_2[0][0]} vs {win_2[1][0]}')
    for k in range(0, 10):
        print(f'\n{k * 10}분 지났습니다.\n')
        a = random.choice(oneSeed)
        b = random.choice(oneSeed)
        if a == "파란공" and b == "빨간공":
            win_2[0][2] += 1
            print("화려한 중거리슛으로 경기를 장식합니다.")
        if b == "파란공" and a == "빨간공":
            win_2[1][2] += 1
            print("헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        win_2[0][3] += win_2[0][2]
        win_2[1][3] += win_2[1][2]
    if win_2[0][2] > win_2[1][2]:
        print(f"\n결승전 마지막 경기 : \n {win_2[0][0]}가 {win_2[0][2]} 대 {win_2[1][2]}로 이겼습니다. 카타르월드컵 트로피를 거머쥡니다. 축하합니다.\n")
        win_1.append(win_2[0])
    elif win_2[0][2] < win_2[1][2]:
        print(f"\n결승전 마지막 경기: \n {win_2[1][0]} {win_2[1][2]} 대 {win_2[0][2]}로 이겼습니다. 카타르월드컵 트로피를 거머쥡니다. 축하합니다.\n")
        win_1.append(win_2[1])
    else:
        print("동점입니다. 재경기 진행합니다.")
        while True:
            a = random.choice(oneSeed)
            b = random.choice(oneSeed)
            if a == "파란공" and b == "빨간공":
                print(f"\n결승전 마지막 경기 : \n {win_2[0][0]} 카타르월드컵 트로피를 거머쥡니다. 축하합니다. ")
                win_1.append(win_2[0])
                break
            elif b == "파란공" and a == "빨간공":
                print(f"\n결승전 마지막 경기 : \n {win_2[1][0]}  카타르월드컵 트로피를 거머쥡니다. 축하합니다. ")
                win_1.append(win_2[1])
                break
    print("\n카타르 월드컵 결승전 경기 ! 선수들 부상 없이 무사히 종료되었습니다.\n")
    print(f'{win_1[0][0]}가 우승을 차지했습니다. 정말 고생하셨습니다.')

def group_fight_32(team_fight, Team):

    oneSeed = ["파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공"]  # 1시드 이길 확률 70%, 질 확률 30%
    twoSeed = ["파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공", "빨간공"]  # 2시드 이길 확률 60%, 질 확률 40%
    threeSeed = ["파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공"]  # 3시드 이길 확률 40%, 질 확률 60%
    fourSeed = ["파란공", "파란공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공"]

    print(f'\n{team_fight}조 예선 경기 시작합니다.\n')
    for i in range(0, 10):
        print(f'\n{i * 10}분 지났습니다.\n')
        a = random.choice(oneSeed)
        b = random.choice(twoSeed)
        if a == "파란공" and b == "빨간공":
            Team[0][2] += 1
            print("화려한 중거리슛으로 경기를 장식합니다.")
        if b == "파란공" and a == "빨간공":
            Team[1][2] += 1
            print("헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        Team[0][3] += Team[0][2]
        Team[1][3] += Team[1][2]
    if Team[0][2] > Team[1][2]:
        print(f"\n1번째 경기 : \n {Team[0][0]}가 {Team[0][2]} 대 {Team[1][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[0][1] += 3
    elif Team[0][2] < Team[1][2]:
        print(f"\n1번째 경기 : \n {Team[1][0]} {Team[1][2]} 대 {Team[0][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[1][1] += 3
    else:
        print("\n1번째 경기 : 동점입니다. 승점 1점씩 추가합니다.\n")
        Team[0][1] += 1
        Team[1][1] += 1

    Team[0][2] = 0
    Team[1][2] = 0

    for i in range(0, 10):
        print(f'\n{i * 10}분 지났습니다.\n')
        a = random.choice(oneSeed)
        b = random.choice(threeSeed)
        if a == "파란공" and b == "빨간공":
            Team[0][2] += 1
            print("절묘한 감아차기 슛! 꼴!! 저 선수 포기하지 않는 정신이 결국 골망을 흔들었습니다.")
        if b == "파란공" and a == "빨간공":
            Team[2][2] += 1
            print("오버헤드킥! 그는 마치 온몸을 자유자재로 조종하는 것 같군요. ")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        Team[0][3] += Team[0][2]
        Team[2][3] += Team[2][2]
    if Team[0][2] > Team[2][2]:
        print(f"\n2번째 경기 : \n {Team[0][0]} {Team[0][2]} 대 {Team[2][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[0][1] += 3
    elif Team[0][2] < Team[2][2]:
        print(f"\n2번째 경기 : \n {Team[2][0]} {Team[2][2]} 대 {Team[0][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[2][1] += 3
    else:
        print("\na조 2번째 경기: 동점입니다. 승점 1점씩 추가합니다.\n")
        Team[0][1] += 1
        Team[2][1] += 1

    Team[0][2] = 0
    Team[2][2] = 0

    for i in range(0, 10):
        print(f'\n{i * 10}분 지났습니다.\n')
        a = random.choice(oneSeed)
        b = random.choice(fourSeed)
        if a == "파란공" and b == "빨간공":
            Team[0][2] += 1
            print("무섭도록 예리한 패스로 마무리 짓네요. 그들은 마치 형제같군요")
        if b == "파란공" and a == "빨간공":
            Team[3][2] += 1
            print("그의 슛은 너무 빨라 보이지도 않군요. ")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        Team[0][3] += Team[0][2]
        Team[3][3] += Team[3][2]
    if Team[0][2] > Team[3][2]:
        print(f"\n3번째 경기 : \n {Team[0][0]} {Team[0][2]} 대 {Team[3][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[0][1] += 3
    elif Team[0][2] < Team[3][2]:
        print(f"\n3번째 경기 : \n {Team[3][0]} {Team[3][2]} 대 {Team[0][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[3][1] += 3
    else:
        print("\n3번째 경기: 동점입니다. 승점 1점씩 추가합니다.\n")
        Team[0][1] += 1
        Team[3][1] += 1

    Team[0][2] = 0
    Team[3][2] = 0

    for i in range(0, 10):
        print(f'\n{i * 10}분 지났습니다.\n')
        a = random.choice(twoSeed)
        b = random.choice(threeSeed)
        if a == "파란공" and b == "빨간공":
            Team[1][2] += 1
            print("UFO 슛! 골~! 관중들의 환호성이 들리십니까?")
        if b == "파란공" and a == "빨간공":
            Team[2][2] += 1
            print("예측불허한 슈팅으로 골망을 찢어버렸습니다. ")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        Team[1][3] += Team[1][2]
        Team[2][3] += Team[2][2]
    if Team[1][2] > Team[2][2]:
        print(f"\n4번째 경기 : \n {Team[1][0]} {Team[1][2]} 대 {Team[2][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[1][1] += 3
    elif Team[1][2] < Team[2][2]:
        print(f"\n4번째 경기 : \n {Team[2][0]} {Team[2][2]} 대 {Team[1][2]}로 이겼습니다. 승점 3점 획득!\n")
        Team[2][1] += 3
    else:
        print("\n4번째 경기 : 동점입니다. 승점 1점씩 추가합니다.\n")
        Team[1][1] += 1
        Team[2][1] += 1

    Team[1][2] = 0
    Team[2][2] = 0

    for i in range(0, 10):
        print(f'\n{i * 10}분 지났습니다.\n')
        a = random.choice(twoSeed)
        b = random.choice(fourSeed)
        if a == "파란공" and b == "빨간공":
            Team[1][2] += 1
            print("그들의 슈팅은 동영상으로 촬영하고 싶을정도로 강력했습니다.")
            if b == "파란공" and a == "빨간공":
                Team[3][2] += 1
                print("코너킥. 올라갑니다. 왼발슈팅!골~~ 그들은 포기를 모르는군요 ")
            if a == "빨간공" and b == "빨간공":
                print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
            if a == "파란공" and b == "파란공":
                print("선수들 이제는 더 분발해야 됩니다.")
            Team[1][3] += Team[1][2]
            Team[3][3] += Team[3][2]
        if Team[1][2] > Team[3][2]:
            print(f"\n5번째 경기 : \n {Team[1][0]} {Team[1][2]} 대 {Team[3][2]}로 이겼습니다. 승점 3점 획득!\n")
            Team[1][1] += 3
        elif Team[1][2] < Team[3][2]:
            print(f"\n5번째 경기 : \n {Team[3][0]} {Team[3][2]} 대 {Team[1][2]}로 이겼습니다. 승점 3점 획득!\n")
            Team[3][1] += 3
        else:
            print("\n5번째 경기 : 동점입니다. 승점 1점씩 추가합니다.\n")
            Team[1][1] += 1
            Team[3][1] += 1

        Team[1][2] = 0
        Team[3][2] = 0

        for i in range(0, 10):
            print(f'\n{i * 10}분 지났습니다.\n')
            a = random.choice(threeSeed)
            b = random.choice(fourSeed)
            if a == "파란공" and b == "빨간공":
                Team[2][2] += 1
                print("킬패스! 오른발이 골망을 흔듭니다. 저 선수는 지치지도 않나보네요")
            if b == "파란공" and a == "빨간공":
                Team[3][2] += 1
                print("슛! 골~~! . 내게 골을 달라. 그가 골대안까지 들어갈 기세로 달려갑니다 ")
            if a == "빨간공" and b == "빨간공":
                print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
            if a == "파란공" and b == "파란공":
                print("선수들 이제는 더 분발해야 됩니다.")
            Team[2][3] += Team[2][2]
            Team[3][3] += Team[3][2]
        if Team[2][2] > Team[3][2]:
            print(f"\n6번째 경기 : \n {Team[2][0]} {Team[2][2]} 대 {Team[3][2]}로 이겼습니다. 승점 3점 획득!\n")
            Team[2][1] += 3
        elif Team[2][2] < Team[3][2]:
            print(f"\n6번째 경기 : \n {Team[3][0]} {Team[3][2]} 대 {Team[2][2]}로 이겼습니다. 승점 3점 획득!\n")
            Team[3][1] += 3
        else:
            print("\n6번째 경기 : 동점입니다. 승점 1점씩 추가합니다.\n")
            Team[2][1] += 1
            Team[3][1] += 1
        print(f"{Team[0][0]} 골 득점 합산:{Team[0][3]}")
        print(f"{Team[1][0]} 골 득점 합산:{Team[1][3]}")
        print(f"{Team[2][0]} 골 득점 합산:{Team[2][3]}")
        print(f"{Team[3][0]} 골 득점 합산:{Team[3][3]}")
        print(
            f"{Team[0][0]} 승점 :{Team[0][1]} , {Team[1][0]} 승점 :{Team[1][1]}, {Team[2][0]} 승점 :{Team[2][1]} , {Team[3][0]} 승점 :{Team[3][1]}")
        if Team[0][1] == Team[1][1]:
            if Team[0][3] > Team[1][3]:
                Team[0][1] += 2
            else:
                Team[1][1] += 2
        if Team[0][1] == Team[2][1]:
            if Team[0][3] > Team[2][3]:
                Team[0][1] += 2
            else:
                Team[2][1] += 2
        if Team[1][1] == Team[2][1]:
            if Team[1][3] > Team[2][3]:
                Team[1][1] += 2
            else:
                Team[2][1] += 2
        if Team[0][1] == Team[1][1] == Team[2][1]:
            if Team[0][3] > Team[1][3] and Team[0][3] > Team[2][3]:
                Team[0][1] += 3
            if Team[1][3] > Team[2][3]:
                Team[1][1] += 2
            else:
                Team[2][1] += 2

        rank = []
        for i in range(len(Team)):
            rank.append(Team[i][1])
        print(rank)
        rank_Max = max(rank)
        rank.remove(rank_Max)

        win = []
        for i in range(4):
            if rank_Max == Team[i][1]:  # 점수가 최댓값인 나라를 찾으면
                win.append(Team.pop(i))  # win 리스트에 1등 나라를 넣고 기존 리스트에서 제거한 후 break로 빠져나옴
                break
        rank_Max = max(rank)
        for i in range(3):
            if rank_Max == Team[i][1]:  # 점수가 그 다음 최댓값인 나라를 찾으면
                win.append(Team.pop(i))  # win 리스트에 2등 나라를 넣고 기존 리스트에서 제거한 후 break로 빠져나옴
                break
        print('\n 카타르 월드컵 16강 진출 확정 두팀 1순위 2순위 발표. 축하합니다 \n')
        print(f'\n{team_fight}조 1등 : {win[0][0]}, 2등 : {win[1][0]}\n')

        return win

A = [["netherlands", 0, 0, 0],  # 승점, 골, 골합산
         ["senegal", 0, 0, 0],
         ["ecuador", 0, 0, 0],
         ["qatar", 0, 0, 0]]
B = [["england", 0, 0, 0],  # 승점, 골, 골합산
         ["wales", 0, 0, 0],
         ["usa", 0, 0, 0],
         ["iran", 0, 0, 0]]
C = [["argentina", 0, 0, 0],  # 승점, 골, 골합산
         ["mexico", 0, 0, 0],
         ["poland", 0, 0, 0],
         ["saudi", 0, 0, 0]]
D = [["france", 0, 0, 0],  # 승점, 골, 골합산
         ["tunisia", 0, 0, 0],
         ["denmark", 0, 0, 0],
         ["australia", 0, 0, 0]]
E = [["spain", 0, 0, 0],  # 승점, 골, 골합산
         ["germany", 0, 0, 0],
         ["japan", 0, 0, 0],
         ["costarica", 0, 0, 0]]
F = [["belgium", 0, 0, 0],  # 승점, 골, 골합산
         ["croatia", 0, 0, 0],
         ["morocco", 0, 0, 0],
         ["canada", 0, 0, 0]]
G = [["brazil", 0, 0, 0],  # 승점, 골, 골합산
         ["serbia", 0, 0, 0],
         ["cameroon", 0, 0, 0],
         ["swiss", 0, 0, 0]]
H = [["portugal", 0, 0, 0],  # 승점, 골, 골합산
         ["uruguay", 0, 0, 0],
         ["ghana", 0, 0, 0],
         ["korea", 0, 0, 0]]
team_fight = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print('카타르 월드컵 32강 예선전을 시작합니다.\n')
print('A조부터 H조까지 경기를 치르게 됩니다.\n')
print('승리할시 승점 3점을 획득, 무승부일시 각각 승점 1점씩을 획득하고, 패배한 경우 승점 변화는 없습니다.\n')
print('최종 승점을 통해 1,2위가 결정납니다.\n')
print('승점이 동일한 경우 골득점으로 순위를 결정 짓습니다.\n')
print('각 국가들에 운명의 여신이 함께 하길 기원합니다.\n')

round_16 = []
round_16.extend(group_fight_32('A', A))
round_16.extend(group_fight_32('B', B))
round_16.extend(group_fight_32('C', C))
round_16.extend(group_fight_32('D', D))
round_16.extend(group_fight_32('E', E))
round_16.extend(group_fight_32('F', F))
round_16.extend(group_fight_32('G', G))
round_16.extend(group_fight_32('H', H))

print(f'\n카타르 월드컵 32강 예선전 결과를 발표하겠습니다.\n')
print(f'발표된 16팀이 16강 진출합니다 축하합니다.\n')
i = 0
for j in range(0, 16, 2):
    print(f'{team_fight[i]}조 1등: {round_16[j][0]}, 2등 : {round_16[j+1][0]}')
    i += 1
# print(round_16)

# print(f'\n16강 1번째 경기\n{team_fight[0]}조 1위 : {round_16[0][0]} vs {team_fight[1]}조 2위 : {round_16[3][0]}')
# print(f'\n16강 2번째 경기\n{team_fight[2]}조 1위 : {round_16[4][0]} vs {team_fight[3]}조 2위 : {round_16[7][0]}')
# print(f'\n16강 3번째 경기\n{team_fight[4]}조 1위 : {round_16[8][0]} vs {team_fight[5]}조 2위 : {round_16[11][0]}')
# print(f'\n16강 4번째 경기\n{team_fight[6]}조 1위 : {round_16[12][0]} vs {team_fight[7]}조 2위 : {round_16[15][0]}')
# print(f'\n16강 5번째 경기\n{team_fight[1]}조 1위 : {round_16[2][0]} vs {team_fight[0]}조 2위 : {round_16[1][0]}')
# print(f'\n16강 6번째 경기\n{team_fight[3]}조 1위 : {round_16[6][0]} vs {team_fight[2]}조 2위 : {round_16[5][0]}')
# print(f'\n16강 7번째 경기\n{team_fight[5]}조 1위 : {round_16[10][0]} vs {team_fight[4]}조 2위 : {round_16[9][0]}')
# print(f'\n16강 8번째 경기\n{team_fight[7]}조 1위 : {round_16[14][0]} vs {team_fight[6]}조 2위 : {round_16[13][0]}')

print("\n카타르 월드컵 16강 대진표를 발표합니다. 경기는 아래 표시된 대진표로 진행됩니다.\n")
print("승부 방식은 토너먼트로 진행됩니다. 무승부일 경우 한 팀이 이길 때까지 진행됩니다.\n")
print("캡틴 박지성 해설 위원, 이번 16강에 큰 이변이 있지 않는 이상 예선전 1시드 2시드 팀이 16강에 올라왔을 거라고 예측이 되는데요\n")
print("네 맞습니다. 크게 이변이 없지 않는 이상 그럴것이라고 생각이 됩니다.\n")
print("그렇다면 예선전 3시드 4시드 국가가 16강에 역전극으로 올라왔다면 그팀의 승률은 어떻게 되는거죠?\n")
print("16강에 올라온 1위 2위 국가의 승률은 1시드 2시드로 측정되어 경기가 진행됩니다\n")
print("그렇군요. 각 국가 별 운명의 여신이 함께하길 기원합니다. \n")
i=1
for j in range(0, 8, 2):
    print(f'\n16강 {i}번째 경기\n{team_fight[j]}조 1위 : {round_16[j*2][0]} vs {team_fight[i*2-1]}조 2위 : {round_16[j*2+3][0]} ')
    i += 1
i=5
for j in range(1, 8, 2):
    print(f'\n16강 {i}번째 경기\n{team_fight[j]}조 1위 : {round_16[j*2][0]} vs {team_fight[j-1]}조 2위 : {round_16[j*2-1][0]} ')
    i += 1
print("\n경기 시작에 앞서 16강에 진출한 국가들의 승점, 골, 골합산 내역들을 초기화한 후 경기를 진행하겠습니다.\n")
print(round_16)
for i in range(0, 16):
    for j in range(1, 4):
        round_16[i][j] = 0   #리스트 점수들(승점, 골, 골합산) 초기화
print(round_16) # 16강에 경기할 국가들 기존 리스트 재활용
group_fight_16(round_16)
