story = f"""Once upon a time, there was a [adjective] programmer named [name].
[Name] loved to code in [programming language]. One day, [name] decided to write a program
that would generate [adjective] Mad Libs stories. The program prompted the user for
various words, such as a [noun], a [verb], and an [adjective]. After the user entered
all the words, the program would create a hilarious story.

[Name] was so excited about their program that they [verb] all night long,
testing it out with different words. The results were [adjective]! Everyone who
tried the program had a good laugh.

From that day on, [name] continued to code and create more fun and [adjective]
programs."""

# User input loop
words = {}  # Dictionary to store user-provided words
for word_type in ["adjective", "name", "programming language", "noun", "verb", "adjective"]:
    words[word_type] = input(f"Enter a(n) {word_type} word: ")

# Combine user input and template
formatted_story = story.format(**words)

# Print the final story
print("\nYour Mad Libs Story:")
print(formatted_story)