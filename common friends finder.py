def get_friends():
    friends = {}
    while True:
        user = input("Enter user's name (or 'done' to finish): ").strip().lower()
        if user == 'done':
            break
        friend_list = input(f"Enter {user}'s friends (comma-separated): ").strip()
        friends[user] = set(friend.strip() for friend in friend_list.split(','))
    return friends

def find_common_and_all_friends(friends):
    if not friends:
        return set(), set()
    all_friends = set()
    common_friends = set.intersection(*friends.values()) if len(friends) > 1 else set()
    for friend_set in friends.values():
        all_friends.update(friend_set)
    return common_friends, all_friends

def find_mutual_friends(friends, user1, user2):
    if user1 in friends and user2 in friends:
        return friends[user1].intersection(friends[user2])
    return set()

def main():
    friends = get_friends()
    if len(friends) < 2:
        print("Not enough users to find common friends.")
        return

    common_friends, all_friends = find_common_and_all_friends(friends)
    print("\nCommon Friends:", common_friends if common_friends else "None")
    print("All Friends:", all_friends if all_friends else "None")

    while True:
        user1 = input("\nFirst user's name (or 'exit' to quit): ").strip().lower()
        if user1 == 'exit':
            break
        user2 = input("Second user's name: ").strip().lower()
        if user1 in friends and user2 in friends:
            mutual_friends = find_mutual_friends(friends, user1, user2)
            print(f"Mutual friends between {user1} and {user2}: {mutual_friends if mutual_friends else 'None'}")
        else:
            print("One or both users not found.")

if __name__ == "__main__":
    main()
