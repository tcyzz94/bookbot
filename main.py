# Print hello world
print("--- Begin report of books/frankenstein.txt ---")

# Open the file and read its contents
try:
    with open("./books/frankenstein.txt", "r") as f:
        w = f.read().split()
    print(len(w))
    
    result = {}
    for word in w:
        newWord = word.lower()
        chars = list(newWord)
        for char in chars:
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
    
   #  print(result)
    sorted_by_values_desc = sorted(result.items(), key=lambda item: item[1], reverse=True)
   #  print("Sorted by values (descending):", sorted_by_values_desc)
    for char, count in sorted_by_values_desc:
      print(f"The '{char}' character was found {count} times")
except FileNotFoundError:
    print("The file frankenstein.txt was not found.")

print("--- End report ---")
