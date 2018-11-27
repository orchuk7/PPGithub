with open('virsh.txt', 'w') as file:
    Sadok = ["A cherry orchard by the house.\n",
            "Above the cherries beetles hum.\n",
            "The plowmen plow the fertile ground\n",
            "And girls sing songs as they pass by.\n",
            "It’s evening — mother calls them home.\n",
            "A family sups by the house.\n",
            "A star shines in the evening chill.\n",
            "A daughter serves the evening meal.\n",
            "Time to give lessons — mother tries,\n",
            "But can’t. She blames the nightingale.\n",
            "It’s getting dark, and by the house,\n",
            "A mother lays her young to sleep;\n",
            "Beside them she too fell asleep.\n",
            "All now went still, and just the girls\n",
            "And nightingale their vigil keep.\n"]

    for i in range(0, len(Sadok)):
        file.write(str(Sadok[i]))

with open('virsh.txt', 'r')as file:
    read_file = file.readlines()

for i in range(0, len(read_file)):
    print(read_file[i].strip())


file = open('b1.txt', 'w')
for i in range(0, len(read_file), 2):
    file.write(str(read_file[i]).upper())
file.close()
file = open('b2.txt', 'w')
for i in range(1, len(read_file), 2):
    file.write(str(read_file[i]).lower())
file.close()
