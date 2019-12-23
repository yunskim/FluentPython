l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')
# 생각해보면 list는 general container이니
# 무슨 값이 들어가있는 줄 알고 연산을 하겠습니까
# 그냥 길이를 늘이는 것이 안전할 따름입니다

# 2.5.1 리스트의 리스트 만들기
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

weird_board = [['_'] * 3] * 3
print(weird_board)

# 동일한 리스트에 대한 참조를 가진 리스트를 수정하면
# 원하는 결과가 나오지 않습니다

weird_board[1][2] = '0'
print(weird_board)

row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)

print(board)

board = []
for i in range(3):
    # 매 이터레이션마다 다른 참조를 생성합니다
    row = ['_'] * 3
    board.append(row)

print(board)
board[2][0] = 'X'
print(board)

