import sys

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    p = 31
    m_pow = p**(m-1)

    bool = pattern.isalpha()
    if bool == False:
        return -2
    bool = text.isalpha()
    if bool == False:
        return -2

    pattern_hash = sum(ord(pattern[i]) * p**(m-1-i) for i in range(m))
    rolling_hash = sum(ord(text[i]) * p**(m-1-i) for i in range(m))
    nrArr = []
    for i in range(n - m + 1):
        if rolling_hash == pattern_hash and text[i:i+m] == pattern:
            nrArr.append(i)
        if i < n - m:
            rolling_hash -= ord(text[i]) * m_pow
            rolling_hash = rolling_hash * p + ord(text[i+m])

    textLen = len(text)
    patternLen = len(pattern)

    if patternLen<1:
        return -2

    if textLen<patternLen:
        return -2

    if 500000<textLen:
        return -2

    indexLen = len(pattern)
    totalLen = textLen*indexLen

    if 100000000<totalLen:
        return -2

    if not nrArr:
        return -1
    return nrArr

def main():

    print("Enter 'I' to input from keyboard, or 'F' to input from file")
    choice = input().strip()

    input1 = ""
    input2 = ""
    if choice == "I":
        print("Enter pattern:")
        input1 = input().strip()

        print("Enter text:")
        input2 = input().strip()

    elif choice == "F":
        print("Enter file name: ")
        try:
            fileName = input().strip()
            with open(fileName, 'r') as f:
                input1 = f.readline().strip()
                input2 = f.readline().strip()
                ##print("Firstline is : " + input1)
                ##print("Secondline is : " + input2)
        except:
            print("error, file not found")
            sys.exit(0)
    else:
        print("wrong input")

    pattern = input1
    text = input2

    index = rabin_karp(text, pattern)

    

    if index == -1:
        print("Pattern not found in the text")
    if index == -2:
        print("error with text or pattern")
    else:
        print(f"Pattern found at index {index}")

if __name__ == "__main__":
    main()