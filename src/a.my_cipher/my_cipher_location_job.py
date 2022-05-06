# JOB 40================================================================

with open("./src/a.my_cipher/text_bible_verse_job40.txt") as text1:
    text1 = text1.read()
book1 = text1.split()
#book_string1 = str(text1)

with open("./src/a.my_cipher/codelocation_1.txt") as codelocation1:
    codelocation1 = codelocation1.read()

#print(codelocation)


#JOB 41=============================================================

with open("./src/a.my_cipher/text_bible_verse_job41.txt") as text2:
    text2 = text2.read()
book2 = text2.split()
#book_string2 = str(text1)

# Code j2==================================================================
with open("./src/a.my_cipher/codelocation_2.txt") as codelocation2:
    codelocation2 = codelocation2.read()

# print("\n" + codelocation2)

#Code j2B================================================================
with open("./src/a.my_cipher/codelocation_2B.txt") as codelocation2B:
    codelocation2B = codelocation2B.read()  
    print("\n" + codelocation2B)

#Book1 = J40==========================================================================================

code_array1 = codelocation1.split()
plain_text1 = ""
counter = 0
for i in code_array1:
    word = book1[int(i) - 1]  # <-- starts at index READABLE
    #word = book_string1[int(i) - 1] #<-- file to 'string'
    letter = word[0]
    plain_text1 += letter
    
#print("\n" "LOCATION JOB 40")
#print(plain_text1)


# Code 2 =========================================================

code_array2 = codelocation2.split()
plain_text2 = ""
counter = 0
for i in code_array2:
    word = book2[int(i) - 1]  # <-- starts at index READABLE
    #word = book_string1[int(i) - 1] #<-- file to 'string'
    letter = word[0]
    #plain_text2 += letter
    plain_text2 += letter.replace(" ", "")

# print("\n" "LOCATION DECODED")
# print(plain_text2)



# Code 2B========================================================
code_array2B = codelocation2B.split()
plain_text2B = ""
counter = 0
for i in code_array2B:
    word = book2[int(i) + 2]  # <-- starts at index READABLE + 3
    #word = book_string1[int(i) - 1] #<-- file to 'string'
    letter = word[0]
    plain_text2B += letter
   

print("\n" "LOCATION DECODED B")
print(plain_text2B)



# get each letter of book_string===================

# for i in book_string:
#     counter += 1
#     print(counter, i)

# 10 115 243 - 261 129 280 53 43 101 16 157
# the treasure 
# 149 147 - 77 181 159 35 494 11 - 7 77 73 364 44 - 17
# is buried about 2 
# 40 35 66 157 64 - 133 125 129 59 90 30 494 466 465
# miles northwest 
# 78 65 - 189 491 14 5 12 39 382 - 99 363 491 386 505
# of newlife dresher 
# 68 182 438 432 22 124 149 505 - 508 118 - 501 511 215 31 44 491 484 - 322 303
# church it is located in 
# 366 73 189 99 15 101 510 - 40 443 25 294 284 - 300 475 129 36
# mondauk manor park
# 57 129 73 70 - 10 182 157 - r159 148 173 36
# from the rock 
# 261 115 353 10 - 43 31 58 147 - 129 62 79 27 - 227 101 133
# that says, Rapp Run 
# 
#----NOT USING------- flood retarding structure 2013.
# 41 504 66 510 - 153 154 129 85 32 87 157 118 130
# walk Northwest 
# 117 73 129 - 73 72 9 51 133 391 - 26 381 382 - 70 80 5 494 118
# for o point one miles
# 85 101 432 133 - 326 338 200 32 85
# turn right.
# 331 81 - 61 133 93 140 - 10 32 280 - 513 16 157 491 118
# go into the trees
# 66 73 22 15 377 157 - 387 407 494 - 118 90 82 27 491 99- 66 196 36 494 - 7 - 5
# locate one shaped like a Y.
# 37 69 - 10 32 243 59 129 494 491 57 100 133 502 82 129 503 1 510 - 14 135 446 90 -344 133 - x
# by the tree find a rock with a 7 on it
# 11 61 331
# dig


# below tree - Latitude = 40.1425 Longitude = -75.1844