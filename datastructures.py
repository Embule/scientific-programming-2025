##### 1. Lemmas: count lemmas in a text
def tokenize(text):
    return [word.strip(" ,\n.);(!?)'").lower() for word in text.split(' ')]

def count_lemmas(text, lemmas):
    tokenized_text = tokenize(text)
    words_list = []
    lemmas_dic = {}

    # add the lemma form of a word into a list
    for word in tokenized_text:
        if word in lemmas:
            words_list.append(lemmas[word])
        else:
            words_list.append(word)

    # count the number of lemmas in the word list of
    # lemma forms and add to dictionary
    for word in words_list:
        if word in lemmas_dic:
            lemmas_dic[word] +=1
        else:
            lemmas_dic[word] = 1

    return lemmas_dic

text = "He is, was and will be a runner. And runners ran, run and will always run. This is their nature."

lemmas = {
    "runners": "runner",
    "ran": "run",
    "was": "be",
    "is": "be"
}

print(count_lemmas(text, lemmas))

#### 2. Grammatical categories
def count_category(lemma_counts, category):
    counter = 0

    # increase counter whenever a word matches the requested category
    for key,value in lemma_counts.items():
        if key in category:
            counter += value

    return counter

lemma_counts = {'he': 1, 'be': 4, 'and': 3, 'will': 2, 'a': 1, 'runner': 2, 'run': 3, 'always': 1, 'this': 1, 'their': 1, 'nature': 1}
nouns = {'runner', 'nature', 'building'}
verbs = {'walk', 'run', 'be'}
determiners = {'the', 'a', 'this', 'their'}

print(count_category(lemma_counts, nouns))
print(count_category(lemma_counts, verbs))
print(count_category(lemma_counts, determiners))

#### 3. Library
library = {"Life of Pi": "Adventure",
           "One World The Water Dancer": "Fantasy",
           "The Three Musketeers": "Adventure",
           "To Kill a Mockingbird": "Classics",
           "Circe": "Fantasy",
           "The Call of the Wild": "Adventure",
           "Little Women": "Classics"}

def group_titles_by_genre(library):
    genre_dic = {}

    # go through titles and add them to a list (value) based on genre (key)
    for book, genre in library.items():
        if genre in genre_dic:
            genre_dic[genre].append(book)
        else:
            genre_dic[genre] = [book]

    return genre_dic

grouped = group_titles_by_genre(library)
print(grouped)

#### 4. Unify
def unify(dict1, dict2):
    result = {}
    unified_dict = set(dict1) | set(dict2)

    # merge lists of values as sets based on same keys and add them 
    # to the final dictionary form
    for key in unified_dict:
        list1 = dict1.get(key, [])
        list2 = dict2.get(key, [])

        merged = list(set(list1 + list2))
        result[key] = merged
            
    return result

dict1 = {"a": [1, 2, 3], "c": [4, 5, 6], "d": [6]}
dict2 = {"a": [1, 3, 4], "b": [9], "c": [2, 4]}
print(unify(dict1, dict2))

#### 5. Melt
def melt(dict):
    tuple_list = []

    # go through dictionary key-value pairs 
    for key, value in dict.items():
        # go through the lists of values and add them to tuple list 
        # by pairing the original key and the value in the list of values
        for number in value:
            tuple_list.append((key, number))
    return tuple_list

dict1 = {"a": [1, 2, 3], "c": [4, 5, 6], "d": [6]}
print(melt(dict1))

#### 6. N-intersection
def n_intersection(sets):
    if not sets:
        return set()
    
    # go through sets by intersecting them
    # starting from the first set on the list
    intersection = sets[0]
    for item in sets[1:]:
        intersection = intersection & item
    
    return intersection

ex1 = n_intersection([{5, 9, 6}, {9, 2, 6}, {6, 5, 9}])
ex2 = n_intersection([{"kerfuffle", "hullaballoo", "ragamuffin", "flummox"},
                      {"kerfuffle", "ragamuffin", "gobbledygook", "flummox"},
                      {"hullaballoo", "ragamuffin", "gobbledygook", "flummox"},
                      {"hullaballoo", "ragamuffin", "ragamuffin", "gobbledygook", "flummox"}])
ex3 = n_intersection([])

print(ex1)
print(ex2)
print(ex3)

#### 7. Sentiment
def sentiment_of_text(text, sentiment_of_word):
    tokenized_text = tokenize(text)
    sentiment_score = 0

    # go through words and if they match a word from the sentiment list,
    # add the value of the sentiment
    for word in tokenized_text:
        if word in sentiment_of_word:
            sentiment_score += sentiment_of_word[word]
        else:
            sentiment_score += 0

    return sentiment_score

text1 = "Wow, what an amazing day it has been! The weather is fantastic!"
text2 = "Today has been abysmal. The weather is dreadful, and I feel miserably upset."

sentiment_of_word = {
    "abysmal": -5, "agonizing": -4, "dreadful": -5, "grim": -3, "horrible": -5,
    "miserable": -4, "terrible": -5, "upset": -3, "unpleasant": -2, "woeful": -4,
    "horrific": -5, "disastrous": -5, "appalling": -5, "repulsive": -4, "noxious": -3,
    "atrocious": -5, "vile": -4, "wretched": -3, "deplorable": -5, "abominable": -5,
    "amazing": 5, "fantastic": 4, "joyful": 4, "excellent": 5, "delightful": 4,
    "wonderful": 5, "terrific": 4, "great": 3, "awesome": 5, "superb": 4,
    "fabulous": 4, "incredible": 5, "marvelous": 4, "phenomenal": 5, "outstanding": 4,
    "brilliant": 5, "spectacular": 4, "splendid": 3, "glorious": 4, "fantabulous": 5
}
print(sentiment_of_text(text1, sentiment_of_word))
print(sentiment_of_text(text2, sentiment_of_word))