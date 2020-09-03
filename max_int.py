# tekur input og ber það saman við öll previous input
# á meðan input er 0 eða meira þá heldur forritið áfram
# 

num_int = int(input("Input a number: ")) 
max_int = 0

while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_int) 