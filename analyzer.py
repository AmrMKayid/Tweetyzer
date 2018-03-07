import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # TODO
        self.positive = set()
        positivesFile = open(positives, "r")
        for line in positivesFile:
            if not line.startswith(";"):
                self.positive.add(line.strip(" ").rstrip("\n"))
        positivesFile.close()
        
        self.negative = set()
        negativesFile = open(negatives, "r")
        for line in negativesFile:
            if not line.startswith(";"):
                self.negative.add(line.rstrip("\n").strip(" "))
        negativesFile.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        sentiment = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for word in tokens:
            #print(word)
            if word.lower() in self.positive:
                sentiment += 1
            elif word.lower() in self.negative:
                sentiment += (-1)
        #print(sentiment)
        return sentiment
