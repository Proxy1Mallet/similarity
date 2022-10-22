def similarityFunction(a: str, b: str) -> int:
    SequenceMatcher = __import__('difflib').SecuenceMatcher #Import the SequenceMatcher function from the difflib library
    similarity = (SequenceMatcher(None, a, b).ratio()) #Get string similarity
    roundedSimilarity = int(similarity * 100) #Rounding off similarity
    return roundedSimilarity

punctuation = __import__('string').punctuation #import the punctuation function from the string library

#Here we write the word with which the comparison will be carried out
lower_case_a = ''.join('Your text for comparison'.lower().split())
a = lower_case_a.translate(str.maketrans('', '', punctuation))

#Loop to repeat comparison, if not needed delete
while True:

    #It's better not to change anything here.
    lower_case_b = ''.join(input('ENTER >>> ').lower().split())
    b = lower_case_b.translate(str.maketrans('', '', punctuation))

    print(similarityFunction(a = a, b = b))
