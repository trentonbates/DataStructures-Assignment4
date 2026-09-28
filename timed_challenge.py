# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 19. Alternate Merge
# Alternate values from two sequences into one.
# Input: [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

def alternate_merge(seq1, seq2):
    if not isinstance(seq1, list) or not isinstance(seq2, list):
        raise TypeError("Sequences must be lists.")
    if len(seq1) == 0 or len(seq2) == 0:
        raise ValueError("Sequences cannot be empty.")
    if len(seq1) != len(seq2):
        raise ValueError("Sequences are not equal lengths.")

    output = []

    for i in range(len(seq1)):
        output.append(seq1[i])
        output.append(seq2[i])

    return output

# print(alternate_merge([1, 3, 5], [2, 4, 6])) -> [1, 2, 3, 4, 5, 6]
# print(alternate_merge([1, 3, 5], "a")) -> TypeError
# print(alternate_merge([], [2, 4, 6])) -> ValueError
# print(alternate_merge([1, 3, 5], [2, 4])) -> ValueError

# For this problem, the inputs in the example were given as lists so I decided
# to just stick with lists. If I had more time to work on this problem, I would
# try to make the program work with an iterable object instead of just lists.
# The time limit did not affect my decision on how I solved the problem because
# since I decided to just focus on lists I didn't worry about other kinds of input.
# I would consider that to also be the biggest trade-off I made as it would make
# the program a lot better and more usuable if it would work for any iterable
# object that is handed to it.