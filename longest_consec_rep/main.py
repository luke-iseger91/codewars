# https://www.codewars.com/kata/586d6cefbcc21eed7a001155

# For a given string s find the character c (or C) with longest consecutive repetition and return:
# (c,l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.
# For empty string return:
# ('', 0)

def longest_repetition(chars):

    if len(chars) == 0:
        return ('', 0)

    longest_c= ""
    longest_c_count = 0
    char_counter = 1

    for x in range(len(chars)):      
        try:
            # print(x, f"testing {chars[x]} and {chars[x+1]}")
            if chars[x] == chars[x+1]:
                char_counter += 1
            else:
                char_counter = 1 
        except IndexError:
            continue
        if char_counter > longest_c_count:
            longest_c = chars[x]
            longest_c_count = char_counter

    return (longest_c, longest_c_count)


# Test cases
# print(find_longest_c("aaa"))
assert longest_repetition("aaa") == ("a", 3)
# print(longest_repetition("vogelbekdier"))
assert longest_repetition("vogelbekdier") == ("v", 1)
assert longest_repetition("") == ("", 0)
# print(longest_repetition("aaabbaaaa"))
assert longest_repetition("aaabbaaaa") == ("a", 4)    