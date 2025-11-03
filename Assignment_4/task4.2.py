def count_vowels(text):
    """
    Count the number of vowels in a given string.
    
    Args:
        text (str): The input string to check for vowels
        
    Returns:
        int: Number of vowels found in the string
    """
    # Define vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Count vowels using sum with generator expression
    return sum(1 for char in text if char in vowels)

# Taking input from keyboard in a loop
if __name__ == "__main__":
    while True:
        print("\nEnter a word to count its vowels")
        print("(Press Enter without text to exit)")
        
        # Get input string
        word = input("Enter word: ").strip().lower()
        
        # Check for exit condition
        if not word:
            print("Thank you for using the vowel counter!")
            break
        
        # Count and display results
        num_vowels = count_vowels(word)
        if num_vowels == 1:
            print(f"'{word}' has {num_vowels} vowel")
        else:
            print(f"'{word}' has {num_vowels} vowels")
