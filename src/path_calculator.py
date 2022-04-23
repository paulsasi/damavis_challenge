import src.board as board


def available_paths(initial_board: board.Board, depth: int) -> int:
    """Classic DFS algorithm with early stopping implemented with a QUEUE data structure."""

    # Considered board moves
    considered_moves = [
                            board.Board.move_player_up,
                            board.Board.move_player_down,
                            board.Board.move_player_left,
                            board.Board.move_player_right
    ]

    # Initialize queue
    queue = [initial_board]

    # Initialize visited
    visited = []

    # Initialize searched level
    searched_level = 0

    while queue:
        current_level = len(queue)
        for _ in (reversed(range(current_level))):
            node_board = queue.pop(0)

            if node_board in visited:
                continue
            visited.append(node_board)

            for move in considered_moves:
                try:
                    nei_node = move(node_board)
                    queue.append(nei_node)
                except board.BoardPossitionError:
                    pass
        searched_level += 1
        if searched_level == depth:
            break

    number_available_paths = len(queue)

    return number_available_paths
