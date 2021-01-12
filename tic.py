from tkinter import *

class Player:

    def __init__(self, start):
        """
        arguments:
            start: represent if it's the first or the second player take 1 or 2
        """

        if start != 1 and start != 2:
            raise ValueError()

        if start == 1:
            self.symbol = "0"
        else:
            self.symbol = "X"


class Board:

    def __init__(self):

        self.turn = "O"

        self._board = {
            (1,1) : None,
            (1,2) : None,
            (1,3) : None,
            (2,1) : None,
            (2,2) : None,
            (2,3) : None,
            (3,1) : None,
            (3,2) : None,
            (3,3) : None,
        }

        self._win_combinaisons = [
            ((1,1), (1,2), (1,3)),
            ((2,1), (2,2), (2,3)),
            ((3,1), (3,2), (3,3)),
            ((1,1), (2,1), (3,1)),
            ((1,2), (2,2), (3,2)),
            ((1,3), (2,3), (3,3)),
            ((1,1), (2,2), (3,3)),
            ((1,3), (2,2), (3,1)),
        ]

    def __getitem__(self, index):
        if index[0] > 3 or index[1] > 3 or index[0] < 1 or index[1] < 1:
            raise IndexError("")

        return self._board[index]

    def __setitem__(self, index, value):
        if index[0] > 3 or index[1] > 3 or index[0] < 1 or index[1] < 1:
            raise IndexError("")

        if value != "O" and value != "X":
            raise ValueError("")

        if self._board[index] != None:
            raise AlreadySelectedError("man this case is already selected")

        self._board[index] = value
        self.__inverse_turns()

    def __inverse_turns(self):
        if self.turn == "O":
            self.turn = "X"
        elif self.turn == "X":
            self.turn = "O"

    def check_saturation(self):
        for index, value in self._board.items():
            if value == None:
                return False
        return True

    def check_winer(self):
        for combinaison in self._win_combinaisons:
            value = self.check_combinaison(combinaison)
            if value != False:
                return value, combinaison
        return False

    def check_combinaison(self, combinaison):
        if self._board[combinaison[0]] == None:
            return False
        else:
            if self._board[combinaison[0]] != self._board[combinaison[1]]:
                return False
            else:
                if self._board[combinaison[0]] != self._board[combinaison[2]]:
                    return False
                else:
                    return self._board[combinaison[0]]


class AlreadySelectedError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return message


class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("tic-tac-toe")

        self.init_board()
        self.init_elements()

        self.root.mainloop()

    def init_board(self):
        player1 = Player(1)
        player2 = Player(2)

        self.my_board = Board()

    def button_click(self, button, index):
        turn = self.my_board.turn
        try:
            self.my_board[index] = self.my_board.turn
        except AlreadySelectedError:
            print("this case has already been selectioned")
        else:
            button.configure(text=turn ,state=DISABLED)
            return_value = self.my_board.check_winer()

            if return_value == False:
                if(self.my_board.check_saturation()):
                    self.end_label.configure(text="it's a Drawn")
                    print("it's a Drawn")
            else:
                winer, combinaison = return_value
                self._color_winner(combinaison)
                self._disable_buttons()
                if winer == "O":
                    self.end_label.configure(text="'O' win")
                    print("'O' win")
                elif winer == "X":
                    self.end_label.configure(text="'X' win")
                    print("'X' win")


    def init_elements(self):

        top_lab = Label(text="Welcome To this Game of tic-tac-toe", font=("open sans", 15))

        #init buttons
        self.b1 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b1, (1,1)))
        self.b2 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b2, (1,2)))
        self.b3 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b3, (1,3)))

        self.b4 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b4, (2,1)))
        self.b5 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b5, (2,2)))
        self.b6 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b6, (2,3)))

        self.b7 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b7, (3,1)))
        self.b8 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b8, (3,2)))
        self.b9 = Button(self.root, text=" ", font=("open sans", 30), height=3, width=6,
                    bg="#DEDEDE", command=lambda: self.button_click(self.b9, (3,3)))

        space = " "*30
        self.end_label = Label(text=space, font=("open sans", 15))

        restart = Button(self.root, text="Restart", font=("open sans", 12),
                    bg="#DEDEDE", command=lambda: self.restart())

        top_lab.grid(row=0, columnspan=3)

        self.b1.grid(row=1, column=0)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=1, column=2)

        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)

        self.b7.grid(row=3, column=0)
        self.b8.grid(row=3, column=1)
        self.b9.grid(row=3, column=2)

        self.end_label.grid(row=4, columnspan=3)
        restart.grid(row=5, column=2)

    def _disable_buttons(self):
        self.b1.configure(state=DISABLED)
        self.b2.configure(state=DISABLED)
        self.b3.configure(state=DISABLED)
        self.b4.configure(state=DISABLED)
        self.b5.configure(state=DISABLED)
        self.b6.configure(state=DISABLED)
        self.b7.configure(state=DISABLED)
        self.b8.configure(state=DISABLED)
        self.b9.configure(state=DISABLED)

    def _color_winner(self, winner_cases):
        cases_equivalence = {
            (1,1) : self.b1,
            (1,2) : self.b2,
            (1,3) : self.b3,
            (2,1) : self.b4,
            (2,2) : self.b5,
            (2,3) : self.b6,
            (3,1) : self.b7,
            (3,2) : self.b8,
            (3,3) : self.b9,
        }

        for case in winner_cases:
            cases_equivalence[case].configure(bg="#90ee90")

    def restart(self):
        self.init_board()
        self.init_elements()

def main():
    user_interface = GUI()


if __name__ == '__main__':
    main()
