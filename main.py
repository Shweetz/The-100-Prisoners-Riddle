# Video link to the puzzle: https://www.youtube.com/watch?v=iSNsgj1OCLA

import random

nb_simulations = 10000
nb_prisoners = 100

def generate(goal="all", log=False):
    max_loop_length = 0
    
    # list of boxes: boxes[index] = paper
    boxes = [e for e in range(nb_prisoners)]
    random.shuffle(boxes)
    if log:
        print(f"boxes: {boxes}")
    
    unopened = [e for e in range(nb_prisoners)]
    while unopened:
        start_loop = unopened[0]
        loop_length = 1
        str_loop = str(start_loop)
        e = start_loop
        unopened.remove(e)
        while boxes[e] != start_loop:
            loop_length += 1
            str_loop += "->" + str(boxes[e])
            e = boxes[e]
            unopened.remove(e)
        max_loop_length = max(loop_length, max_loop_length)
        if log:
            print(f"len={loop_length}: {str_loop}")
        if goal == "first":
            return loop_length
    
    return max_loop_length

print("Example of boxes randomized and the loops created")
generate(goal="all", log=True)

print("Simulations where all prisoners must live")
all_prisoners_live = 0
for _ in range(nb_simulations):
    max_loop_length = generate(goal="all")
    if max_loop_length <= nb_prisoners/2:
        all_prisoners_live += 1
        
print(f"{(all_prisoners_live / nb_simulations * 100):.3f}%")

print("Simulations where the 1st prisoner must live")
one_prisoner_live = 0
for _ in range(nb_simulations):
    max_loop_length = generate(goal="first")
    if max_loop_length <= nb_prisoners/2:
        one_prisoner_live += 1
        
print(f"{(one_prisoner_live / nb_simulations * 100):.3f}%")
