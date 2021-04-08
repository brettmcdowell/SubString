def subset(word1, word2):
    word3 = ''
    length1 = len(word1)
    for i in range(0,length1):
        if word1[i] in word2:
            string = word1[i]
            word3 += word1[i]
            word2 = word2.replace(string,'',1)

    if word3 == word1:
        print("\nFirst word is a subset of second word")
        print(word3)
    else:
        print("\nFirst word is not a subset of second word")


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
subset(word1,word2)
