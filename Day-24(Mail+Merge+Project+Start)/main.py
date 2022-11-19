
with open("./Input/Letters/starting_letter.txt") as st:
    starting_letter = st.read()

with open("./Input/Names/invited_names.txt") as nm:
    names = nm.readlines()
    for i in range(len(names)):
        names[i] = names[i].replace("\n", "")
        with open(f"./Output/ReadyToSend/{names[i]}.txt", "w") as op:
            text = starting_letter.replace("[name]", f"{names[i]}")
            op.write(text)

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp