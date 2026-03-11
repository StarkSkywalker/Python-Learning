print('🏆欢迎来到：答题闯关挑战赛（输入q可随时退出）\n')

# 题目与答案
ques1, ans1 = 'Python中用于输出的函数是？', 'print'
ques2, ans2 = 'Python中用于表示逻辑“并且”的关键字是？', 'and'
ques3, ans3 = 'Python属于编译型还是解释型？', '解释型'

# 最多可尝试次数
max_tries = 3
# 总关卡数
total_levels = 3
# 是否处于可游戏状态
is_playing = True

for level in range(1, total_levels + 1):
    print(f'********🎯第{level}关********')
    if level == 1:
        question,answer = ques1,ans1
    if level == 2:
        question, answer = ques2, ans2
    if level == 3:
        question, answer = ques3, ans3

    tries =1
    while tries <= max_tries:
        user_input = input('📢'+question)
        if user_input == answer:
            print('✅回答正确！\n')
            break
        elif user_input == '':
            print('⚠️您的输入为空，请重新作答！\n')
            continue
        elif user_input == 'q':
            print('👋您已退出游戏！\n')
            is_playing = False
            break
        else:# 绝对是错误答案
            leave = max_tries - tries
            if leave > 0:
                print(f'❌回答错误，您还剩{leave}次机会！\n')
                tries +=1
                continue
            else:
                print(f'😢挑战失败，本题的正确答案是：{answer}，游戏结束！')
                is_playing = False
                break
    if not is_playing:
        break

if is_playing:
    print('🎉🎉🎉恭喜您！全部通关！🎉🎉🎉')