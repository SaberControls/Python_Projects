logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet  = []
alphabet1  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0' ,'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'!' ,'£' ,'$' ,'%' ,'^' ,'&' ,'*' ,':' ,'?' ,'#' ,'~' ,'@' ,'|' ,'¬' ,'<' , '>', ' ']
alphabet2  = ['z', '>', '1', '<', '5', 'b', 's', 'g', 'h', 'a', 'r', '%', 't', '@', '£', 'f', '7', 'j', 'd', '!', 'p', '2', '~', 'l', '$', '¬', 'n', 'm', '0', '&', '6', '^', ':', 'i', '8', '#', '9', '4', '|', 'c', 'k', ' ', 'e', 'v', 'q', '*', '?', 'x', 'o', 'u', 'w', 'y', '3']
alphabet3  = ['w', '1', 'a', 'r', 'f', 'm', 'u', '0', '>', 's', 'c', 'j', 'h', '%', '8', '&', 'l', 'k', '^', 'x', '4', '6', '3', '~', 'v', '!', '5', '<', '|', ' ', '9', ':', '*', '@', 'z', 'i', 't', 'o', 'q', '#', 'e', 'p', 'd', '¬', '7', 'y', '$', '£', '?', '2', 'n', 'b', 'g']
alphabet4  = ['2', 'l', 'q', 'n', 'm', '#', 'x', 'a', 'v', '?', 'j', '3', '~', '4', 'u', 'd', 'e', 'f', '<', '>', ' ', 'y', '6', '*', 'w', 'i', '&', 's', '@', '¬', 'p', '1', '£', 'b', '^', '0', 'g', '7', '9', 't', '!', ':', 'z', 'o', '|', 'k', 'h', '%', '5', 'r', '8', '$', 'c']
alphabet5  = ['*', '?', '^', '9', 's', 'a', 'z', 'e', 'v', 'b', 'x', '2', ':', 't', 'l', '|', 'p', 'c', '3', 'j', 'g', '&', 'q', 'k', 'o', 'u', '!', '7', 'i', '¬', '1', '$', 'm', '>', 'n', '@', 'h', 'f', ' ', '5', 'w', '%', '~', '4', 'y', 'd', '<', '#', '£', '6', 'r', '0', '8']
alphabet6  = ['s', 'z', '$', '0', 'j', 'b', '4', '#', 'a', ':', 'y', '?', '2', '9', 'e', 'h', '1', 'g', 'x', '7', 't', '£', '5', 'c', '6', '^', '%', 'n', '&', 'w', 'k', 'f', 'p', ' ', '@', '8', 'o', '*', 'm', 'q', 'l', '~', '¬', '|', '!', 'i', 'u', '>', 'v', '3', '<', 'd', 'r']
alphabet7  = ['7', 'f', '3', '*', 'w', 'k', 'h', '2', '4', 'b', 'l', '@', 'o', 'i', 'p', '9', 'u', 'z', '0', 'a', '|', '1', '%', '~', ' ', '>', '5', 'n', '&', '<', ':', '¬', 'v', 'g', 'c', '£', '!', 'q', 'y', 's', '#', '6', 'e', 't', 'd', '^', 'j', 'r', '$', '?', 'x', '8', 'm']
alphabet8  = ['>', 'q', '$', '£', 'z', '#', '5', 'i', 'b', 'a', '2', '¬', 'm', '%', 'p', '8', 's', '7', '4', 'u', '!', '1', '9', 'e', '&', '3', 'l', 'w', ':', '6', 'r', 'g', '0', '^', 'c', 'n', ' ', 'x', 'k', 'o', 'y', 'j', 't', '<', '~', 'f', '|', 'd', 'v', '@', 'h', '?', '*']
alphabet9  = ['1', '@', '3', 'x', 'y', 'a', '~', '¬', '$', 'c', '|', 'n', '%', '&', '9', '£', 's', '8', 'k', 'd', '6', 'f', 't', '2', 'r', 'v', 'm', '0', 'u', '#', ' ', 'e', '!', ':', 'b', 'q', 'j', '*', 'l', 'z', '5', 'p', '4', 'g', '?', 'o', 'w', '<', 'i', '>', '7', '^', 'h']
alphabet10 = ['&', '4', '£', '#', '7', '1', 'o', 'a', 'p', 'w', '^', '>', 't', 'e', '?', '2', 'n', 'g', ' ', '$', 'i', 'm', 'l', '8', '<', '|', '9', 's', ':', '!', 'b', '0', '@', '%', 'r', '¬', 'z', 'v', 'h', 'd', 'y', 'c', 'q', 'j', 'k', 'f', 'x', '3', '6', '5', '*', 'u', '~']        

