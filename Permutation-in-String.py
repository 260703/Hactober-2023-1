# this is leet code roblem solution (567) Permutation in String

from collections import Counter

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    # Create a Counter for s1 to count character frequencies
    s1_counter = Counter(s1)

    # Initialize a sliding window for s2 of the same length as s1
    window_counter = Counter(s2[:len(s1)])

    for i in range(len(s1), len(s2)):
        if window_counter == s1_counter:
            return True
        
        # Update the sliding window by removing the character leaving the window
        left_char = s2[i - len(s1)]
        if window_counter[left_char] == 1:
            del window_counter[left_char]
        else:
            window_counter[left_char] -= 1
        
        # Add the new character entering the window
        right_char = s2[i]
        if right_char in window_counter:
            window_counter[right_char] += 1
        else:
            window_counter[right_char] = 1
    
    return window_counter == s1_counter

# Example usage:
s1 = "abc"
s2 = "eidbaooo"
result = checkInclusion(s1, s2)
print(result)  # This should print True
