#This is not the weasel problem.
#This is the hill climbing problem
#Each new improvement is saved.
#Here we change all non correct position and check whether the new_str is an improvement.
#Another implementation is try each character change and check whether it produce an improvement. If not redo.
import random

def generate_str(strlength, alph):
    result = ''
    for i in range(strlength):
        result += random.choice(alph)
    return result

def similarity_score(goal_str, gen_str):
    score = 0
    correct_index = []
    for i in range(len(goal_str)):
        if goal_str[i] == gen_str[i]:
            correct_index.append(i)
            score += 1
    return score/len(goal_str), correct_index
             

def main():
    counter = 0
    alph = 'abcdefghijklmnopqrstuvwxyz '
    goal_str = 'methinks it is like a weasel'
    new_str = generate_str(28, alph)
    score , match_index = similarity_score(goal_str, new_str)
    med_str = [x for x in new_str]
    ccounter = 0
    while score < 1:
        for i in range(len(new_str)):
            if i not in match_index:
                med_str[i] = random.choice(alph) 
                new_str = ''.join(med_str)
            ccounter += 1
        score,match_index = similarity_score(goal_str,new_str)
        print(counter, new_str)
        counter += 1

main()
