# Practice-python-console-for-2022-world-cup-game-in-Qatar
The 2022 Qatar World Cup was programmed with a Python console.
![image](https://user-images.githubusercontent.com/115389450/233533631-9abf27b2-21f4-4de4-92ff-b8968b8eceb4.png)
![image](https://user-images.githubusercontent.com/115389450/233533663-0ae4cc72-7cb6-429f-96d1-c299e464c466.png)
![image](https://user-images.githubusercontent.com/115389450/233533686-9d7c4a56-553b-4531-95cb-882c8dc9f5d3.png)
```
def a_group_one():
    netherlands = 0
    senegal = 0
    ecuador = 0
    qatar = 0

    nethergoal = 0
    senegalgoal = 0
    ecuadorgoal = 0
    qatargoal = 0

    nethergoalfinal = 0
    senegalgoalfinal = 0
    ecuadorgoalfinal = 0
    qatargoalfinal = 0

    oneSeed = ["파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공"]  # 1시드 이길 확률 70%, 질 확률 30%
    twoSeed = ["파란공", "파란공", "파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공", "빨간공"]
    threeSeed = ["파란공", "파란공", "파란공", "파란공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공"]  # 3시드 이길 확률 40%, 질 확률 60%
    fourSeed = ["파란공", "파란공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공", "빨간공"]
    for i in range(1, 10):
        print(f'{i*10}분 지났습니다.')
        a = random.choice(oneSeed)
        b = random.choice(twoSeed)
        if a == "파란공" and b == "빨간공":
            nethergoal += 1
            print("프렝키 더 용~ 화려한 중거리슛으로 경기를 장식합니다.")
        if b == "파란공" and a == "빨간공":
            senegalgoal += 1
            print("밤바 디엥 헤딩슛! 역시 머리를 짧게 짜른 이유가 있었군요")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        nethergoalfinal += nethergoal
        senegalgoalfinal += senegalgoal
    if nethergoal>senegalgoal:
        print(f"a조 1번째 경기 : \n 네덜란드가 {nethergoal} 대 {senegalgoal}로 이겼습니다. 승점 3점 획득!")
        netherlands += 3
    elif nethergoal<senegalgoal:
        print(f"a조 1번째 경기 : \n 세네갈이 {senegalgoal} 대 {nethergoal}로 이겼습니다. 승점 3점 획득!")
        senegal += 3
    else:
        print("a조 1번째 경기 : 동점입니다. 승점 1점씩 추가합니다.")
        netherlands += 1
        senegal += 1

    nethergoal=0
    senegalgoal=0

    for i in range(1, 10):
        print(f'{i*10}분 지났습니다.')
        a = random.choice(oneSeed)
        b = random.choice(threeSeed)
        if a == "파란공" and b == "빨간공":
            nethergoal += 1
            print("멤피스 데파이의 절묘한 감아차기 슛! 꼴!! 저 선수 포기하지 않는 정신이 결국 골망을 흔들었습니다.")
        if b == "파란공" and a == "빨간공":
            ecuadorgoal += 1
            print("에콰도르의 심장 발렌시아의 오버헤드킥! 그는 마치 온몸을 자유자재로 조종하는 것 같군요. ")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        nethergoalfinal += nethergoal
        ecuadorgoalfinal += ecuadorgoal
    if nethergoal>ecuadorgoal:
        print(f"a조 2번째 경기 : \n 네덜란드가 {nethergoal} 대 {ecuadorgoal}로 이겼습니다. 승점 3점 획득!")
        netherlands += 3
    elif nethergoal < ecuadorgoal:
        print(f"a조 2번째 경기 : \n 에콰도르가 {ecuadorgoal} 대 {nethergoal}로 이겼습니다. 승점 3점 획득!")
        ecuador += 3
    else:
        print("a조 2번째 경기: 동점입니다. 승점 1점씩 추가합니다.")
        netherlands += 1
        ecuador += 1

    nethergoal=0
    ecuadorgoal=0

    for i in range(1, 10):
        print(f'{i * 10}분 지났습니다.')
        a = random.choice(oneSeed)
        b = random.choice(fourSeed)
        if a == "파란공" and b == "빨간공":
            nethergoal += 1
            print("테일러의 무섭도록 예리한 패스로 노아 랭이 마무리 짓네요. 그들은 마치 형제같군요")
        if b == "파란공" and a == "빨간공":
            qatargoal += 1
            print("강철 심장 하산 알 하이도스! 그의 슛은 너무 빨라 보이지도 않군요. ")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        nethergoalfinal += nethergoal
        qatargoalfinal += qatargoal
    if nethergoal>qatargoal:
        print(f"a조 3번째 경기 : \n 네덜란드가 {nethergoal} 대 {qatargoal}로 이겼습니다. 승점 3점 획득!")
        netherlands += 3
    elif nethergoal<qatargoal:
        print(f"a조 3번째 경기 : \n 카타르가 {qatargoal} 대 {nethergoal}로 이겼습니다. 승점 3점 획득!")
        qatar += 3
    else:
        print("a조 3번째 경기: 동점입니다. 승점 1점씩 추가합니다.")
        netherlands += 1
        qatar += 1

    nethergoal=0
    qatargoal=0

    for i in range(1, 10):
        print(f'{i * 10}분 지났습니다.')
        a = random.choice(twoSeed)
        b = random.choice(threeSeed)
        if a == "파란공" and b == "빨간공":
            senegalgoal += 1
            print("마마두 로움의 UFO 슛! 나도 골 널거야 아마두?")
        if b == "파란공" and a == "빨간공":
            ecuadorgoal += 1
            print("로마리오 이바라의 예측불허한 슈팅으로 골망을 찢어버렸습니다. ")
        if a == "빨간공" and b == "빨간공":
            print("선수들 조금 더 분발해야 겠는데요. 많이 지친걸까요")
        if a == "파란공" and b == "파란공":
            print("선수들 이제는 더 분발해야 됩니다.")
        senegalgoalfinal += senegalgoal
        ecuadorgoalfinal += ecuadorgoal
    if senegalgoal>ecuadorgoal:
        print(f"a조 4번째 경기 : \n 세네갈이 {senegalgoal} 대 {ecuadorgoal}로 이겼습니다. 승점 3점 획득!")
        senegal += 3
    elif senegalgoal<ecuadorgoal:
        print(f"a조 4번째 경기 : \n 에콰도르가 {ecuadorgoal} 대 {senegalgoal}로 이겼습니다. 승점 3점 획득!")
        ecuador += 3
    else:
        print("a조 4번째 경기 : 동점입니다. 승점 1점씩 추가합니다.")
        senegal += 1
        ecuador += 1

    senegalgoal=0
    ecuadorgoal=0

    for i in range(1, 10):
        print(f'{i * 10}분 지났습니다.')
        a = random.choice(twoSeed)
        b = random.choice(fourSeed)
```
![image](https://user-images.githubusercontent.com/115389450/233533787-c91bed8f-e034-41a5-a128-4c5741ff1836.png)
```
# print("a조 경기 시작!!")
# gong = ["파란공", "빨간공"]
# bluegong = 0
# redgong = 0
# a = random.randint(1, 10)
# if 1 <= a <= 7:
#     print(gong[0])
# else:
#     print(gong[1])

# def gong():
#     percent = random.randint(1,10)
#     if percent <= 7:
#         gong = print("파란공")
#     else:
#         gong = print("빨간공")
#     # return gong
#
# gong()
# while True:
# #     a = random.choice(gong)
# #
# #     if a == "파란공":
# #         bluegong += 1
# #     else:
# #         redgong += 1
# #
# #     if bluegong >= 7:
# #         print("네덜란드가 이김")
# #         break
# #     elif redgong >= 3:
# #         print("네덜란드가 짐")
# #         breaks
# #     continue
#     if netherlands == senegal:
    #         print("네덜란드와 세네갈 승점이 동일합니다. 재경기합니다.")
    #         continue
    #     if netherlands == ecuador:
    #         print("네덜란드와 에콰도르 승점이 동일합니다. 재경기합니다.")
    #         continue
    #     if netherlands == senegal == ecuador:
    #         print("네덜란드와 세네갈, 에콰도르 승점이 동일합니다. 재경기합니다.")
    #         continue
    # if netherlands == senegal :
    #     if nethergoalfinal > senegalgoalfinal:
    #         print("네덜란드와 세네갈의 승점이 같아 골득점으로 비교합니다. 네덜란드가 세네갈보다 골을 많이 넣었으므로 A조 1위를 차지합니다.")
    #         groupA1st = "netherlands"
    #         print("a조 1위 = ", groupA1st)
    # if netherlands == senegal:
    #     if nethergoalfinal>senegalgoalfinal:
    #         netherlands += nethergoalfinal
    #     else:
    #         senegal += senegalgoalfinal
    #     if ecuador == qatar:
    #         if ecuadorgoalfinal>qatargoalfinal:
    #             ecuador += ecuadorgoalfinal
    #         else:
    #             qatar += qatargoalfinal
    #     if senegal == ecuador:
    #         if senegalgoalfinal>ecuadorgoalfinal:
    #             senegal += senegalgoalfinal
    #         else:
    #             ecuador += ecuadorgoalfinal
    #     if netherlands == ecuador:
    #         if nethergoalfinal>ecuadorgoalfinal:
    #             netherlands += nethergoalfinal
    #         else:
    #             ecuador += qatargoalfinal
    #     if netherlands == qatar:
    #         if nethergoalfinal>qatargoalfinal:
    #             netherlands += nethergoalfinal
    #         else:
    #             qatar += qatargoalfinal
    # print(f"네덜란드 승점 :{netherlands} , 세네갈 승점 :{senegal}, 에콰도르 승점 :{ecuador} , 카타르 승점 :{qatar}")
     # if netherlands == senegal:
    #     if nethergoalfinal > senegalgoalfinal:
    #         groupA.append("netherlands")
    #     else:
    #         groupA.append("senegal")
    # if netherlands == senegal == ecuador:
    #     if nethergoalfinal > senegalgoalfinal and nethergoalfinal > ecuadorgoalfinal:
    #         groupA.append("netherlands")
    #     if senegalgoalfinal > ecuadorgoalfinal:
    #         groupA.append("senegal")
      # if a == "파란공" and b == "빨간공" :
                #     netherlands += 3
                #     print("네덜란드 승리! 승점 3점을 획득 합니다.")
                #     break
                # if a == "빨간공" and b == "파란공" :
                #     senegal += 3
                #     print("세네갈 승리 ! 승점 3점을 획득 합니다.")
                #     break
                # if a == "파란공" and b == "파란공" :
                #     netherlands += 1
                #     senegal += 1
                #     print("무승부입니다. 승점 1점씩 획득 합니다.")
                #     break
                # if a == "빨간공" and b == "빨간공" :
                #     netherlands += 1
                #     senegal += 1
                #     print("무승부입니다. 승점 1점씩 획득 합니다.")
                #     break
    #     if i == 2:
    #         while True:
    #             print("네덜란드(1시드) vs 에콰도르(3시드)")
    #             a = random.choice(oneSeed)
    #             b = random.choice(threeSeed)
    #             if a == "파란공" and b == "빨간공" :
    #                 netherlands += 3
    #                 print("네덜란드 승리! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "파란공" :
    #                 ecuador += 3
    #                 print("에콰도르 승리 ! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "파란공" and b == "파란공" :
    #                 netherlands += 1
    #                 ecuador += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "빨간공" :
    #                 netherlands += 1
    #                 ecuador += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #     if i == 3:
    #         while True:
    #             print("네덜란드(1시드) vs 카타르(4시드)")
    #             a = random.choice(oneSeed)
    #             b = random.choice(fourSeed)
    #             if a == "파란공" and b == "빨간공" :
    #                 netherlands += 3
    #                 print("네덜란드 승리! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "파란공" :
    #                 qatar += 3
    #                 print("카타르 승리 ! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "파란공" and b == "파란공" :
    #                 netherlands += 1
    #                 qatar += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "빨간공" :
    #                 netherlands += 1
    #                 qatar += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #     if i == 4:
    #         while True:
    #             print("세네갈(2시드) vs 에콰도르(3시드)")
    #             a = random.choice(twoSeed)
    #             b = random.choice(threeSeed)
    #             if a == "파란공" and b == "빨간공" :
    #                 senegal += 3
    #                 print("세네갈 승리! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "파란공" :
    #                 ecuador += 3
    #                 print("카타르 승리 ! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "파란공" and b == "파란공" :
    #                 senegal += 1
    #                 ecuador += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "빨간공" :
    #                 senegal += 1
    #                 ecuador += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #     if i == 5:
    #         while True:
    #             print("세네갈(2시드) vs 카타르(4시드)")
    #             a = random.choice(twoSeed)
    #             b = random.choice(fourSeed)
    #             if a == "파란공" and b == "빨간공" :
    #                 senegal += 3
    #                 print("세네갈 승리! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "파란공" :
    #                 qatar += 3
    #                 print("카타르 승리 ! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "파란공" and b == "파란공" :
    #                 senegal += 1
    #                 qatar += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "빨간공" :
    #                 senegal += 1
    #                 qatar += 1
    #                 print("무승부입니다. 승점 1점씩 획득 합니다.")
    #                 break
    #     if i == 6:
    #         while True:
    #             print("에콰도르(3시드) vs 카타르(4시드)")
    #             a = random.choice(threeSeed)
    #             b = random.choice(fourSeed)
    #             if a == "파란공" and b == "빨간공" :
    #                 ecuador += 3
    #                 print("에콰도르 승리! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "빨간공" and b == "파란공" :
    #                 qatar += 3
    #                 print("카타르 승리 ! 승점 3점을 획득 합니다.")
    #                 break
    #             if a == "파란공" and b ==
    #     percent = random.randint(1,10)
#     if percent <= 7:
#         gong = print("파란공")
#     else:
#         gong = print("빨간공")
#     # return gong
#
# gong()

# print(random.choice(oneSeed))
# print(random.choice(twoSeed))
# print(random.choice(threeSeed))
# print(random.choice(fourSeed))
```
![image](https://user-images.githubusercontent.com/115389450/233534372-40ad5d58-5b2a-4e23-9bd2-d12ba1e8e28e.png)

```
import random

def group_fight(team_fight, Team):

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
```
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
    print(f"{Team[0][0]} 승점 :{Team[0][1]} , {Team[1][0]} 승점 :{Team[1][1]}, {Team[2][0]} 승점 :{Team[2][1]} , {Team[3][0]} 승점 :{Team[3][1]}")
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
        if Team[0][3] > Team[1][3] and Team[0][3]>Team[2][3]:
            Team[0][1] += 3
        if Team[1][3] > Team[2][3]:
            Team[1][1] += 2
        else:
            Team[2][1] +=2

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
```

A = [["netherlands", 0, 0, 0], # 승점, 골, 골합산
    ["senegal", 0, 0, 0],
    ["ecuador", 0, 0, 0],
    ["qatar", 0, 0, 0]]
B = [["england", 0, 0, 0], # 승점, 골, 골합산
    ["wales", 0, 0, 0],
    ["usa", 0, 0, 0],
    ["iran", 0, 0, 0]]
C = [["argentina", 0, 0, 0], # 승점, 골, 골합산
    ["mexico", 0, 0, 0],
    ["poland", 0, 0, 0],
    ["saudi", 0, 0, 0]]
D = [["france", 0, 0, 0], # 승점, 골, 골합산
    ["tunisia", 0, 0, 0],
    ["denmark", 0, 0, 0],
    ["australia", 0, 0, 0]]
E = [["spain", 0, 0, 0], # 승점, 골, 골합산
    ["germany", 0, 0, 0],
    ["japan", 0, 0, 0],
    ["costarica", 0, 0, 0]]
F = [["belgium", 0, 0, 0], # 승점, 골, 골합산
    ["croatia", 0, 0, 0],
    ["morocco", 0, 0, 0],
    ["canada", 0, 0, 0]]
G = [["brazil", 0, 0, 0], # 승점, 골, 골합산
    ["serbia", 0, 0, 0],
    ["cameroon", 0, 0, 0],
    ["swiss", 0, 0, 0]]
H = [["portugal", 0, 0, 0], # 승점, 골, 골합산
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
round_16.extend(group_fight('A', A))
round_16.extend(group_fight('B', B))
round_16.extend(group_fight('C', C))
round_16.extend(group_fight('D', D))
round_16.extend(group_fight('E', E))
round_16.extend(group_fight('F', F))
round_16.extend(group_fight('G', G))
round_16.extend(group_fight('H', H))

print(f'\n카타르 월드컵 32강 예선전 결과를 발표하겠습니다.\n')
print(f'발표된 16팀이 16강 진출합니다 축하합니다.\n')
i = 0
for j in range(0, 16, 2):
    print(f'{team_fight[i]}조 1등: {round_16[j][0]}, 2등 : {round_16[j+1][0]}')
    i += 1
```
![image](https://user-images.githubusercontent.com/115389450/233533993-bd9f88aa-568f-4c67-98c5-0a6312b8675c.png)
![image](https://user-images.githubusercontent.com/115389450/233534027-246cb8ad-ce8c-471e-a468-6fcc73d46a9a.png)
![image](https://user-images.githubusercontent.com/115389450/233534058-832726d3-baeb-4c77-8603-ffffbab6941d.png)
![image](https://user-images.githubusercontent.com/115389450/233534085-ae0f1b24-417b-484b-ac6b-11782703745f.png)

![image](https://user-images.githubusercontent.com/115389450/233534448-59ece4c5-f62b-4b6f-a6eb-0c4732325601.png)
![image](https://user-images.githubusercontent.com/115389450/233534484-e57dc59e-431d-4541-a517-dbbe315d26a1.png)
```
# print(f'\n16강 1번째 경기\n{team_fight[0]}조 1위 : {round_16[0][0]} vs {team_fight[1]}조 2위 : {round_16[3][0]}')
# print(f'\n16강 2번째 경기\n{team_fight[2]}조 1위 : {round_16[4][0]} vs {team_fight[3]}조 2위 : {round_16[7][0]}')
# print(f'\n16강 3번째 경기\n{team_fight[4]}조 1위 : {round_16[8][0]} vs {team_fight[5]}조 2위 : {round_16[11][0]}')
# print(f'\n16강 4번째 경기\n{team_fight[6]}조 1위 : {round_16[12][0]} vs {team_fight[7]}조 2위 : {round_16[15][0]}')
# print(f'\n16강 5번째 경기\n{team_fight[1]}조 1위 : {round_16[2][0]} vs {team_fight[0]}조 2위 : {round_16[1][0]}')
# print(f'\n16강 6번째 경기\n{team_fight[3]}조 1위 : {round_16[6][0]} vs {team_fight[2]}조 2위 : {round_16[5][0]}')
# print(f'\n16강 7번째 경기\n{team_fight[5]}조 1위 : {round_16[10][0]} vs {team_fight[4]}조 2위 : {round_16[9][0]}')
# print(f'\n16강 8번째 경기\n{team_fight[7]}조 1위 : {round_16[14][0]} vs {team_fight[6]}조 2위 : {round_16[13][0]}')
```
![image](https://user-images.githubusercontent.com/115389450/233534532-a7d65d75-d16c-4d24-854b-ac38656e9e72.png)\
```
i=1
for j in range(0, 8, 2):
    print(f'\n16강 {i}번째 경기\n{team_fight[j]}조 1위 : {round_16[j*2][0]} vs {team_fight[i*2-1]}조 2위 : {round_16[j*2+3][0]} ')
    i += 1
i=5
for j in range(1, 8, 2):
    print(f'\n16강 {i}번째 경기\n{team_fight[j]}조 1위 : {round_16[j*2][0]} vs {team_fight[j-1]}조 2위 : {round_16[j*2-1][0]} ')
    i += 1
```
![image](https://user-images.githubusercontent.com/115389450/233534602-090a7e2a-fd15-4c9a-9792-82ab545f75f1.png)
```
print("\n경기 시작에 앞서 16강에 진출한 국가들의 승점, 골, 골합산 내역들을 초기화한 후 경기를 진행하겠습니다.\n")
print(round_16)
for i in range(0, 16):
    for j in range(1, 4):
        round_16[i][j] = 0   #리스트 점수들(승점, 골, 골합산) 초기화
print(round_16) # 16강에 경기할 국가들 기존 리스트 재활용
```
![image](https://user-images.githubusercontent.com/115389450/233534666-823a08c8-e969-454d-898d-0d1f5a2b931a.png)
```
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
            win_8.append(round_16[j*2][0])
        elif round_16[j*2][2] < round_16[j*2+3][2]:
            print(f"\n{i}번째 경기 : \n {round_16[j*2+3][0]} {round_16[j*2+3][2]} 대 {round_16[j*2][2]}로 이겼습니다. 8강 진출합니다.\n")
            win_8.append(round_16[j*2+3][0])
        else:
            print("동점입니다. 재경기 진행합니다.")
            while True:
                a = random.choice(oneSeed)
                b = random.choice(twoSeed)
                if a == "파란공" and b == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*2][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2][0])
                    break
                elif b == "파란공" and a == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*2+3][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2 + 3][0])
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
            win_8.append(round_16[j*2][0])
        elif round_16[j*2][2] < round_16[j*2-1][2]:
            print(f"\n{i}번째 경기 : \n {round_16[j*2-1][0]} {round_16[j*2-1][2]} 대 {round_16[j*2][2]}로 이겼습니다. 8강 진출합니다.\n")
            win_8.append(round_16[j*2-1][0])
        else:
            print("동점입니다. 재경기 진행합니다.")
            while True:
                a = random.choice(oneSeed)
                b = random.choice(twoSeed)
                if a == "파란공" and b == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*2][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2][0])
                    break
                elif b == "파란공" and a == "빨간공":
                    print(f"\n{i}번째 경기 : \n {round_16[j*-1][0]} 8강 진출합니다. ")
                    win_8.append(round_16[j * 2 -1][0])
                    break
        i += 1
    print("\n카타르 월드컵 16강 경기 선수들 부상 없이 무사히 종료되었습니다.\n")
    print("8강 진출 국가는 아래와 같습니다. \n")
    for i in range(0, 8):
        print(win_8[i])
```
![image](https://user-images.githubusercontent.com/115389450/233534712-52834662-2a52-4521-b10d-3d498b192652.png)
![image](https://user-images.githubusercontent.com/115389450/233534739-18f2a164-6841-4f46-8571-4f70e76bd729.png)
![image](https://user-images.githubusercontent.com/115389450/233534754-e7d2562b-ac0d-4fd8-a4bc-5aeee3367f59.png)
```
    print("\n카타르 월드컵 8강을 시작 하겠습니다.\n")
    print("\n대진표는 아래와 같습니다.\n")
    print(f'1번째 경기 : {win_8[0]} vs {win_8[1]}')
    print(f'2번째 경기 : {win_8[4]} vs {win_8[5]}')
    print(f'3번째 경기 : {win_8[2]} vs {win_8[3]}')
    print(f'4번째 경기 : {win_8[6]} vs {win_8[7]}')
```
![image](https://user-images.githubusercontent.com/115389450/233534811-9fc4a18c-0aff-4f44-bc37-37b63a2529e8.png)
```
    i=1
    for j in range(0, 13, 4):
        if i>=3:
            print(f'{i}번째 경기 : {win_8[j-6]} vs {win_8[(j+1)-6]}')
        else:
            print(f'{i}번째 경기 : {win_8[j]} vs {win_8[j+1]}')
        i += 1
``` 
![image](https://user-images.githubusercontent.com/115389450/233534856-9f0a1388-6320-4e77-84c4-9563e09d4e63.png)
```
    i=1
    for j in range(0, 3, 2):
        print(f'준결승전 {i}번째 경기 : {win_4[j][0]} vs {win_4[j+1][0]}')
        i += 1
```
```
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
```
```
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
            print(f"\n{i}번째 경기 : \n {win_4[j][0]}가 {win_4[j][2
```
```
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
```
![image](https://user-images.githubusercontent.com/115389450/233535070-97976ed5-a6ed-4f0f-90d2-d90274a78293.png)
![image](https://user-images.githubusercontent.com/115389450/233535095-5ef3d8a8-f2ef-4b8f-b997-fabb3b0497f5.png)


          









