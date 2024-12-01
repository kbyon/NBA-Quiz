class NBAQuizQuestions:
    def __init__(self):
        """
        Initialize NBA quiz questions
        
        [List and Dictionaries] Using a list of dictionaries to store quiz questions
        """
        self.questions = [
            {
                "question": "Which NBA player is known as the 'Greek Freak'?",
                "options": ["LeBron James", "Giannis Antetokounmpo", "Kevin Durant", "Stephen Curry"],
                "correct_answer": "Giannis Antetokounmpo"
            },
            {
                "question": "How many NBA championships have the Chicago Bulls won?",
                "options": ["5", "6", "4", "3"],
                "correct_answer": "6"
            },
            {
                "question": "Who was the first overall draft pick in the 2018 NBA Draft?",
                "options": ["Luka Doncic", "Trae Young", "Deandre Ayton", "Mohamed Bamba"],
                "correct_answer": "Deandre Ayton"
            },
            {
                "question": "Which team has won the most NBA championships?",
                "options": ["Los Angeles Lakers", "Boston Celtics", "Golden State Warriors", "Chicago Bulls"],
                "correct_answer": "Boston Celtics"
            },
            {
                "question": "In what year did Michael Jordan retire for the first time?",
                "options": ["1993", "1994", "1995", "1992"],
                "correct_answer": "1993"
            }
        ]

    def get_random_question(self):
        """
        [Functions] Get a random question from the list
        
        Returns:
            dict: A random NBA quiz question
        """
        import random
        return random.choice(self.questions)

    def save_questions_to_file(self, filename='nba_questions.txt'):
        """
        [Files] Save questions to a text file
        
        Args:
            filename (str): Filename to save questions
        """
        # [Loops] Using a loop to write questions to file
        with open(filename, 'w') as f:
            for q in self.questions:
                f.write(f"Question: {q['question']}\n")
                f.write(f"Options: {', '.join(q['options'])}\n")
                f.write(f"Correct Answer: {q['correct_answer']}\n\n")
