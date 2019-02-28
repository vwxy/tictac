from flask import Flask, request, abort
from tictac_helper import is_valid, check_for_winner, make_move, find_best_move, score_move

app = Flask(__name__)


@app.route('/game')
def index():
	board = request.args.get('board')

	if not board:
		return 'please provide a board position'

	if not is_valid(board):
		abort(400)

	move, score = find_best_move(board, 'o', 3)
	return make_move(board, 'o', move)


if __name__ == '__main__':
	app.run()
