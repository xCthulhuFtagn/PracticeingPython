with open('input.txt', 'r') as f:
    #f.readlines() - список строк
    for line in f:
        words = line.strip().split()
        for word in words :
            print(word)
