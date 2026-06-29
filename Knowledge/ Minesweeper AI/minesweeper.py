import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        self.height = height
        self.width = width
        self.mines = set()

        self.board = []

        for i in range(self.height):
            row = []

            for j in range(self.width):
                row.append(False)

            self.board.append(row)

        while len(self.mines) != mines:

            i = random.randrange(height)
            j = random.randrange(width)

            if not self.board[i][j]:

                self.mines.add((i, j))
                self.board[i][j] = True


        self.mines_found = set()


    def print(self):

        for i in range(self.height):

            print("--" * self.width + "-")

            for j in range(self.width):

                if self.board[i][j]:
                    print("|X", end="")

                else:
                    print("| ", end="")

            print("|")

        print("--" * self.width + "-")


    def is_mine(self, cell):

        i, j = cell

        return self.board[i][j]


    def nearby_mines(self, cell):

        count = 0


        for i in range(cell[0] - 1, cell[0] + 2):

            for j in range(cell[1] - 1, cell[1] + 2):

                if (i, j) == cell:
                    continue


                if 0 <= i < self.height and 0 <= j < self.width:

                    if self.board[i][j]:

                        count += 1


        return count



    def won(self):

        return self.mines_found == self.mines

class Sentence():
    """
    Logical statement about a Minesweeper game.

    A sentence contains:
    - a set of cells
    - a count of how many cells are mines
    """


    def __init__(self, cells, count):

        self.cells = set(cells)
        self.count = count



    def __eq__(self, other):

        return (
            self.cells == other.cells
            and
            self.count == other.count
        )



    def __str__(self):

        return f"{self.cells} = {self.count}"



    def known_mines(self):

        """
        Returns cells that must be mines.
        """

        if len(self.cells) == self.count:

            return self.cells.copy()


        return set()



    def known_safes(self):

        """
        Returns cells that must be safe.
        """

        if self.count == 0:

            return self.cells.copy()


        return set()



    def mark_mine(self, cell):

        """
        Updates sentence after discovering a mine.
        """

        if cell in self.cells:

            self.cells.remove(cell)

            self.count -= 1



    def mark_safe(self, cell):

        """
        Updates sentence after discovering a safe cell.
        """

        if cell in self.cells:

            self.cells.remove(cell)
class MinesweeperAI():
    """
    Minesweeper game player
    """


    def __init__(self, height=8, width=8):

        self.height = height
        self.width = width


        # Cells already clicked
        self.moves_made = set()


        # Known mines
        self.mines = set()


        # Known safe cells
        self.safes = set()


        # Knowledge base
        self.knowledge = []



    def mark_mine(self, cell):

        """
        Marks a cell as a mine and updates knowledge.
        """

        self.mines.add(cell)


        for sentence in self.knowledge:

            sentence.mark_mine(cell)




    def mark_safe(self, cell):

        """
        Marks a cell as safe and updates knowledge.
        """

        self.safes.add(cell)


        for sentence in self.knowledge:

            sentence.mark_safe(cell)



    def make_safe_move(self):

        """
        Returns a safe cell that has not already been played.
        """

        for cell in self.safes:

            if cell not in self.moves_made:

                return cell


        return None





    def make_random_move(self):

        """
        Returns a random cell that:

        1. Has not already been chosen
        2. Is not known to be a mine
        """


        possible_moves = []


        for i in range(self.height):

            for j in range(self.width):

                cell = (i, j)


                if cell not in self.moves_made and cell not in self.mines:

                    possible_moves.append(cell)



        if possible_moves:

            return random.choice(possible_moves)


        return None



    def add_knowledge(self, cell, count):

        """
        Called when a safe cell is revealed.

        Updates knowledge base and makes deductions.
        """


        # 1. Record that we made this move
        self.moves_made.add(cell)


        # 2. Mark the cell as safe
        self.mark_safe(cell)



        # 3. Create new sentence from neighboring cells

        new_cells = set()


        for i in range(cell[0] - 1, cell[0] + 2):

            for j in range(cell[1] - 1, cell[1] + 2):


                neighbor = (i, j)


                # ignore current cell

                if neighbor == cell:
                    continue


                # check board boundaries

                if 0 <= i < self.height and 0 <= j < self.width:


                    # only unknown cells

                    if neighbor not in self.safes and neighbor not in self.mines:

                        new_cells.add(neighbor)



        new_sentence = Sentence(new_cells, count)



        if new_sentence not in self.knowledge:

            self.knowledge.append(new_sentence)




        # 4. Repeatedly make deductions

        changed = True


        while changed:

            changed = False



            # Find known mines

            mines_found = set()


            for sentence in self.knowledge:

                mines_found.update(sentence.known_mines())



            for mine in mines_found:

                if mine not in self.mines:

                    self.mark_mine(mine)

                    changed = True




            # Find known safes

            safes_found = set()


            for sentence in self.knowledge:

                safes_found.update(sentence.known_safes())



            for safe in safes_found:

                if safe not in self.safes:

                    self.mark_safe(safe)

                    changed = True




            # Remove empty sentences

            self.knowledge = [

                sentence

                for sentence in self.knowledge

                if len(sentence.cells) > 0

            ]




            # 5. Infer new sentences using subsets

            new_sentences = []


            for sentence1 in self.knowledge:


                for sentence2 in self.knowledge:


                    if sentence1 == sentence2:

                        continue



                    # if sentence1 is smaller subset

                    if sentence1.cells.issubset(sentence2.cells):


                        difference = sentence2.cells - sentence1.cells


                        count_difference = (
                            sentence2.count - sentence1.count
                        )


                        inferred = Sentence(
                            difference,
                            count_difference
                        )


                        if (

                            inferred not in self.knowledge
                            and
                            inferred not in new_sentences

                        ):

                            new_sentences.append(inferred)



            for sentence in new_sentences:

                self.knowledge.append(sentence)

                changed = True
