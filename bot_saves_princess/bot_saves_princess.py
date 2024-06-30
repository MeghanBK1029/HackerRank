#!/usr/bin/python

from typing import List, Tuple

def _get_location(letter: str, grid: List[str]) -> Tuple[int, int]:
    """
    Args:
        letter: the letter in the grid to find
        grid: the grid to search for letter
        
    Returns:
        (x, y) location of letter in grid
    """
    for y, row in enumerate(grid):
        if letter in row:
            return (row.find(letter), y)
    
    
def _get_x_direction_name(x_direction: int) -> str:
    """
    Args:
        x_direction: the number of moves in the x axis
        
    Return:
        String of direction_name either LEFT, RIGHT where a negative 
            movement is LEFT and a positive movement is RIGHT
    """
    if x_direction > 0:
        x_direction_name = "RIGHT"
    else:
        x_direction_name = "LEFT"
        
    return x_direction_name
   
    
def _get_y_direction_name(y_direction: int) -> str:
    """
    Args:
        y_direction: the number of moves in the x axis
        
    Return:
        String of direction_name either DOWN, UP where a negative 
            movement is DOWN and a positive movement is UP
    """
    if y_direction > 0:
        y_direction_name = "DOWN"
    else:
        y_direction_name = "UP"
        
    return y_direction_name

    
def _get_direction_str(direction_name: str, direction_length: int) -> str:
    """
    Args:
        direction_name: name of direction (LEFT, RIGHT, UP or DOWN)
        direction_length: number of moves in direction
        
    Return:
        String of direction_name multiplied by direction_length
    """
    direction_str = ""
    
    for i in range(0, abs(direction_length)):
        direction_str += direction_name + "\n"
        
    return direction_str
    
    
def displayPathtoPrincess(n: int, grid: List[str]) -> str:
    """
    The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive 
    lines to rescue/reach the princess. The goal is to reach the princess in 
    as few moves as possible.
    
    Args:
        n: an odd integer N (3 <= N < 100) denoting the size of the grid
        grid: an NxN grid. Each cell is denoted by '-' (ascii value: 45). 
            The bot position is denoted by 'm' and the princess position 
            is denoted by 'p'.
            
    Returns:
        The moves you will take to rescue the princess in one go. The moves
            must be separated by '\n', a newline. The valid moves are LEFT or 
            RIGHT or UP or DOWN.
    """
    (x_p, y_p) = _get_location("p", grid)
    (x_m, y_m) = _get_location("m", grid)
    
    x_direction = x_p - x_m
    x_direction_name = _get_x_direction_name(x_direction)
    x_direction_str = _get_direction_str(x_direction_name, abs(x_direction))
        
    y_direction = y_p - y_m
    y_direction_name = _get_y_direction_name(y_direction)
    y_direction_str = _get_direction_str(y_direction_name, abs(y_direction))
    
    direction_str = (x_direction_str + y_direction_str)[:-1]
    print(direction_str)
    return direction_str


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
    
    
displayPathtoPrincess(m, grid)