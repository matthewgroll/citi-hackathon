import PyPDF2
import textract
import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def get_word_count(file_name):

    filename = file_name
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    num_pages = pdfReader.numPages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    if text != "":
        text = text
    else:
        text = textract.process(filename, method='tesseract', language = 'eng')

    tokens = word_tokenize(text)

    punctuations = ['(',')',';',':','[',']',',']

    stop_words = stopwords.words('english')
    keywords_list = [word for word in tokens if not word in stop_words and not word in punctuations]

    word_count = dict()

    for word in keywords_list:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def get_keywords(file_name):
    filename = file_name
    fileObj = pd.ExcelFile(filename)
    sheet_name = fileObj.sheet_names[0]
    df = fileObj.parse(sheet_name)
    keywords_dict = dict()
    for i in range(len(df)):
        keywords_dict[df['Field'][i]] = df['KeyWords'][i].split(',')
    
    return keywords_dict



def get_score(word_count, keywords):
    input_words = word_count.keys()
    scores = dict()
    max_score = dict()

    for field in keywords.keys():
        max_score[field] = len(keywords[field])
    
    for field in keywords.keys():
        score = 0
        for keyword in keywords[field]:
            if keyword in input_words:
                score += 1
            scores[field] = score/max_score[field]
    return scores
        
input_file = "resume.pdf"
word_count = get_word_count(input_file)

keyword_file = "keywords_DEMO.xlsx"
keywords = get_keywords(keyword_file)

scores = get_score(word_count, keywords)
print(scores)


