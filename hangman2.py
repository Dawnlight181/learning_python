import random

def hangman():
    words = {"cat": "animal", "dragon": "imaginary animal", "soup": "food", "computer": "useful tool", "febrary": "month"}
    answer = random.choice(list(words.items()))
    word = answer[0]
    wrong = 0
    stages = ["",
               "_________     ",
               "|             ",
               "|       |     ",
               "|       0     ",
               "|      /|\    ",
               "|      / \    ",
               "|             "
               ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね:"
        if wrong > 3:
            msg = "１文字を予想してね,ヒント,{}:".format(answer[1])
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}。".format(word))

hangman()
