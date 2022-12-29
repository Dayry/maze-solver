import unittest
from maze import Maze


class Tests(unittest.TestCase):

    def test1_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test2_maze_create_cells(self):
        num_cols = 60
        num_rows = 12
        m1 = Maze(5, 70, num_rows, num_cols, 2, 4)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test3_maze_create_cells(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(1, 1, num_rows, num_cols, 1, 1)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    # def test4_maze_create_cells(self):
    #         num_cols = 0
    #         num_rows = 0
    #         m1 = Maze(0, 0, num_rows, num_cols, 0, 0)
    #         self.assertEqual(
    #             len(m1._cells),
    #             num_cols,
    #         )
    #         self.assertEqual(
    #             len(m1._cells[0]),
    #             num_rows,
    #         )

    def test1_maze_entrance_exit_cells(self):
        num_cols = 10
        num_rows = 7
        m1 = Maze(20, 20, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False,
        )


if __name__ =="__main__":
    unittest.main()