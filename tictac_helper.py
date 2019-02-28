from collections import Counter

def is_valid(board):
	c = Counter(board)

	return len(board) == 9 \
			and set(board) - {'o','x',' '} == set() \
			and (c['x'] == c['o'] or c['x'] == c['o'] + 1) \
			and c[' '] != 0 \
			and not check_for_winner(board)


def check_for_winner(board):
	rows = [(0,1,2), (3,4,5), (6,7,8)]
	columns = [(0,3,6), (1,4,7), (2,5,8)]
	diagonals = [(0,4,8), (2,4,6)]
	lines = [board[i]+board[j]+board[k] for (i,j,k) in rows + columns + diagonals]

	if 'xxx' in lines:
		return 'x'
	elif 'ooo' in lines:
		return 'o'
	else:
		return None


def make_move(board, player, n):
	return board[:n] + player + board[n+1:]


def find_best_move(board, player, depth):
	next = {'x':'o', 'o':'x'}
	priorities = [4, 0, 2, 6, 8, 1, 3, 5, 7]
	spaces = [i for i in priorities if board[i]==' ']

	max_score = -99
	max_move = None

	for n in spaces:
		if depth == 0:
			score = -score_move(board, player, n)
		else:
			(move, score) = find_best_move(make_move(board, player, n), next[player], depth-1)
			(move, score) = (move, score - depth)

		score = -score
		if score > max_score:
			max_score = score
			max_move = n

	return (max_move, max_score)


def score_move(board, player, n):
	board = make_move(board, player, n)

	winner = check_for_winner(board)

	if winner == player:
		return 100
	elif winner and winner != player:
		return -100
	else:
		return 0
