from MazeExamples import *
from Maze import Maze
from MazeSolver import MazeSolver
from MazeLoader import *

class TestClass:
    def test_length(self):
        maze_test = Maze()
        maze_test.initializer(maze1)
        assert maze_test.length == (6,5)
        maze_test = Maze()
        maze_test.initializer(maze2)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze3)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze4)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze7)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze8)
        assert maze_test.length == (20,20)
        maze_test = Maze()
        maze_test.initializer(maze9)
        assert maze_test.length == (17,18)
        maze_test = Maze()
        maze_test.initializer(maze10)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze11)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze12)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze13)
        assert maze_test.length == (10,10)
        maze_test = Maze()
        maze_test.initializer(maze14)
        assert maze_test.length == (10,10)

    def test_solution(self):
        maze_test = Maze()
        maze_test.initializer(maze1)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3)]

        maze_test = Maze()
        maze_test.initializer(maze2)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3), (2, 3), (2, 4), (2, 5), (1, 5), (1, 6), (1, 7), (1, 6), (1, 5), (2, 5), (2, 4), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (7, 3), (7, 4), (6, 4), (6, 5), (5, 5), (4, 5), (4, 6), (4, 7), (4, 8), (4, 7), (4, 6), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7)]

        maze_test = Maze()
        maze_test.initializer(maze4)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 8), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (7, 5), (7, 4), (7, 3), (7, 2), (8, 2)]

        maze_test = Maze()
        maze_test.initializer(maze7)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 5), (1, 6), (2, 6), (3, 6), (3, 7), (3, 8), (2, 8), (1, 8), (2, 8), (3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (8, 2), (7, 2), (6, 2), (6, 3), (5, 3), (6, 3), (6, 2), (7, 2), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

        maze_test = Maze()
        maze_test.initializer(maze8)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 1), (2, 1), (2, 2), (2, 3), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (4, 4), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (5, 5), (5, 6), (4, 6), (4, 7), (4, 8), (4, 7), (4, 6), (5, 6), (5, 5), (6, 5), (6, 4), (6, 3), (5, 3), (4, 3), (4, 4), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (8, 3), (8, 4), (8, 5), (9, 5), (10, 5), (10, 4), (11, 4), (11, 3), (11, 2), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (11, 2), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (18, 4), (18, 5), (17, 5), (16, 5), (15, 5), (14, 5), (13, 5), (13, 6), (12, 6), (12, 7), (11, 7), (10, 7), (9, 7), (8, 7), (8, 8), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (14, 8), (14, 7), (15, 7), (14, 7), (14, 8), (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (9, 9), (8, 9), (8, 8), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (12, 6), (13, 6), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (17, 6), (17, 7), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11), (17, 11), (17, 12), (17, 13), (16, 13), (15, 13), (15, 14), (15, 15), (14, 15), (13, 15), (12, 15), (12, 14), (11, 14), (10, 14), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (9, 11), (10, 11), (10, 12), (10, 11), (9, 11), (8, 11), (8, 12), (8, 13), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (17, 14), (17, 13), (17, 12), (17, 11), (18, 11), (18, 10), (18, 9), (18, 8), (18, 7), (17, 7), (17, 6), (17, 5), (18, 5), (18, 4), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (11, 4), (10, 4), (10, 5), (9, 5), (8, 5), (8, 4), (8, 3), (9, 3), (9, 2), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (4, 4), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (5, 5), (5, 6), (4, 6), (4, 7), (4, 8), (5, 8), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (5, 15), (4, 15), (3, 15), (2, 15), (2, 16), (2, 17), (3, 17), (4, 17), (5, 17), (6, 17), (7, 17), (8, 17), (9, 17), (10, 17), (11, 17), (12, 17), (13, 17), (14, 17), (15, 17), (16, 17), (17, 17), (18, 17), (18, 18)]

        maze_test = Maze()
        maze_test.initializer(maze9)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 1), (7, 1), (8, 1), (8, 2), (9, 2), (10, 2), (10, 1), (11, 1), (12, 1), (13, 1), (13, 2), (14, 2), (15, 2), (15, 1), (15, 2), (14, 2), (13, 2), (13, 1), (12, 1), (11, 1), (10, 1), (10, 2), (9, 2), (8, 2), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (9, 5), (10, 5), (10, 4), (11, 4), (12, 4), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (12, 8), (11, 8), (11, 9), (11, 10), (11, 11), (10, 11), (9, 11), (9, 12), (9, 13), (10, 13), (10, 14), (11, 14), (12, 14), (12, 13), (12, 12), (13, 12), (13, 11), (13, 10), (14, 10), (15, 10), (15, 11), (15, 10), (14, 10), (13, 10), (13, 11), (13, 12), (12, 12), (12, 13), (12, 14), (11, 14), (10, 14), (10, 13), (9, 13), (9, 12), (9, 11), (10, 11), (11, 11), (11, 10), (11, 9), (11, 8), (12, 8), (13, 8), (13, 7), (13, 6), (13, 5), (13, 4), (12, 4), (11, 4), (10, 4), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (4, 6), (4, 7), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 10), (3, 11), (4, 11), (5, 11), (5, 12), (6, 12), (7, 12), (7, 13), (7, 14), (7, 15), (8, 15), (9, 15), (9, 16), (10, 16), (11, 16), (12, 16), (13, 16), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13), (14, 13), (15, 13), (15, 14), (15, 15), (14, 15), (13, 15), (13, 16), (12, 16), (11, 16), (10, 16), (9, 16), (9, 15), (8, 15), (7, 15), (7, 14), (7, 13), (7, 12), (6, 12), (5, 12), (5, 11), (4, 11), (3, 11), (3, 10), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (2, 13), (2, 14), (1, 14), (1, 15), (1, 16), (2, 16), (3, 16), (3, 15), (4, 15), (5, 15), (5, 16)]

        maze_test = Maze()
        maze_test.initializer(maze11)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 5), (1, 6)]

        maze_test = Maze()
        maze_test.initializer(maze12)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5)]

        maze_test = Maze()
        maze_test.initializer(maze13)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (6, 3), (6, 2), (7, 2), (7, 1), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (4, 6), (3, 6), (4, 6), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (4, 6), (3, 6), (3, 7), (3, 8), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (2, 5)]

        maze_test = Maze()
        maze_test.initializer(maze14)
        maze_test_solving = MazeSolver(maze_test)
        maze_test_solving.solving()
        assert maze_test_solving.solution_finale == [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 2), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (8, 4), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7), (6, 6), (5, 6), (4, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (7, 1), (6, 1), (6, 2), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6)]

    def test_co_start(self):

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze2.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 1)


        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze3.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 1)

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze4.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 1)


        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze5.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 1)

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze6.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 1)


        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze7.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 1)


        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze8.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 1)


        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze9.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_start == (1, 3)

    def test_co_end (self):

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze2.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_end == (6, 7)

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze3.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_end == (5, 16)

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze4.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_end == (5, 16)

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze5.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_end == (15, 16)

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze5.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_end == (15, 16)

        loader_instance = MazeLoader()
        loader_instance.load_maze("maze_files/Maze5.txt")
        maze_test = Maze()
        maze_test.initializer(loader_instance.matrix)
        assert maze_test.co_end == (15, 16)
