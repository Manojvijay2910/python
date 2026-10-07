s = "Take up one idea and make that idea your life."
sub = "idea"
found = False
pos = -1
while True:
    pos = s.find(sub, pos + 1, len(s))
    if pos == -1:
        break
    print("Found substring at position ", pos)
    found = True

if found == False:
    print("Substring not found")