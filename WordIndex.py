#WordIndex.py
#Name:Erick Andres
#Date:3/1/2026
#Assignment:Lab 6
#Purpose:Build an index mapping each word to list of line numbers where it appears.

def main():
    filename = input("Enter a file name:")

    try:
        with open(filename, 'r') as textFile:
            words = {} 
            lineNum = 0

            for line in textFile:
                lineNum += 1
                wordList = line.split()
                for w in wordList:
                    w= w.lower()
                    w = w.replace(",", "")
                    w = w.replace(".", "")
                    w = w.replace("!", "")
                    w = w.replace("?", "")
                    w = w.replace(";", "")
                    w = w.replace(":", "")

                    if w not in words:
                        words[w] = []
                    if not words[w] or words[w][-1] != lineNum:
                        words[w].append(lineNum)
    
            for word in sorted(words):
                print(word, words[word])

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
  

if __name__ == '__main__':
  main()
