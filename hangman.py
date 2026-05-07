import random
words = ['sugarplum', 'centipide', 'fingernail', 'apricot', 'pinapple', 'firefighter', 'language', 'leftovers', 'question', 'alternate', 'paradise', 'anteater', 'marvelous', 'dumplings', 'americano']


class Word:
    def __init__(self, word_itself, attempts = 6):
        self.word_itself = word_itself
        self.guessed_letters = set()
        self.all_guessed_letters = set()
        self.attempts = attempts

    def add_guessed_letter(self):
        letter = input('Insert letter or full word').lower()

        if len(letter) == 1:
            if letter in self.word_itself:
                self.guessed_letters.add(letter)
                self.all_guessed_letters.add(letter)
                return 'You\'ve got that!'
            
            else:
                self.attempts -= 1
                print(f'{self.attempts} attempts left')
                if letter in self.all_guessed_letters:
                    print('I won\'t let u redo that') #я знаю что повторный ввод не должен наказываться и то что это дело 1го иф-элса, но я злой
                self.all_guessed_letters.add(letter)
                return 'Nah bro, try again'
                

        else:
            if letter == self.word_itself:
                self.guessed_letters = set(self.word_itself)
                return 'You\'ve got that'
            else:
                self.attempts -= 1
                print(f'{self.attempts} attempts left')
                return 'Not this one'
        

            

    def idle(self, full_word = ''):
        print(f'Guessed letters:{', '.join(self.all_guessed_letters)}')
        for i in range(len(self.word_itself)):
            letter = self.word_itself[i]
            if letter in self.guessed_letters:
                    full_word += letter
            else:
                    full_word += '_'
        return full_word
            



def save_to_history(word, result):
    with open('history.txt', 'a') as a:
        a.write(f"Word: {word} Result: {result}\n")



def show_history():
    try:
        print('\n---GAME---HISTORY---')
        with open('history.txt', 'r') as b:
            content = b.read()
            print(content)
    except:
        print('No history yet')
        

    

def main():
    while True:
        print('\n---HANGMAN---THE---GAME---')
        print('1.New game')
        print('2.Show history')
        print('3.Exit')
        choice = input('What do ya want??:')


        if choice == '1':

            hangman = Word(random.choice(words))
        
            while True:
                print(hangman.idle())
                print(hangman.add_guessed_letter())
                if set(hangman.word_itself) == hangman.guessed_letters:
                    print(f'You win!')
                    save_to_history(hangman.word_itself, 'won')
                    break
                if hangman.attempts <= 0:
                    print(f'You lose! The answer was: {hangman.word_itself}')
                    save_to_history(hangman.word_itself, 'lost')
                    break


        elif choice == '2':
            show_history()


        elif choice == '3':
            break
        

        else:
            print("What")

if __name__ == '__main__':
    main()
