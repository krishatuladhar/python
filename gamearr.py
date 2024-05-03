import numpy as np
import random

file1_arrays = [np.random.randint(1, 10, size=(3, 2)) for _ in range(20)]
file2_arrays = [np.random.randint(1, 10, size=(2, 3)) for _ in range(20)]

def play_game():
    player_name = input("Enter your name: ")
    player_score = 0

    for round in range(5):
        array1 = random.choice(file1_arrays)
        array2 = random.choice(file2_arrays)

        print(f"\nRound {round + 1}:")
        print("Array 1:\n", array1)
        print("Array 2:\n", array2)
        guess = int(input("What is the dot product of these two arrays? "))

        dot_product = np.dot(array1.flatten(), array2.flatten())

     
        if guess == dot_product:
            print("Correct!")
            player_score += 1
        else:
            print("Incorrect!")
    
    print(f"\n{player_name}'s final score: {player_score}\n")

    return {'name': player_name, 'score': player_score}


player_info = play_game()
print(player_info)
