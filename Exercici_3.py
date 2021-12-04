def main():
    user = {'username': '', 'department': '', 'classroom': ''}
    user['username'] = str(input("Enter your username: "))
    user['department'] = str(input("Enter your department: "))
    user['classroom'] = int(input("Enter your classroom: "))
    while user["classroom"] < 1 or user["classroom"] > 15:
        del user["classroom"]
        user['classroom'] = int(
            input("Error! Your classroom must be between 1 and 15.\nPlease re-enter your classroom: "))
    print("User data is:")
    for x in user:
        print(user[x])


if __name__ == '__main__':
    main()
