from operator import le


arq_txt = "C:\\Users\\gusta\\Crash Course on Python - by Google\\sample.txt"
with open(arq_txt, "r", encoding="utf-8") as file_contents:
    
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    frequencies = {} #Empty frequency is generated here
    f = file_contents
    
    for word in f:
        lista = word.split()
        for i in lista:
            i = i.lower()
            if i not in uninteresting_words and i.isalpha():
                if i not in frequencies.keys():
                    frequencies[i] = 0
                else:
                    frequencies[i] += 1
    frequencies
                