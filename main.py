with open(file="../Mail Merge Project Start/Input/Names/invited_names.txt") as invNames:
    all_names = invNames.readlines()

with open(file="../Mail Merge Project Start/Input/Letters/starting_letter.txt") as startLetter:
    l_start = startLetter.read()
    for names in all_names:
        stripped_names = names.strip()
        new_letter = l_start.replace("[name]", stripped_names)
        print(new_letter)
        with open(file=f"../Mail Merge Project Start/Output/letter_for{stripped_names}.txt", mode="w") as completed:
            completed.write(new_letter)