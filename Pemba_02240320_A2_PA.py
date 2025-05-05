import random

class gametime:
    def __init__(self):
        self.score_number_guess = 0
        self.score_rps = 0
        self.score_trivia = 0
    
    def display_menu(self):
         
         print("""select a function(1-4):
        1. Guess a number
        2. Rock Paper Scissor game
        3. Trivia pursuit game  
        4. show overall score
        5.  exit""")
         

    def run(self):
        
        while True:
            self.display_menu()

            choice = int(input('select your choice: '))

            if choice == 1:
               self.number_guessingGame()

            elif choice == 2 :
                 self.rockPaper_scissors()

            elif choice == 3:
                 self.triviaquiz()

            elif choice == 4:
                self.show_overall_score()
                
            elif choice == 5:
                exit()

            else:
                print("Out of range \n select a number between 1-5") 


    def number_guessingGame(self):
        min_num= 1
        max_num =100
        score = 100

        answer = random.randint(min_num,max_num)

        print(f"select a number between {min_num} and {max_num}")

        guesses = 0 
        while True:
            guess = int(input('enter your guess:'))
            guesses += 1
            score -= 5
            if guess == answer:
                print(f"Congrats! You got it, the Number is: {answer} ")
                print(f"the total guesses you have done is: {guesses}")    
                print(f" your score is {score}")

                if score < 40:
                    print (f"Do well next time! score is very low. Guess = {guesses}")
                self.score_number_guess += score
                break
                    

            elif guess > answer:
                print(f"its high, choose a lower one. Guess = {guesses}")

            elif guess < answer:
                print(f'it is low, select a higher one. Guess = {guesses}')

            else:
                print(f'out of range, select a number between {min_num} and {max_num}')

            


    def rockPaper_scissors(self):
        options = ("rock" , "paper" , "scissors")
        score = {"player": 0, "computer": 0}
        rounds_played= 0
        max_rounds= 4
  
        while True:
            player = None
            computer =random.choice(options)
            player = input(f"choose one from {options}: ").lower()
            rounds_played += 1

            print(f'player: {player}')
            print(f'computer: {computer}')

            while player not in options:
                player = input("Its is out of range, enter your choice (rock, paper,scissors): ")

            win = ((player == "rock" and computer == "scissors") or
                    (player == "scissors" and computer == "paper") or
                    (player == "paper" and computer == "rock"))
            
            draw = (computer == player)

            if win:
                print("You won!🎉")
                score["player"] += 2
            elif draw:
                    print("It's a draw!✌️")
            else:
                print("You lose!😒")
                score["computer"] += 2

            self.score_rps += score["player"]

        
            print(f"Score of the player: {score['player']}")
            print(f"Score of the computer: {score['computer']}")

            if rounds_played >= max_rounds:
                    break

    def triviaquiz(self):
        
        questions= ("what is the study of plant called? : ",
                "what is the biggest planet in the solar system? : ", 
                "what is the name of first satellite of Bhutan? : ",
                "who is referred to as Father of Modern Bhutan? : ",
                "what is the value of absolute temperature? : " )
    
        options = (("A. plantology", "B. botany" , "C. botanology", "D.Florist") ,
                ("A. Mars" , "B. Neptune" , "C. Jupiter" , "D. Saturn"),
                ("A. Bhu-sat I", "B. Satallite-I Bhutan", "C. Druk-satallite", "D. Bhutan-1"),
                ("A. Zhabdrung", "B. First King" , "C. Fourth King" , "D. Third King"),
                ("A. 0 Degree celsius" , "B. 0 kelvin" , "C. -100 Degree celsius" , "D. -15 Degree celsius"))
        
        answers= ("B" , "C" , "D" , "D" , "B")

        choices =[]
        score = 0
        question_num = 0

        for question in questions:
            print("..................................................")
            print(question)

            for option in options[question_num]:
                print(option)

            choice = input("Enter your answer (A, B, C, D) : ").upper()
            choices.append(choice)
        
            if choice== answers[question_num]:
                print("Well Done!")
                score +=2 
            else:
                print(f"Sorry!Correct answer is {answers[question_num]}")

            question_num +=1

        print(" ***** RESULTS ****")

        print("Correct answers : ",*answers)

        print(".....Your answer: ", *choices)

        self.score_trivia += score

        print(f"\nYou scored {score} out of 10.")

    
    def show_overall_score(self):
        print("\n====== Score Summary ======")
        print(f"Number Guessing Score: {self.score_number_guess}")
        print(f"Rock-Paper-Scissors Score: {self.score_rps}")
        print(f"Trivia Quiz Score: {self.score_trivia}\n")

        print("===========================\n")

        total_score = self.score_number_guess + self.score_rps + self.score_trivia
        print(f"Total score so far = {total_score} \n")



if __name__== "__main__":
    game = gametime()
    game.run()


    