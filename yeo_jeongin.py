from datetime import datetime
def todo_list(user_todo, mode=("new", "edit", "remove")): 
    if mode == "new": 
        new_date = input("Enter the date (yyyy-mm-dd): ")
        new_list = input("Enter the todo_list: ")
        user_todo[new_date] = new_list
        print("You are so hardworking! 🫵​ ​👍​", user_todo)
        
    elif mode == "edit": 
        edit_date = input("Enter the date (yyyy-mm-dd): ")
        for edit in user_todo:
            if edit == edit_date:
                new_list = input(f"{user_todo[edit]} --> : ")
                user_todo[edit] = new_list
                print("Your todo_list has been updated.", user_todo)
                break
        else: print("No entry found for that date.")

def log_in():
    users = {
        "sion": {"birth": "2003-01-01", "id": "si", "pw": "1234", "role": "viewer", 
                 "todo": {"2025-08-25": "study", "2025-08-26": "enum"}},
        "tokuno": {"birth": "2004-01-01", "id": "to", "pw": "5678", "role": "editor", 
                   "todo": {"2025-08-25": "while", "2025-08-26": "case"}},
        "sakuya": {"birth": "2007-01-01", "id": "sa", "pw": "9101", "role": "admin", 
                   "todo": {"2025-08-25": "def", "2025-08-26": "match"}}}

    name = input("Enter your name: ")
    if name in users : 
        password = input("Enter your password: ")
        if users[name]["pw"] == password:
            print(f"succeed. your profile: {users[name]}")
            want = input("Do you want to add_new/edit your todo_list? (new/edit/no): ")
            print("") if want == "no" else todo_list(users[name]["todo"], want) and print(users[name]["todo"])
            match users[name]["role"]:
                case "viewer": 
                    print(users[name])
                    if input(f"Do you want to remove your ID? (y/n): ") == "y": 
                        users.pop(name) and print("removed.")
                case "editor": 
                    print(users) 
                    if input(f"Do you want to remove your ID? (y/n): ") == "y": 
                        users.pop(name) and print("removed.", users.keys())
                case "admin": 
                    print(users) 
                    if input(f"Do you want to remove USER? (y/n): ") == "y": 
                        users.pop(input(f"Enter the name to remove: ")) and print("removed.", users.keys())
        else: print("Wrong password.")

    else:
        print("failed. Do you want to join us?")
        if input("y/n: ") == "y":
            while (name := input("Enter your name: ")) in users: print("already exist")
            password = input("Enter your password: ")
            while True:
                try: birthday = datetime.strptime(input("Enter your birthday (yyyy-mm-dd): "), "%Y-%m-%d"); break
                except ValueError: print("format!!!!!")
            id = input("Enter your id: ")
            while (role := input("Enter your role(viewer/editor/admin): ")) not in ["viewer", "editor", "admin"]: print("format!!!!!")
            users[name] = {"birth": birthday, "id": id, "pw": password, "role": role}
            print("User added successfully.")
            match users[name]["role"]:
                case "viewer": print(users[name])
                case "editor": print(users)
                case "admin": print(users)
log_in()