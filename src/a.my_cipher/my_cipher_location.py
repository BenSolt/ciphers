with open("./src/a.my_cipher/text_bible_verse.txt") as text2:
    text2 = text2.read()
book1 = text2.split()

with open("./src/a.my_cipher/codelocation.txt") as codelocation:
    codelocation = codelocation.read()
print("\n" "LOCATION")
print(codelocation)


#CODE VERSE
code_array = codelocation.split()
plain_text1 = ""
counter = 0
for i in code_array:
    word = book1[int(i) - 1]  # <-- starts at index READABLE
    #word = book1[int(i) - 4]  # <-- starts at index
    letter = word[0]
    plain_text1 += letter
  
print(plain_text1)


# for i in book1:
#     counter += 1
#     print(counter, i)




#ADD 3 to Decode
# with open("./src/a.my_cipher/codelocation_add3.txt") as codelocation_add3:
#     codelocation_add3 = codelocation_add3.read()
# print("\n" "LOCATION")
# print(codelocation_add3)

# # Code with negative 3
# code_array2 = codelocation_add3.split()
# plain_text2 = ""
# for i in code_array2:
#     word = book1[int(i) - 1]  # <-- starts at index READABLE
#     #word = book1[int(i) - 4]  # <-- starts at index
#     letter = word[0]
#     plain_text2 += letter
  
# print(plain_text2)



#the-treasore-is-boried-aboot-2-miles-northwest-of-newlife-dresher-chorch
#-it-is-located-in-mondaoc-manor-parc-northeast-of-the-dam-inside-the-treeline
#-below-the-rocc--foorte-oeight-thirtetwo-dot-nine-north-seventefive-eleven-
#ofoordot-nine-west
 

# TEXT CODE DECIPHER REFERENCE MESSAGE 2=================================================
# the treasure is buried about 2 miles northwest of newlife dresher church
# it is located in mondauk manor park northeast of the dam inside the treeline
# below a tree shaped liked a V.



 






