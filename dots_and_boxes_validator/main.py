import math
def dots_and_boxes(ar):
    # your code goes here. the sleeper must awaken!
    ar = ((0,1),(7,8),(1,2),(6,7),(0,3),(5,8),(3,4),(1,4),(4,5),(2,5),(4,7),(3,6))
    n = find_board_size(ar)
    all_boxes(ar,n)
    return None


def find_board_size(ar):
    '''find the size of the board that has been played on.
    So we can work out which moves make a square together'''

    # find the last dot of the board. first dot is always 0
    last_dot = max(max(ar))

    # Boards are always n x n, find n
    n = math.sqrt(last_dot+1) # +1 because boards start at 0\
    n=int(n)

    print(f'Board is {n} x {n} big, so numbers in rows are {n} apart')

    return n

def all_boxes(ar, n):
    '''find out which numbers together make a box'''

    # sort moves into a list
    ar_as_list = [t for t in ar]
    sorted_ar = sorted(ar_as_list)

    # find out which moves are horizontal and which are vertical
    horizontal_lines = []
    vertical_lines = []
    for pair in sorted_ar:
        if pair[1] - pair[0] == 1:
            horizontal_lines.append(pair)
        elif pair[1] - pair[0] == n:
            vertical_lines.append(pair)
        else:
            print("wtf")
    
    print("hor", horizontal_lines)
    print("ver", vertical_lines)

    # find out which boxes are in the game
    my_boxes = []
    for item in horizontal_lines:
        # we take a point and search for its "brothers", which together make a box
        # since we sorted our lists, we will start from line (0,1)
        print("finding brothers of: ", item)
        h_brother = None
        v_brother = None
        v_brother2 = None

        # the other horizontal line is right below both points. The difference between the points is always n
        for h_item in horizontal_lines:
            if min(h_item) - n == min(item) and max(h_item) - n == max(item):
                print("found h_brother: ", h_item)
                h_brother = h_item
                break # no need to search any other lines
        
        # for both vertical lines, there is always a difference of n between either the minimum point or the maximum point
        for v_item in vertical_lines:
            # the first vertical line has the same starting point as the first horizontal line
            if min(v_item) == min(item) and max(v_item) == min(item) + n:
                print("found v_brother: ", v_item)
                v_brother = v_item
            # the second vertical line has the same starting point as where the first horizontal line ends
            if min(v_item) == max(item) and max(v_item) == max(item) + n:
                print("found v_brother2: ", v_item)
                v_brother2 = v_item
        
        # If any of our searches turned up empty, one or more of these variables should be empty, so we cannot make a box
        if h_brother == None or v_brother == None or v_brother2 == None:
            print("cant make box")
        else:
            box = []
            box.append(item)
            box.append(h_brother)
            box.append(v_brother)
            box.append(v_brother2)
            # carry found box outside loop
            my_boxes.append(box)





    
    print("my boxes:")
    for b in my_boxes:
        print(b)

    # a box consists of 2 horz lines and 2 vert lines

dots_and_boxes(0)