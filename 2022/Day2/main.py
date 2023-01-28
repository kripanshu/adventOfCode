"""
Rock Paper Scissor
Opponent: A-> Rock , B -> Paper, C-> Scissor
Myslef: X-> Rock , Y -> Paper, Z-> Scissor
Win: X>C, Z>B, Y>A
points
Win = 6, Draw = 3, Loose=0
X = 1, Y=2, Z=3

part two
X= loose
Y = draw
Z = win
"""
selection_points = {"X": 1, "Y": 2, "Z": 3}

win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B":"Y", "C": "Z"}
loose = {"A":"Z", "B":"X", "C":"Y"}

def calculate_current_points(op, me):
    res = 0
    me = evaluate_selection(op, me) #remove/comment this line for part 1
    # draw
    if((op == "C" and me == "Z") or (op == "B" and me == "Y") or (op == "A" and me == "X")):
        res = 3
    # win
    elif((op == "C" and me == "X") or (op == "B" and me == "Z") or (op == "A" and me == "Y")):
        res = 6
    # loose : no points
    return res + selection_points[me]

def evaluate_selection(op, me):
    if(me == "X"):
        return loose[op]
    if(me == "Y"):
        return draw[op]
    
    return win[op]
    
def main():
    puzzle_data = open('input.txt').readlines()

    total = 0
    for line in puzzle_data:
        op, me = line.split()
        print(op, me)
        total+= calculate_current_points(op, me)
    
    print(total)

main()