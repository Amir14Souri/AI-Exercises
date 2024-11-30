from player import Player

class MinimaxPlayer(Player):
    def __init__(self, player_number, board, depth=3):
        super().__init__(player_number, board)
        self.depth = depth
        
    def max_value(self, imaginary, depth):
        if depth == self.depth:
            return self.greedy_node_player(imaginary)
        
        max_value = -float('inf')
        best_move = None
        moves = []
        range_n = 0, self.board.get_n()
        step = 1
        if self.player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
        for i in range(range_n[0], range_n[1], step):
            for j in range(range_n[0], range_n[1], step):
                if self.board.get_board_grid()[i][j] == self.player_number:
                    for direction in self.board.get_possible_directions(self.player_number):
                        move = (i, j), (i + direction[0], j + direction[1])
                        self.board.start_imagination()
                        if self.board.is_move_valid(self.board.get_imaginary_board(), move, self.player_number):
                            scores, game_over = self.board.place_piece_imaginary(move, self.player_number)

                            if game_over == self.player_number:
                                max_value = float('inf')
                                best_move = move
                            else:
                                node_value = self.min_value(self.board.imaginary_board_grid, depth + 1)[1]
                                if node_value > max_value:
                                    max_value = node_value
                                    best_move = move
                                
        return best_move, max_value
        
    def min_value(self, imaginary, depth):
        if depth == self.depth:
            return self.greedy_node_opponent(imaginary)
        
        min_value = float('inf')
        best_move = None
        moves = []
        range_n = 0, self.board.get_n()
        step = 1
        if self.player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
        for i in range(range_n[0], range_n[1], step):
            for j in range(range_n[0], range_n[1], step):
                if self.board.get_board_grid()[i][j] == self.player_number:
                    for direction in self.board.get_possible_directions(self.player_number):
                        move = (i, j), (i + direction[0], j + direction[1])
                        self.board.start_imagination()
                        if self.board.is_move_valid(self.board.get_imaginary_board(), move, self.player_number):
                            scores, game_over = self.board.place_piece_imaginary(move, self.player_number)

                            if game_over == self.player_number:
                                min_value = -float('inf')
                                best_move = move
                            else:
                                node_value = self.max_value(self.board.imaginary_board_grid, depth + 1)[1]
                                if node_value < min_value:
                                    min_value = node_value
                                    best_move = move
                                
        return best_move, min_value
    
    def greedy_node_player(self, imaginary):
        max_value = -float('inf')
        best_move = None
        range_n = 0, self.board.get_n()
        step = 1
        if self.player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
        for i in range(range_n[0], range_n[1], step):
            for j in range(range_n[0], range_n[1], step):
                if self.board.get_board_grid()[i][j] == self.player_number:
                    for direction in self.board.get_possible_directions(self.player_number):
                        move = (i, j), (i + direction[0], j + direction[1])
                        self.board.start_imagination()
                        if self.board.is_move_valid(self.board.get_imaginary_board(), move, self.player_number):
                            scores, game_over = self.board.place_piece_imaginary(move, self.player_number)

                            if game_over == self.player_number:
                                max_value = float('inf')
                                best_move = move
                            else:
                                if scores[self.player_number] > max_value:
                                    max_value = scores[self.player_number]
                                    best_move = move
                                
        return best_move, max_value
    
    def greedy_node_opponent(self, imaginary):
        max_value = -float('inf')
        best_move = None
        range_n = 0, self.board.get_n()
        step = 1
        if self.player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
        for i in range(range_n[0], range_n[1], step):
            for j in range(range_n[0], range_n[1], step):
                if self.board.get_board_grid()[i][j] == self.player_number:
                    for direction in self.board.get_possible_directions(self.player_number):
                        move = (i, j), (i + direction[0], j + direction[1])
                        self.board.start_imagination()
                        if self.board.is_move_valid(self.board.get_imaginary_board(), move, self.player_number):
                            scores, game_over = self.board.place_piece_imaginary(move, self.player_number)

                            if game_over == self.player_number:
                                scores = {self.player_number: float('inf'), self.opponent_number: -float('inf')}
                            elif game_over == self.opponent_number:
                                scores = {self.player_number: -float('inf'), self.opponent_number: float('inf')}
                            else:
                                if scores[self.opponent_number] > max_value:
                                    max_value = scores[self.opponent_number]
                                    best_move = move
                                
        return best_move, max_value
        

    def get_next_move(self):
        self.board.start_imagination()
        imaginary_board = self.board.get_imaginary_board()
        move, score = self.max_value(imaginary_board, 1)
        return move