# introduction coding in the book


users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]


friendship_pairs = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

# represent firendships as an adjacency list
friendship_connections = {user["id"]: [] for user in users}

# add connections to adjacency list

for person1, person2 in friendship_pairs:
    friendship_connections[person1].append(person2)
    friendship_connections[person2].append(person1)

print(friendship_connections)

'''Getting average number of connections'''

def number_of_friends(user: dict) -> int:
    '''
        returns the number of friends a user has.

        user (dict): dictionary holding metadata of a
        user must contain an "id" key.

        returns (int): number of friends a user has.

        ex:
            >> usernmae = {"id": 1, "name": "bob"}
            >> number_of_friends(username)
                2
    '''

    user_id = user["id"]
    friends = friendship_connections[user_id]
    return len(friends)

# count all friendship connections
total_connections = sum([number_of_friends(user) for user in users])
print(f'total_connections: {total_connections}')

# divide by total users
connection_avg = total_connections / len(users)
print(f'connection average: {connection_avg}')

# find most connected users
users.sort(key=lambda x: number_of_friends(x), reverse=True)
print(f'users sorted by number of connections: \n\n {users}')

