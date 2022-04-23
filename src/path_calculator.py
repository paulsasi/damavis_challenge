import src.board as board


def available_paths(initial_board: board.Board, depth: int) -> int:
    """Paths are scrapped using Breadth-first search (BFS) algorithm with early stopping. The implementation of DFS is
    done using a QUEUE data structure. Remark that for a tree (our case), we don't need to keep track of visited nodes.
    Take int account that BFS is a computationally expensive operation:
        - Time complexity: In general, O(V) where V is the number of nodes (you need to traverse all nodes at worst). For
            our case, with 4 possible moves and depth p, there are ~4^p nodes.
        - Space complexity: O(V) as well - since at worst case you need to hold all vertices in the queue.

    """

    # Considered board moves
    considered_moves = [
                            board.Board.move_player_up,
                            board.Board.move_player_down,
                            board.Board.move_player_left,
                            board.Board.move_player_right
    ]

    # Initialize queue
    queue = [initial_board]

    # Initialize searched level
    searched_level = 0

    while queue:
        current_level = len(queue)
        for _ in (reversed(range(current_level))):
            node_board = queue.pop(0)

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
