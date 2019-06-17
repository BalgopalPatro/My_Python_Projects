#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
board = [0,1,2,3,4,5,6,7,8,9]


# In[2]:


def reset_board(board):
    board = [0,1,2,3,4,5,6,7,8,9]


# In[3]:


def print_board(board):
    clear_output()
    i = 1
    print('-------------')
    while i<=9:
        print('|',board[i],'|',board[i+1],'|',board[i+2],'|'+'\n'+'-------------')
        i = i+3


# In[4]:


def user_input():
    m = ''
    while not(m == 'X' or m == 'O'):
        m = input('Player 1 : What do you want to be X or O?', ).upper()
    if m == 'X':
        return ('X' , 'O')
    else:
        return ('O' , 'X')


# In[5]:


def place_mark(board,m,p):
    board[p] = m


# In[6]:


def win_check(board,m):
    return ( (board[1] == m and board[2] == m and board[3] == m ) or 
            (board[4] == m and board[5] == m and board[6] == m ) or
            (board[7] == m and board[8] == m and board[9] == m ) or 
            (board[1] == m and board[4] == m and board[7] == m ) or
            (board[2] == m and board[5] == m and board[8] == m ) or 
            (board[3] == m and board[6] == m and board[9] == m ) or
           (board[3] == m and board[5] == m and board[7] == m ) or 
           (board[1] == m and board[5] == m and board[9] == m ) ) 


# In[7]:


import random
def fst_player():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[8]:


def space_check(board,p):
    return board[p] == int(p)


# In[9]:


def board_full(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[10]:


def player_choice(board):
    
    p = 0
    
    while p not in range(1,10):
        p = int(input('Choose your position: (1-9)'))
    if not space_check(board,p):
        print('The position is alredy taken')
        player_choice(board)
    return p


# In[11]:



def replay():
    print('Do you want to play again ?? Y or N')
    ans = input().upper()
    while not ( ans == 'Y' or ans == 'N'):
        ans = input('Enter the Correct ANS : ')
    return ans == 'Y'


# In[ ]:


print('Welcome to Tic Tac Toe')

while True:
    board = [0,1,2,3,4,5,6,7,8,9]
    p1_m,p2_m = user_input()
    turn = fst_player()
    print(turn,' will go first')
    
    
    game = True
    
    while game:
        if turn == 'Player 1':
            
            print_board(board)
            print(turn)
            p = player_choice(board)
            place_mark(board,p1_m,p)
            
            if win_check(board,p1_m):
                print_board(board)
                print('Player 1 Win')
                game = False
                
            else :
                if board_full  (board):
                    print_board(board)
                    print('The game is Draw')
                    break
                else:
                    turn = 'Player 2'
        else:
            print_board(board)
            print(turn)
            p = player_choice(board)
            place_mark(board,p2_m,p)
            
            if win_check(board,p2_m):
                print_board(board)
                print('Player 2 Win')
                game = False
                
            else :
                if board_full  (board):
                    print_board(board)
                    print('The game is Draw')
                    break
                else:
                    turn = 'Player 1'
    if  not replay():
        clear_output()
        print('Thank You')
        break  
             


# In[ ]:




