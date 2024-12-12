'''1. Create a class that validates the password which contains various methods to validate the
password.
Get input from the user and validate the password.
Write a program to validate the password based on these rules and provide feedback(Valid
or invalid).
Password rules:
At least one uppercase letter.
At least one lowercase letter.
At least one digit.
At least one special character.
Minimum length of 8 characters.'''
class Password:
    def __init__(self):
        self.password=input("Enter the password")
        self.length=len(self.password)
        self.l=False
        self.upper=False
        self.lower=False
        self.digit=False
        self.char=False
    def check_len(self):
        if self.length>8:
            self.l=True
    def check_upper(self):
        for i in self.password:
            if i.isupper()==True:
                self.upper=True
                break
    def check_lower(self):
        for i in self.password:
            if i.islower()==True:
                self.lower=True
                break
    def check_digit(self):
        for i in self.password:
            if i.isdigit()==True:
                self.digit=True
                break
    def check_special(self):
        for i in self.password:
            if not i.isalnum():
                self.char=True
                break
    def display(self):
        if self.l and self.upper and self.lower and self.digit and self.char==True:
            print("The given password is valid")
        else:
            print("The given password is not valid")
p=Password()
p.check_len()
p.check_upper()
p.check_lower()
p.check_digit()
p.check_special()
p.display()   

'''2
Create a class program that takes a paragraph of text as input and splits it into individual
sentences. Additionally, process each sentence to provide useful information, such as word
count or other linguistic analysis."
Requirements:
Design a class called TextProcessor.
Include a method to split the text into sentences (split_into_sentences).
Include a method to further process each sentence (process_sentences), such as counting
words.
Sample :
Input: "Hello! How are you? I am fine. Let's learn NLP."
Output:
Split Sentences:
o "Hello!"
o "How are you?"
o "I am fine."
o "Let's learn NLP."
Processed Sentence Data:
o Sentence: "Hello!", Word Count: 1
o Sentence: "How are you?", Word Count: 3
o Sentence: "I am fine.", Word Count: 3
o Sentence: "Let's learn NLP.", Word Count: 3'''

class Textprocessor:
    def __init__(self):
        self.text=input("Enter your text").strip()
        
        
    def split_into_sentences(self):
        sentences=[]
        split=""
        for i in range(len(self.text)):
            split+=self.text[i]
            if self.text[i] in ".!,?":
                
                sentences.append(split)
                split=""
        if split.strip():
            sentences.append(split.strip())
        print(sentences)
        for sentence in sentences:
            word_count = len(sentence.split())
            print(f"{sentence} - count: {word_count}")
t=Textprocessor()
t.split_into_sentences()


