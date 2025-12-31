class Todo:
    """
    Represents a single todo item with an ID, title, description, and completion status.
    """
    def __init__(self, todo_id, title, description=""):
        self.id = todo_id
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "\u2713" if self.completed else "\u25cb"
        return f"[{status}] {self.id}: {self.title} - {self.description}"


class TodoManager:
    """
    Manages a collection of Todo items in memory.
    Provides methods to add, view, update, delete, and mark todos as complete.
    """
    def __init__(self):
        self.todos = []
        self.next_id = 1

    def add_todo(self, title, description=""):
        """
        Adds a new todo to the list with a unique ID.
        """
        todo = Todo(self.next_id, title, description)
        self.todos.append(todo)
        self.next_id += 1
        print(f"Added todo: {title}")

    def view_todos(self):
        """
        Displays all todos in the list with their current status.
        """
        if not self.todos:
            print("No todos available.")
            return

        print("\\nYour Todo List:")
        for todo in self.todos:
            print(todo)
        print()

    def update_todo(self, todo_id, new_title=None, new_description=None):
        """
        Updates a todo's title and/or description by its ID.
        """
        todo = self.find_todo_by_id(todo_id)
        if todo:
            if new_title:
                todo.title = new_title
            if new_description is not None:
                todo.description = new_description
            print(f"Updated todo ID {todo_id}")
        else:
            print(f"Todo with ID {todo_id} not found.")

    def delete_todo(self, todo_id):
        """
        Deletes a todo by its ID.
        """
        todo = self.find_todo_by_id(todo_id)
        if todo:
            self.todos.remove(todo)
            print(f"Deleted todo ID {todo_id}")
        else:
            print(f"Todo with ID {todo_id} not found.")

    def mark_complete(self, todo_id, completed=True):
        """
        Marks a todo as complete or incomplete by its ID.
        """
        todo = self.find_todo_by_id(todo_id)
        if todo:
            todo.completed = completed
            status = "complete" if completed else "incomplete"
            print(f"Marked todo ID {todo_id} as {status}")
        else:
            print(f"Todo with ID {todo_id} not found.")

    def find_todo_by_id(self, todo_id):
        """
        Helper method to find a todo by its ID.
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None


def display_menu():
    """
    Displays the menu options to the user.
    """
    print("\\nTodo App Menu:")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Mark Todo Complete")
    print("6. Mark Todo Incomplete")
    print("7. Exit")


def get_user_choice():
    """
    Gets the user's choice from the menu.
    """
    try:
        choice = int(input("Enter your choice (1-7): "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def main():
    """
    Main function to run the Todo console application.
    Handles user input and calls appropriate methods from TodoManager.
    """
    manager = TodoManager()

    print("Welcome to the Todo Console App!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            # Add a new todo
            title = input("Enter todo title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            description = input("Enter todo description (optional): ").strip()
            manager.add_todo(title, description)

        elif choice == 2:
            # View all todos
            manager.view_todos()

        elif choice == 3:
            # Update a todo
            try:
                todo_id = int(input("Enter todo ID to update: "))
                title = input("Enter new title (press Enter to skip): ").strip()
                description = input("Enter new description (press Enter to skip): ").strip()

                # Use None for values we don't want to update
                new_title = title if title else None
                new_description = description if description else None

                manager.update_todo(todo_id, new_title, new_description)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == 4:
            # Delete a todo
            try:
                todo_id = int(input("Enter todo ID to delete: "))
                manager.delete_todo(todo_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == 5:
            # Mark a todo as complete
            try:
                todo_id = int(input("Enter todo ID to mark complete: "))
                manager.mark_complete(todo_id, True)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == 6:
            # Mark a todo as incomplete
            try:
                todo_id = int(input("Enter todo ID to mark incomplete: "))
                manager.mark_complete(todo_id, False)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == 7:
            # Exit the application
            print("Thank you for using the Todo Console App!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")



# Run the application if this file is executed directly
if __name__ == "__main__":
    main()
