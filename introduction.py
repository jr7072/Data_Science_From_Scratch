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

# start of friend suggestion

def friend_of_friends_bad(user: dict) -> list:
    '''
        returns the user id of the friends of user's friends

        user (dict): Hash map with user metadata must include an id
        field

        returns (list): list of user id's that are friends of the user's friends
    '''

    return [
        user_id for friend in friendship_connections[user["id"]]
        for user_id  in friendship_connections[friend]
    ]

print(friend_of_friends_bad(users[5]))

from collections import Counter

def friends_of_friends(user: dict) -> list:
    '''
        Takes in user metadata and provides freinds of friends exclusive of self 
        and friends

        user (dict): hash map that contains user metadata. Must contain an
        id entry

        returns (list): list of friends of friends excluding user and the user's
        friends
    '''
    user_id = user["id"]

    mutual_friends = list()
    user_friends = friendship_connections[user_id]

    for friend in user_friends:
        for mutual_id in friendship_connections[friend]:

            if (mutual_id == user_id or
                    mutual_id in user_friends):
                continue

            mutual_friends.append(mutual_id)

    mutual_counts = Counter(mutual_friends)

    return mutual_counts

print(f"true friend of friends: {friends_of_friends(users[2])}")

# get user interests from the book data science from scratch

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"),
    (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"),
    (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"),
    (8, "artificial intelligence"),
    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientist_who_like(target_interest: str) -> list:
    '''
        Gets all users who have the target interest

        target_indetest (str): The target interest to search for

        return (list): list of user ids that have the target interest
    '''

    users_with_interest = list()

    for user, user_interest in interests:

        if user_interest != target_interest:
            continue

        users_with_interest.append(user)
    
    return users_with_interest

from collections import defaultdict

user_ids_by_interest = defaultdict(list)

for user_id, user_interest in interests:

    user_ids_by_interest[user_interest].append(user_id)

print(user_ids_by_interest)

interest_by_user_id = defaultdict(list)

for user_id, user_interest in interests:
    interest_by_user_id[user_id].append(user_interest)

print(interest_by_user_id)

def most_common_interest_with(user: dict) -> dict:
    '''
        returns a dictionary of users that has common interest
        with the addition of how many interest in common the users have

        user (dict): user metadata with id field

        return (dict): user hash map of users mapped to number of interest
        they have in common with the user
    '''

    user_id = user["id"]
    similar_users = list()

    for interest in interest_by_user_id[user_id]:

        for similar_user in user_ids_by_interest[interest]:

            if similar_user == user_id:
                continue

            similar_users.append(similar_user)
    
    interest_count = Counter(similar_users)

    return interest_count

print(most_common_interest_with(users[5]))

# salaries and experience

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

tenure_map = defaultdict(list)

for salary, tenure in salaries_and_tenures:

    tenure_map[tenure].append(salary)

print(tenure_map)

# bucket tenures
def bucket_tenures(tenure: float) -> str:
    '''
        returns string representation of
        tenure

        tenure (int): The tenure amount in years

        returns (str):
        String representation of tenure. ex "less than 2 years"
    '''

    if tenure < 2:
        return "Less than 2"
    if tenure < 5:
        return "Between 2 and 5 Years"
    
    return "More than 5 years"

bucket_tenure_map = defaultdict(list)

for salary, tenure in salaries_and_tenures:

    bucket = bucket_tenures(tenure)
    bucket_tenure_map[bucket].append(salary)

for bucket, salaries in bucket_tenure_map.items():

    mean = sum(salaries) / len(salaries)
    print(f'Tenure: {bucket} Average Salary: {mean}')


    
