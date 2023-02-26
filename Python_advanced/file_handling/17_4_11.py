with open('class_scores.txt', encoding='utf-8') as class_scores, open(
        'new_scores.txt', 'w', encoding='utf-8') as new_scores:
    for line in class_scores:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=new_scores)

# There is a text file class_scores.txt with scores for the final test on the
# lines of the form: last name score (last name and score are separated by a space).
# Rating is an integer from 0 to 100 inclusive.

# The program adds 5 points to each test result and outputs
# the last names and new test results to a file.
