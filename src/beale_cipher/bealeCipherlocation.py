from collections import Counter

#LOCATION LOCATION

#Declaation Independence
with open("./src/beale_cipher/declaration.txt") as declaration:    
    declaration = declaration.read()
    
    book1 = declaration.split()

    book_string = str(declaration)

#Declaation Independence SPANISH
with open("./src/beale_cipher/declaration_spanish.txt") as declaration_spanish:    
    declaration_spanish = declaration_spanish.read()
    
    book_spanish = declaration_spanish.split()


# Declaration multiply by 2
with open("./src/beale_cipher/declar_times3.txt") as declaration:    
    declaration = declaration.read()
    
    book2 = declaration.split()


with open("./src/beale_cipher/bealecipherlocation.txt") as codelocation:    
    codelocation = codelocation.read()
    #print(codelocation)




# BIGGEST NUMBER: 2906

code_array = codelocation.split()
plain_text1 = ""
counter = 0
num1 = "1701"
num2 = "1629"


# for i in code_array:
#     counter += 1
#     if counter <= 3:
#         print(counter,i)
#     # word = book1[int(i) - 1]
# # print(word)
# print(book1)



# COUNT BY LETTER INSTEAD OF BY WORD===========================================
for i in code_array:
    word = book_string[int(i) - 1]
    #word = book1[int(i) - 1]
    letter = word[0]
    plain_text1 += letter

    #print(i, letter)
    # if i == "  ":
    #     i.replace("  ","")

    #for r in (("C", "v",18),("M", "I", 5),("R", "i", 15)):
        #plain_text = plain_text.replace(*r)
    #print(plain_text)
    
print("\nLOCATION BY LETTER COUNT")
print(plain_text1)

# TEST REMOVE SPACES=========================================================================
plain_text4 = ""
for i in code_array:
    word = book_string[int(i) - 1]
    letter = word[0]
    # for i in ((" ", ""),(",", "")):
    #     plain_text4 = letter.replace(i)

    plain_text4 += letter.replace(" ", "")

    #print(i, letter)

print("\nREMOVE SPACE TEST\n",(plain_text4)) 


# TEST LETTER COUNT===================================================================

  
with open("./src/beale_cipher/locationcipher_lettercount.txt") as codelocation_letters:    
    codelocation_letters = codelocation_letters.read()

# for i in codelocation_letters:
#     print(i)



# DECLAR SPANISH===============================================
# code_array = codelocation.split()
# plain_text3 = ""
# counter = 0

# for i in code_array:

#     word = book_spanish[int(i) - 1]
#     letter = word[0]
#     plain_text3 += letter
#     counter += 1
#     # if counter:
#     #     if counter == 5:
#     #         print (" ")
#     #     print(counter,letter)
# print("\nLOCATION")
# print(plain_text3)


# DECLAR TIMES 3 =============================================
# code_array = codelocation.split()
# plain_text1 = ""
# counter = 0

# for i in code_array:

#     word = book2[int(i) - 1]
#     #word = book1[int(i) - 1]
#     letter = word[0]
#     plain_text1 += letter
#     counter += 1
#     # if counter:
#     #     if counter == 5:
#     #         print (" ")
#     #     print(counter,letter)
# print("\nLOCATION")
#print(plain_text1)


# JAMES J. GILLOGLY - THE BEALE CIPHER: A DISSENTING OPINION =======================================

#ABFDE FGHII JKLMM NOHPP

#===============================================================================


#NUMBER OF WORDS
# for i in book_string:
# #for i in book1:
#     print(i)
#     counter += 1
#     if counter < 75:
#         print(counter, i)



# def cipher2(s):
#     if len(s) < 1:
#         return {}
#     else:
#         word_counter = {}

#     s = " ".join(s.split()).lower().split(" ")
    
#     for word in s:
        
#         word = word.strip(',[,]')
           
#         if word_counter.get(f"{word}"):
#             word_counter[word] += 1
           
#         else: 
#             word_counter[word] = 1
        
#     words = list(word_counter.items())

#     words.sort(key=(lambda e: (-e[-1], e[0])))
#     for word, a in words:
#         word = word + " " * (35-len(word)) + "#" * a
#         print(word)

# if __name__ == "__main__":
#     print(cipher2(""))
#     print(cipher2(f"{codelocation}"))




