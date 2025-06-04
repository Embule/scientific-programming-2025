"""
unique-words-classifier.py: The program takes an arbitrary file from the folder
`test-set` and predicts whether it is written by Shakespeare.

Author: ...
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

SHAKESPEARE_WORDS_FILE = "shakespeare-words.txt"
TEST_SET_PATH = Path("test-set")

def main():
    # Get shakespeare words
    shakespeare_words = load_shakespeare_words(SHAKESPEARE_WORDS_FILE)

    # Get files from the dataset
    text_file_names = get_text_file_names(TEST_SET_PATH)

    # create thresholds using values between 0 and 0.1 in 40 steps
    thresholds = np.linspace(0, 0.1, 40)

    # get accuracies for all the thresholds
    accuracies = compute_all_accuracies(
        thresholds,
        text_file_names,
        shakespeare_words
    )

    # plot the thresholds on th x-axis and accuracies on the y-axis
    plt.plot(thresholds, accuracies, 'co-', markersize = 5)
    plt.legend(['Classifier performance']) 
    plt.title("Classifier performance")
    plt.xlabel("Score Threshold")
    plt.ylabel("Accuracy")
    plt.grid()
    plt.show()


# Change this function in favor of efficiency
def load_shakespeare_words(filename):
    """
    Load the file containing words typicaly for Shakespearean language. Assumes
    that the input file does not contain any duplicate words.
    """
    words = set()
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            words.add(line.rstrip('\n'))
    return words

def get_text_file_names(path, extension='txt'):
    """
    Get all paths of files with given (.txt) extension.
    """
    text_file_names = list(Path(path).glob(f'*.{extension}'))
    return text_file_names

def compute_all_accuracies(thresholds, text_file_names, shakespeare_words):
    # Check if the files are written by shakespeare
    is_shakespeare = is_written_by_shakespeare(text_file_names)

    # Predict step 1, get scores
    scores = []
    for file_name in text_file_names:
        with open(file_name, 'r', encoding='UTF-8') as file:
            score = calculate_shakespeare_score(file.read(), shakespeare_words)
        scores.append(score)

    # Predict step 2, try multiple thresholds and calculate accuracy for each
    accuracies = []
    for threshold in thresholds:
        predicted = [score >= threshold for score in scores]
        accuracy = calculate_accuracy(is_shakespeare, predicted)
        accuracies.append(accuracy)

    return accuracies

# calculate individual accuracy by dividing the number of 
# correctly predicted scores by the number of total predictions
def calculate_accuracy(actual, predicted):
    correct_predictions = 0
    n_predictions = len(predicted)
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct_predictions += 1
    
    return correct_predictions / n_predictions

    
# Change this function in favor of efficiency.
# With N being the length of shakespeare_words:
# Complexity before changes: O(N^2)
# Complexity after changes: O(N)
def calculate_shakespeare_score(text, shakespeare_words):
    """
    Compute the score of a text fragment by checking the relative overlap of
    words in the text with the shakespeare word list.
    """
    word_list = tokenize_text(text)

    # get all unique words in text
    unique_words = set(word_list)

    # get all unique shakespeare words in text
    shakespeare_words_in_text = set(unique_words) & shakespeare_words

    shakespeare_score = len(shakespeare_words_in_text)/len(unique_words)
    return shakespeare_score

def is_written_by_shakespeare(file_names):
    """
    Checks for a given filename in a list of file names
    if they contain the text "shakespeare"
    """
    by_shakespeare = []
    for name in file_names:
        if name.name.split('.')[0] == "shakespeare":
            by_shakespeare.append(True)
        else:
            by_shakespeare.append(False)

    return by_shakespeare

def tokenize_text(text):
    """
    Returns a list of words from string text.
    """
    words = []
    for word in text.split():
        clean = word.lower().strip(' ,;.:\'"[]()-_?!')
        if clean.isalpha():
            words.append(clean)
    return words

if __name__ == "__main__":
    main()