print(logo,"\n")

free = True
cont = True
enccomp = True
decomp = True

while cont:

    while free:
        
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        level = int(input("Type encryption level between 1 and 10:\n"))

        if direction == 'encode' and level > 0 and level < 11:
            free = False
        elif direction == 'decode' and level > 0 and level < 11:
            free = False
        else:
            print("Incorrect input, try again") 



    count = 1
    text1 = input("Type your message:\n").lower()
    txt_length = len(text1)

    #shift = int(input("Type the encryption key:\n"))
    #if shift > 52:
       # shift = shift % 53

    if direction == "decode":
        shift = -1
    if direction == "encode":
        shift = 0

    def caeser(text1, shift, direction, level):
        global free
        global cont
        global num
        global count
        global enccomp
        global decomp
        global alphabet
        global alphabet1
        global alphabet2
        global alphabet3
        global alphabet4
        global alphabet5
        global alphabet6
        global alphabet7
        global alphabet8
        global alphabet9
        global alphabet10
        
        cipher_text = ""
        if direction == "decode":

            count = level

            while decomp:

                #count += level
                
                shift = int(input(f"Type the encryption key for level {count}:\n"))
                shift *= -1
                if shift > 52:
                    shift = shift % 53
                


                alphabet = 0
                alphabet = []

                if count > 0:

                    if count == 1:
                        alphabet.extend(alphabet1)
                    elif count == 2:
                        alphabet.extend(alphabet2)
                    elif count == 3:
                        alphabet.extend(alphabet3)
                    elif count == 4:
                        alphabet.extend(alphabet4)
                    elif count == 5:
                        alphabet.extend(alphabet5)
                    elif count == 6:
                        alphabet.extend(alphabet6)
                    elif count == 7:
                        alphabet.extend(alphabet7)
                    elif count == 8:
                        alphabet.extend(alphabet8)
                    elif count == 9:
                        alphabet.extend(alphabet9)
                    elif count == 10:
                        alphabet.extend(alphabet10)

                    for letter in text1:
                        if letter in alphabet:
                            num = alphabet.index(letter) + shift
                            if num > 52:
                                num = num % 53
                            lettr = alphabet[num]
                            cipher_text += lettr
                        else:
                            cipher_text += letter
                    

                    if count > 1:
                        text1 = cipher_text
                        cipher_text = ""
                        count -= 1
                    else:
                        print('\n')                  
                        print(f'Your message at level {count} is:')
                        print(cipher_text)
                        print('\n')
                        decomp = False  
                        #cont1 = input("Do you want to continue? Type Y for Yes and N for No:\n").lower()
                        #if cont1 == 'y':
                        #    free = True
                        #elif cont1 == 'n':
                        #    cont = False
                        #else:
                        #    cont = False
                        cont = False


        
        if direction == "encode":
            while enccomp:

                shift = int(input(f"Type the encryption key for level {count}:\n"))
                if shift > 52:
                    shift = shift % 53

                alphabet = 0
                alphabet = []
                
                if count == 1:
                    alphabet.extend(alphabet1)
                elif count == 2:
                    alphabet.extend(alphabet2)
                elif count == 3:
                    alphabet.extend(alphabet3)
                elif count == 4:
                    alphabet.extend(alphabet4)
                elif count == 5:
                    alphabet.extend(alphabet5)
                elif count == 6:
                    alphabet.extend(alphabet6)
                elif count == 7:
                    alphabet.extend(alphabet7)
                elif count == 8:
                    alphabet.extend(alphabet8)
                elif count == 9:
                    alphabet.extend(alphabet9)
                elif count == 10:
                    alphabet.extend(alphabet10)

                for letter in text1:
                    if letter in alphabet:
                        num = alphabet.index(letter) + shift
                        if num > 52:
                            num = num % 53
                        lettr = alphabet[num]
                        cipher_text += lettr
                    else:
                        cipher_text += letter

                if count != level:                   
                    text1 = cipher_text
                    cipher_text = ""



                if count == level:

                    print('\n')                   
                    print(f'Your message at level {count} is:')
                    print(cipher_text)
                    print('\n')
                    cipher_text = ""
                    enccomp = False                    
                    #cont1 = input("Do you want to continue? Type Y for Yes and N for No:\n").lower()
                    #if cont1 == 'y':
                    #    free = True
                    #elif cont1 == 'n':
                    #    cont = False
                    #else:
                    #    cont = False
                    cont = False
                else:
                    count += 1
            
    

    caeser(text1,shift,direction,level)
