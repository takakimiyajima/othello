# coding=utf-8

WHITE = 0
BLACK = 1
BOARD_SIZE = 8


class OthelloBoard(object):

    def __init__(self):
        # 2次元リストを生成する
        # 各要素の初期値はNone
        self.cells = []
        for i in range(BOARD_SIZE):
            self.cells.append([None for i in range(BOARD_SIZE)])

        # 4つの石を初期配置する
        self.cells[3][3] = WHITE
        self.cells[3][4] = BLACK
        self.cells[4][3] = BLACK
        self.cells[4][4] = WHITE

    def put_disk(self, x, y, player):

        """指定した座標に指定したプレイヤーの石を置く
        Args:
            x: 置く石のX座標
            y: 置く石のY座標
            player: 石を置こうとしているプレイヤー(WHITEまたはBLACK)

        Returns:
            True: 関数の成功を意味する. 指定した座標と
                それによって獲得できる石がすべてplayerの色になった場合に返す
            False: 関数が以下のいずれかのケースによって失敗した場合に返す
                ・指定した座標に既に別の石がある
                ・指定した座標に石を置いても相手側の石を獲得できない
        """

        # 既にほかの石があれば置くことができない
        # if self.cells[y][x] is not None:
        #     return False

        # # 獲得できる石がない場合も置くことができない
        # flippable = self.list_flippable_disks(x, y, player)
        # if not flippable:
        #     return False

        # # 実際に石を置く処理
        # self.cells[y][x] = player
        # for x,y in flippable:
        #     self.cells[y][x] = player

        # return True


board = OthelloBoard()
print(board.cells)