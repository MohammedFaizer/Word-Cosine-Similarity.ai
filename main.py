import PyPDF2
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load the PDF document
pdf_file = open('f.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# extract the text from the document
document_text = ''
for page in pdf_reader.pages:
    document_text += page.extract_text()

# tokenize the document text
document_tokens = word_tokenize(document_text)
document_sentences = sent_tokenize(document_text)

# remove stop words
stop_words = set(stopwords.words('english'))
document_tokens = [token for token in document_tokens if token.lower() not in stop_words]

# create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
document_tfidf = vectorizer.fit_transform(document_sentences)

# define a function to get the most relevant sentence
def get_most_relevant_sentence(question):
    # tokenize the question
    question_tokens = word_tokenize(question.lower())
    question_tokens = [token for token in question_tokens if token not in stop_words]
    # create a TF-IDF vector for the question
    question_tfidf = vectorizer.transform([question])
    # calculate the cosine similarity between the question and each sentence in the document
    similarities = cosine_similarity(question_tfidf, document_tfidf)[0]
    # get the index of the most similar sentence
    most_similar_index = similarities.argmax()
    # return the most relevant sentence
    return document_sentences[most_similar_index]

# main loop
while True:
    # get a question from the user
    question = input("You: ")
    # get the most relevant sentence from the document
    relevant_sentence = get_most_relevant_sentence(question)
    # print the relevant sentence
    print("ChatBot:", relevant_sentence)
