#=========ENTIRE CODE========================

#DECLARATION INDEPENDENCE
with open("./src/beale_cipher/declaration.txt") as declaration:
    declaration = declaration.read()
#print(declaration)



#DECLARATION INDEPENDENCE ENGROSSED COPY
with open("./src/beale_cipher/declar_engrossed_copy.txt") as delcaration_engrossed:
    delcaration_engrossed = delcaration_engrossed.read()
#print(delcaration_engrossed)

#DECLARATION INDEPENDENCE REPORTED DRAFT
with open("./src/beale_cipher/declar_reported_draft.txt") as delcaration_reported_draft:
    delcaration_reported_draft = delcaration_reported_draft.read()
#print(delcaration_reported_draft)

#DECLARATION INDEPENDENCE FIRST DRAFT
with open("./src/beale_cipher/declar_first_draft.txt") as delcaration_first_draft:
    delcaration_first_draft = delcaration_first_draft.read()
#print(delcaration_reported_draft)



# DECODED CIPHER
with open("./src/beale_cipher/bealecipher2.txt") as decoded_code:
    decoded_code = decoded_code.read()
#print(decoded_code)

# DECODED CIPHER EDITED
with open("./src/beale_cipher/bealecipher2_edited.txt") as decoded_edit:
    decoded_edit = decoded_edit.read()
#print(decoded_code)

book1 = declaration.split()

#print(book)
declar_engross = delcaration_engrossed.split()

declar_reported_d = delcaration_reported_draft.split()

delcar_first_draft = delcaration_reported_draft.split()

# LARGEST NUMBER: 1005

#ENTIRE CODE
code_array = decoded_code.split()
code_array_edit = decoded_edit.split()
plain_text = ""
counter = 0

#for i in code_array:
    #replace_num = i.replace("107", "----73----",5)
    #print(f"\033[1;34m{replace_num}\033[0m")
    #print(replace_num) 


    


#MODERN DECLARATION INDEPENDENCE
# for i in code_array_edit:
for i in code_array: 
    word = book1[int(i) - 1]
    letter = word[0] #<-- first letter of word
    # letter = word < -- prints out entire word at said index
    plain_text += letter
    #print(i, letter)

    #print(i) # <-- prints out each number from cipher2. 115, 73, 24 etc.
print("\nMODERN DECLARATION - DECODE CIPHER ")
print(plain_text)    


# ===============================================#=================================
# 73 = h 
# change 107(t) to = h 

#========Replace num 107(t) with 73(h)===========================
#for i in code_array:
#    replace_num = i.replace("107", "----73----",5)
    #print(f"\033[1;34m{replace_num}\033[0m")
    #print(replace_num) 



# for r in (("C", "v",18),("M", "I", 5),("R", "i", 15)):
#     plain_text = plain_text.replace(*r)
#print(plain_text)


# Split each word into characters hi = "h", "i"

# for i in book1:
#     counter += 1
#     if counter <= 90:
#         print(counter,i)
    #print(counter,i)

    # characters = list(i)
    # print(characters)


#plain_text2 = ""
#=====================ENGROSSED COPY DECLARATION INDEPENDENCE
# for i in code_array:
#     word = declar_engross[int(i) - 1]
#     letter = word[0] #<-- first letter of word
    
#     plain_text2 += letter
# print("\nENGROSSED COPY - DECODE CIPHER ")
# print(plain_text2)


#plain_text3 = ""
#=====================REPORTED DRAFT DECLARATION INDEPENDENCE
# for i in code_array:
#     word = declar_reported_d[int(i) - 1]
#     letter = word[0] #<-- first letter of word

#     plain_text3 += letter
# print("\nREPORTED DRAFT - DECODE CIPHER ")
# print(plain_text3)


#plain_text4 = ""
#====================REPORTED DRAFT DECLARATION INDEPENDENCE
# for i in code_array:
#     word = delcar_first_draft[int(i) - 1]
#     letter = word[0] #<-- first letter of word

#     plain_text4 += letter
# print("\nFIRST DRAFT - DECODE CIPHER ")
# print(plain_text4)


#===================NUMBER OF NUMBERS in decoded message
# for i in code_array:
#     counter += 1
#     print(counter,i)


#=============multiply by 2
# a = 762 #<-- number of words in decoded cipher
# b = 2  
# print(a * b) 








# NUMBER OF TIMES NUMBERS APPEAR

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
#     print(cipher2(f"{decoded_code}"))

