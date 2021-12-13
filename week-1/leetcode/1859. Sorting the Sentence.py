def sortSentence(s):
    s = s.split(" ")
    for i in range(len(s)):
        for j in range(len(s) - 1):
            if int(s[j][len(s[j]) - 1]) > int(s[j + 1][len(s[j + 1]) - 1]):
                s[j], s[j + 1] = s[j + 1], s[j]
    sorted = ""
    for word in s:
        sorted += word.replace(word[len(word) - 1], " ")
    print(sorted[:len(sorted) - 1])


sortSentence("is2 sentence4 This1 a3")