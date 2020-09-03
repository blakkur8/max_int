# algorithm sem finnur fyrstu n tölunar í sequence
# sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# 3 tölur á undan samanlagðar
# ef það eru færri en 3 tölur, bæta við einni
# byrja á 1, á meðan ég hef ekki farið uppí n tölu þá heldur forritið áfram að gefa mér tölur
#previus 2 numbers + sequence

n = int(input("Enter the length of the sequence: "))

n1,n2,n3 = 1,2,3
count = 0

while n > count:
    count = count + 1
    jafna = n1 + n2 + n3
    print(jafna)
    n1 = n2
    n2 = n3
    n3 = jafna 

