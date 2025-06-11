def table(x_moves, o_moves):
    zero = "X" if x_moves[0] else ("O" if o_moves[0] else 0)
    one = "X" if x_moves[1] else ("O" if o_moves[1] else 1)
    two = "X" if x_moves[2] else ("O" if o_moves[2] else 2)
    three = "X" if x_moves[3] else ("O" if o_moves[3] else 3)
    four = "X" if x_moves[4] else ("O" if o_moves[4] else 4)
    five = "X" if x_moves[5] else ("O" if o_moves[5] else 5)
    six = "X" if x_moves[6] else ("O" if o_moves[6] else 6)
    seven = "X" if x_moves[7] else ("O" if o_moves[7] else 7)
    eight = "X" if x_moves[8] else ("O" if o_moves[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")

def check (x_moves,o_moves):
    winning = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for win in winning :
        if((x_moves[win[0]] + x_moves[win[1]] + x_moves[win[2]]) == 3):
            print("\nX won")
            return 1
        if((o_moves[win[0]] + o_moves[win[1]] + o_moves[win[2]]) == 3):
            print("\nO won")
            return 0
    return -1


if __name__ ==  "__main__":
    x_moves = [0,0,0,0,0,0,0,0,0]
    o_moves = [0,0,0,0,0,0,0,0,0]
    chance = 1
    while (True):
          table(x_moves,o_moves)
          if(chance == 1):
               print("X's turn")
               value = int(input("please enter your value :- "))
               x_moves[value] = 1

          else:
            print("O's turn")
            value = int(input("please enter your value :- "))
            o_moves[value] = 1

          win_check = check(x_moves,o_moves)
          if win_check != -1:
            print("good game well played boss")
            print('play again')
            break
          chance = 1 - chance
        
      