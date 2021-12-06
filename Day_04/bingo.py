class Bingo(object):

    def __init__(self, text):
        self.board = []
        self.marked = []
        for line in text:
            nums = line.split()
            self.board.append([int(n) for n in nums])
            self.marked.append([False for n in nums])

    def mark(self, n):
        """
        Designate number "n" on the board as marked.
        If the number n was found on the board, return True.
        Otherwise, return false.
        :param n: a number to mark
        :return: True if the board state was modified
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == n:
                    self.marked[i][j] = True
                    return True
        return False

    def winning(self):
        """
        :return: True if the board is in a winning state, False otherwise
        """
        # Check for winning rows
        for row in self.marked:
            if all(row):
                return True
        # Check for winning columns
        for col in range(len(self.marked[0])):
            if all(self.marked[row][col] for row in range(len(self.marked))):
                return True
        return False

    def score(self):
        """
        :return: the sum of all unmarked numbers on the board
        """
        return sum(self.board[x][y] for x in range(5) for y in range(5) if not self.marked[x][y])

    def __str__(self):
        s = ""
        for row in range(5):
            s += "|"
            for col in range(5):
                s += f"{self.board[row][col]: 3d}"
                s += "* |" if self.marked[row][col] else "  |"
            s += "\n"
        return s


def play_bingo(data, wins=1):
    drawings = [int(n) for n in data.pop(0).split(",")]
    data.pop(0)
    boards = []
    temp = []
    for d in data:
        if d.strip():
            temp.append(d.strip())
        else:
            boards.append(Bingo(temp))
            temp = []

    if temp:
        boards.append(Bingo(temp))

    games_won = 0
    for n in drawings:
        for b in boards:
            # skip boards we have already won
            if b.winning():
                continue
            # Mark this number on this board; if the board is now
            # a winning board, update the win count and see if we're done.
            if b.mark(n):
                if b.winning():
                    games_won += 1
                    if games_won >= wins:
                        return b.score() * n

    return None
