import sys
if len(sys.argv) != 2:
    print("Filename not provided.")
    print("Usage: python3 customCounter.py <file>")
else:
    file = open(sys.argv[1], "r")
    file_content = file.read()
    file.close()
    character_dict = {}
    for character in file_content:
        if character not in character_dict:
            character_dict[character] = 0
        character_dict[character] += 1
    for character, count in character_dict.items():
        print(character,count,sep=":")