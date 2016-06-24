def factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    else:
        return (n * factorial(n - 1))


def rank_calculate(words="rohit"):
        l = len(words)
        i = 0
        pos = 1
        current = 0
        letter = []
        for i in range(0, l):
            letter.append(int(ord(words[i])))
        letter.sort()

        while(current<l):
            i=0
            while(letter[i]!=int(ord(words[current]))):
                if letter[i]!=0:
                    pos += factorial(l - 1 - current)

                    i+=1
                else:
                    i+=1


            letter[i]=0
            current+=1

        return pos

