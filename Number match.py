def determine_winner(n, arr):
    team_a_support = 0
    team_b_support = 0

    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    for num, count in frequency.items():
        if num % 2 == 0:
            if count % 2 == 0:
                team_a_support += 1 
            else:
                team_b_support += 1 
        else: 
            if count % 2 == 0:
                team_b_support += 1  
            else:
                team_a_support += 1  

   
    if team_a_support > team_b_support:
        print(f"A {team_a_support}")  
    elif team_b_support > team_a_support:
        print(f"B {team_b_support}")  
    else:
        print("T 0") 

n = int(input().strip()) 
arr = list(map(int, input().strip().split()))  

determine_winner(n, arr)
