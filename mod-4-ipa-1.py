'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return str("friends")
    elif from_member in social_graph[to_member]["following"]:
        return str("followed by")
    elif to_member in social_graph[from_member]["following"]:
        return str("follower")
    else:
        return str("no relationship")


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for horizontal, horizontal_2 in enumerate(board):
        if len(set(horizontal_2)) == 1:
            final_horizontal_set = (set(horizontal_2))
            final_horizontal_string = " ".join(map(str,final_horizontal_set))
            return (final_horizontal_string)
    for vertical in zip(*board):
        if len(set(vertical)) == 1:
            final_vertical_set = (set(vertical))
            final_vertical_string = " ".join(map(str,final_vertical_set))
            return (final_vertical_string)
    if len(set([board[(len(host)-1)-c][c] for c, host in enumerate(board)])) == 1:
        final_down_up_set = (set([board[(len(host)-1)-c][c] for c, host in enumerate(board)]))
        final_down_up_string = " ".join(map(str,final_down_up_set))
        return (final_down_up_string)
    elif len(set([board[a][a] for a,b in enumerate(board)])) == 1:
        final_up_down_set = (set([board[a][a] for a,b in enumerate(board)]))
        final_up_down_string = " ".join(map(str, final_up_down_set))
        return (final_up_down_string)
    else:
        return ("no winner")
    

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predebonifined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    x = []
    x.append(first_stop)
    x.append(second_stop)
    x = tuple(x)
    legs = route_map
    y = legs.keys()
    z = []
    eta = 0
    if first_stop == second_stop:
        eta = 0
    elif x in legs.keys():
        eta = legs[x]["travel_time_mins"]
    else:
        while second_stop != z:
            for i in range(len(legs.keys())):
                x = []
                x.append(first_stop)
                y = legs.keys()
                y = list(y)
                y = y[i]
                y = list(y)
                y = y[1]
                x.append(y)
                x = tuple(x)
                if x in legs.keys():
                    eta += legs[x]["travel_time_mins"]
                    first_stop = y
                    z = y
                    break
                else:
                    continue
    return(eta)