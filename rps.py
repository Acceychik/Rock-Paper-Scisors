    import random

    def logic(a, b):
    	if a == "scissors" and b == "rock":
    		print(f"You losed!\n You: {a}\n Me: {b}")
    	elif a == "scissors" and b == "paper":
    		print(f"You won!\n You: {a}\n Me: {b}")
    	elif a == "rock" and b == "scissors":
    		print(f"You won!\n You: {a}\n Me: {b}")
    	elif a == "rock" and b == "paper":
    		print(f"You losed!\n You: {a}\n Me: {b}")
    	elif a == "paper" and b == "rock":
    		print(f"You won!\n You: {a}\n Me: {b}")
    	elif a == "paper" and b == "scissors":
    		print(f"You losed!\n You: {a}\n Me: {b}")

    print("Rock, Paper, Scissors!\nVersion: [1.0]\n\n")

    answer = str(input("What is your answer?: "))

    while answer:
    	quest = random.choice(["rock", "paper", "scissors"])
    	if quest == answer:
    		continue
    	logic(answer, quest)
    	break
