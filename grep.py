def grep():
    file = raw_input("choose a file: ")
    word = raw_input("what do you want to search: ")
    
    try:
        # opeining file. to be countinued... 
        doc = open(file,"r")
    except Exception, e:
        print "file doesn't exist! :(" 
        grep()
    counter = 0 
    for a_line in doc:
        counter += 1 
        if word.lower() in a_line.lower() :
            print "the word: " + word + " found in line " + str(counter)
grep()