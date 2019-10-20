with open("x.txt", 'r', encoding='utf-8') as filelist:
    test = [x.lower() for x in filelist]

    s = set(test)
    with open('y.txt', 'w') as f:
        for item in s:
            item = item.capitalize()
            f.write("%s" % item)
