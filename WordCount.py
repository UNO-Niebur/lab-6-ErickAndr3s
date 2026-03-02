#WordCount.py
#Name:Erick Andres
#Date: 3/1/2026
#Assignment:Lab 6
#Purpose:Implement a wc that reports

def main():
  filename = input("Enter a file name: ")

  try:
      with open(filename, 'r') as textFile:
        lineCount = 0
        wordCount = 0 
        charCount = 0

        for line in textFile:
          #count lines
          lineCount += 1

          #count words
          words = line.split()
          wordCount += len(words)

          #count characters
          charCount += len(line)

      #print results
      print(f"lines: {lineCount}")
      print(f"words: {wordCount}")
      print(f"characters: {charCount}")
  
  #file not found
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

if __name__ == '__main__':
  main()
