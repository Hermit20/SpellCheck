def main():
    # displays data in the words,mywords and mistakes file
    words = open('words.txt','r')
    wordslist = []
    print('--- words.txt---')
    for i in words:
        word = i.strip()
        print(word)
        # appends data in words.file to a list
        wordslist.append(word)
    print('-----------------')
    mywords = open('mywords.txt','r')
    mywordslist = []
    print('---mywords.txt---')
    for i in mywords:
        myword = i.strip()
        print(myword)
        # appends data in mywords.file to a list
        mywordslist.append(myword)
    print('-----------------')
    mywords.close()
    mistakeslist = []
    mistakes = open('mistakes.txt','r')
    print('---mistakes.txt---')
    for i in mistakes:
        mistake = i.split(',')
        print(i.strip())

        for k in range(1,len(mistake),2):
            sub = [mistake[0],mistake[k].strip(' '),mistake[k+1].strip()]
            # appends data in mistakes file to a list 
            mistakeslist.append(sub)
    print('-----------------')
    mistakes.close()
    #orders the suggestion
    def suggest(word):
        suggestionint = []
        suggestionstr = []
        for i in mistakeslist:
            if word in i:
                g = i[2]
                # checks for duplicates
                if int(g) in suggestionint:
                    continue
                else:
                    suggestionint.append(int(i[2]))
        suggestionint.sort()
        suggestionint.reverse()
        for i in suggestionint:
            for j in mistakeslist:
                if str(i) in j and word in j:
                    suggestionstr.append(j[1])
        return suggestionstr  
    # saves to a file 
    def save(text):
        try:
            fileli = command.split(' ')
            filenam = fileli[1]
            fileope = open(filenam,'w')
            for i in savelist:
                if i == savelist[0]:
                    pass
                else:
                    fileope.write('\n')
                for j in i:
                    fileope.write(j+' ')
            fileope.close()
        except:
            print('There is nothing to save')
    # loads user input file
    def load(text):
        filelist = command.split(' ')
        filename = filelist[1]
        fileopen = open(filename,'r')
        return fileopen
    savelist = []
    mistakeslist2 = []
    for i in mistakeslist:
        mistakeslist2.append(i)
    mistakeslist3 = []
    for i in mistakeslist2:
        for j in i:
            mistakeslist3.append(j)
    # writes mistakes into mistakes file
    def writemistakes(list = mistakeslist2):
        mist = open('mistakes.txt','w')
        allreadyseen = []
        for i in mistakeslist2:
            if i[0] in allreadyseen:
                continue
            else:
                allreadyseen.append(i[0])
            suggestionlist = []
            for j in mistakeslist2:
                if i[0] == j[0]:
                    c = [j[1],j[2]]
                    suggestionlist.append(c)
            mist.write(i[0])
            for k in suggestionlist:
                mist.write(', '+k[0]+', '+k[1])
            mist.write('\n')
        mist.close()
    # replaces the mistake with the proper word 
    def save2(word):
        for y in range(len(spelllist)): 
            if k == spelllist[y]:
                spelllist.insert(y,word)
                spelllist.pop(y+1)
                savelist.append(spelllist)
                break
        return savelist
    while True:
        command = input('Enter command( or quit to escape ): ')
        if command == 'quit':
            break
        if 'load' in command:
            try:
                fileopen = load(command)
                continue
            except:
                print('there is nothing to load')
        #checks for a spelling error
        if command == 'spell':
            #creates a list form the data user input
            for i in fileopen:
                spelllist = i.split()
                a = spelllist[len(spelllist)-1].strip('.')
                spelllist.insert(len(spelllist)-1,a)
                spelllist.pop(len(spelllist)-1) 
                for k in spelllist:
                    #checks if word is in the "safe" lists
                    if k in wordslist or k in mywordslist:
                        pass
                    else:
                        # if mistakelist is empty
                        if len(mistakeslist) == 0:
                            if len(mistakeslist2) == 0:
                                print('potential mistake: ',k,'suggestions','[No suggestions]')
                                Act = input('Action: ' )
                                savelist= save2(Act)
                                new = [k,Act,str(1)]
                                mistakeslist2.append(new)
                                continue
                        #if mistakes list isn't empty 
                        for j in mistakeslist2:
                            found = False
                            # checks for the mistake in the mistake list 
                            for a in mistakeslist2:
                                if a[0] == k:
                                    found = True
                            if found:
                                # Flags mistake
                                sug = suggest(k)
                                if len(sug) == 0:
                                    sug = '[No suggestions]'
                                print('potential mistake: ',k,'suggestions',sug)
                                Act = input('Action: ' )
                                savelist= save2(Act)
                                # updates mistake file
                                for t in range(len(mistakeslist2)):
                                    # increases the number of times suggestion has been used by 1 if mistake is in mistake file
                                    if Act in mistakeslist2[t]:
                                        n = int(mistakeslist2[t][2])
                                        n += 1
                                        mistakeslist2[t][2] = str(n)
                                        break
                                    else:
                                        # inputs new mistake if mistake isn't in mistakefile 
                                        new = [k,Act,str(1)]
                                        if new in mistakeslist2 or k in mistakeslist3:
                                            continue
                                        else:
                                            mistakeslist2.append(new)
                                            break
                                break
                            # if mistake isn't in mistake file but mistake list has values 
                            else:
                                print('potential mistake: ',k,'suggestions',['No suggestions'])
                                Act = input('Action: ' )
                                # if there is no value entered appends to mywords file
                                if Act == ' ' or Act == '':
                                    mywordslist.append(k)
                                    break
                                # if there is a value entered appends it to the mistake list so it can be written later
                                else:
                                    new = [k,Act,str(0)]
                                    mistakeslist2.append(new)
        # Writes in the new text and writes in the updated mistakes
        if 'save' in command:
            try: 
                mywor = open('mywords.txt','w')
                for i in mywordslist:
                    mywor.write(i)
                mywor.close()
                fileliST = command.split(' ')
                filenamE = fileliST[1]
                save(command)
                writemistakes()
            except:
                print('there is nothing to save')
        
    # diplays new text file, mywords file and mistakes file
    newtxt = open(filenamE,'r')
    print('---newtext.txt---')
    for i in newtxt:
        print(i.strip())
    print('-----------------')
    mywords = open('mywords.txt','r')
    print('---mywords.txt---')
    for i in mywords:
        myword = i.strip()
        print(myword)
    print('-----------------')
    mistakes = open('mistakes.txt','r')
    print('---mistakes.txt---')
    for i in mistakes:
        print(i.strip())
    print('-----------------')


    words.close()
    mywords.close()
    mistakes.close()
    fileopen.close()
    newtxt.close()

if __name__ == '__main__':
    main()
