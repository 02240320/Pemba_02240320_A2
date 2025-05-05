print(" 🙌Welcome to pokemon card binder Manager! ")

binder={}
max_pokedex = 1025

class Pokedex:

    def print_menu(self):     
        print("1. add pokemon card")
        print("2. Reset binder")
        print("3. View current placement")
        print("4. Exit")

    def run(self):

        while True:
            self.print_menu()
            choice = int(input('select your choice: '))

            if choice == 1:
                self.add_card()

            elif choice == 2 :
                self.reset_binder()

            elif choice == 3:
                self.view_CardAdded()
                
            elif choice == 4:
                exit()

            else:
                print(" select a number between 1-4") 


    def add_card(self):
        try:
            num =int(input("Enter Pokedex number🖋️: "))

            if num < 1 or num > max_pokedex:
                print("It is out of range \n Enter number between 1 and 1025 🤦‍♂️.")
                return
            

            if num in binder :
                print(f"pokedex {num} is already in the binder")
                return
            
            page = (num -1 ) // 64 + 1
            index = (num-1) % 64
            row = index // 8+1
            col = index % 8+1

            binder[num]= {'page': page, 'row': row, 'column': col}

            print(f"page : {page}")
            print(f"position : row {row}, column {col}")
            print(f"status: Added Pokedex {(num), binder[num]} to binder")

        except ValueError:
            print("error: please enter a valid number")


    def reset_binder(self):
        print("WARNING: This will delete ALL pokemon cards from the binder.\n This action cannot be undone")

        choice = input("Type 'CONFIRM' to reset or 'EXIT' to return to Main Menu: ")

        if choice.upper() == 'CONFIRM':
            binder.clear()
            print("The binder reset is successful! \n All cards have been REMOVED")

        elif choice.upper() == 'EXIT':
            print("binder Reset Cancelled")

        else:
            print("Invalid Input!")

    def view_CardAdded(self):
   
        if len(binder)== 0:
            print("\n The binder is Empty! \n ")

        else:

            print(" \n The cards added in the binder are: ")
            for num in sorted(binder.keys()):
                print(f"Pokedex {num}: ")
                print(f"page : {binder[num]['page']}")
                print(f"position : row {binder[num]['row']}, column {binder[num]['column']}")

            print(f" **** Total cards in binder: {len(binder)}")

            per_completion = (len(binder)/max_pokedex)*100 
            print(f" \n The percentage completion = {per_completion: .2f} % \n" )
            if per_completion == 100:
                print("YOU have caught them all!")

if __name__ == "__main__":
    game = Pokedex()
    game.run()