# Initialize lists and dictionaries
messages = []
users = set()
user_message_count = {}
user_word_count = {}
user_messages = {}
deleted_messages = 0

# Input section
num = int(input("Enter the number of messages: "))
i = 0
while i < num:
    msg = input()
    messages.append(msg)
    if msg == "This message was deleted":
        deleted_messages += 1
        i += 1
        continue
    if ":" in msg:
        name, text = msg.split(":", 1)
        name = name.strip()
        text = text.strip()
        users.add(name)
        user_message_count[name] = user_message_count.get(name, 0) + 1
        word_list = text.lower().split()
        user_word_count[name] = user_word_count.get(name, 0) + len(word_list)
        if name not in user_messages:
            user_messages[name] = []
        user_messages[name].append(msg)
    i += 1

# Menu
while True:
    print("\nChoose analysis option:")
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("13. Identify user with longest average message length")
    print("14. Count how many messages mention a specific user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract all questions asked in the chat")
    print("18. Calculate reply ratio between two users")
    print("19. Check for deleted messages")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Total messages:", len(messages))
    elif choice == '2':
        print("Unique users in the chat:", users)
    elif choice == '3':
        total_words = sum(user_word_count.values())
        print("Total words in the chat:", total_words)
    elif choice == '4':
        avg = sum(user_word_count.values()) / len(messages)
        print("Average words per message:", round(avg, 2))
    elif choice == '5':
        longest = max(messages, key=len)
        print("Longest message:", longest)
    elif choice == '6':
        most_active = max(user_message_count, key=user_message_count.get)
        print(f"Most active user: {most_active} ({user_message_count[most_active]} messages)")
    elif choice == '7':
        user = input("Input: ")
        print(f"Messages sent by {user}: {user_message_count.get(user, 0)}")
    elif choice == '8':
        user = input("Input: ")
        if user in user_messages:
            from collections import Counter
            words = []
            for m in user_messages[user]:
                _, text = m.split(":", 1)
                words.extend(text.lower().split())
            most_common = Counter(words).most_common(1)
            if most_common:
                print(f'Most frequent word used by {user}: "{most_common[0][0]}"')
            else:
                print("No words found.")
        else:
            print("User not found.")
    elif choice == '9':
        user = input("Input: ")
        if user in user_messages:
            print("First message by", user + ":", user_messages[user][0])
            print("Last message by", user + ":", user_messages[user][-1])
        else:
            print("User not found.")
    elif choice == '10':
        user = input("Input: ")
        if user in users:
            print(f"User '{user}' found in the chat.")
        else:
            print(f"User '{user}' not found in the chat.")
    elif choice == '11':
        from collections import Counter
        all_words = []
        for msg in messages:
            if ":" in msg:
                _, text = msg.split(":", 1)
                all_words.extend(text.lower().split())
        repeated = {word for word, count in Counter(all_words).items() if count > 1}
        print("Common repeated words:", repeated)
    elif choice == '13':
        avg_lengths = {user: user_word_count[user]/user_message_count[user] for user in users}
        max_user = max(avg_lengths, key=avg_lengths.get)
        print(f"User with longest average message: {max_user} (avg {round(avg_lengths[max_user], 2)} words)")
    elif choice == '14':
        keyword = input("Input: ").lower()
        count = 0
        for msg in messages:
            if keyword in msg.lower().split():
                count += 1
        print(f"Messages mentioning '{keyword}': {count}")
    elif choice == '15':
        unique_msgs = set(messages)
        print("Unique messages count:", len(unique_msgs))
        for m in sorted(unique_msgs):
            print(m)
    elif choice == '16':
        for m in sorted(messages):
            print(m)
    elif choice == '17':
        questions = [m for m in messages if '?' in m]
        for q in questions:
            print(q)
    elif choice == '18':
        user1 = input("Input first user: ")
        user2 = input("Input second user: ")
        replies = 0
        for i in range(1, len(messages)):
            if ":" not in messages[i-1] or ":" not in messages[i]:
                continue
            u1, _ = messages[i-1].split(":", 1)
            u2, _ = messages[i].split(":", 1)
            if u1.strip() == user1 and u2.strip() == user2:
                replies += 1
        print(f"Reply ratio from {user2} to {user1}: {replies} replies")
    elif choice == '19':
        print("Deleted messages found:", deleted_messages)
    elif choice == '0':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
