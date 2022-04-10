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
        """Print a question to the console and ask the user for an answer.
        
        Return True or False depending on if the answer is correct (True for correct answers)."""

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

        # Initialize a variable to track the total number of correct answers
        correct_answers = 0

        # Iterate through each question
        for question in self.questions:
            # Ask and evaluate the question
            answer = question.ask_and_evaluate()
            # Check if answer is True; if so then increment total number of correct answers
            if answer == True:
                correct_answers += 1
        
        # Calculate the percentage of correct answers
        tally_correct = correct_answers / len(self.questions)

        return tally_correct


