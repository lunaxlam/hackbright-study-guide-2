"""Practice portion to build a range of classes that work together."""

class Student():
    """A student clas."""

    def __init__(self, first_name, last_name, address):
        "Initialize a Student class."

        self.first_name = first_name
        self.last_name = last_name
        self.address = address



class Question():
    """A question class."""

    def __init__(self, question, correct_answer):
        "Initialize a Question object."

        self.question = question
        self.correct_answer = correct_answer
    

    def ask_and_evaluate(self):
        # Print the question to the console and allow the user for an answer
        answer = input(self.question)

        if answer == self.correct_answer:
            return True
        
        return False


class Exam():
    """An exam class."""

    def __init__ (self, name):
        "Initialize an Exam object."

        self.name = name
        # A list of Question class objects
        self.questions = []
    

    def add_question(self, Question):
        """Take a Question and add it to the Exam instance's list of questions."""

        self.questions.append(Question)
    

    def administer(self):
        """Administer the exam."""


        for question in self.questions:
            
