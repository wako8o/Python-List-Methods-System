def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):
    value = input("Enter a value to append:-> ")
    lst.append(value)
    print("list after append: ", lst)


def handle_extend(lst):
    value = input("Enter a value to extend:-> ")
    lst.extend(value)
    print("List after extend: ", lst)


def handle_insert(lst):
    value = input("Enter a value to insert:-> ")
    index = int(input("Index to insert: -> "))
    lst.insert(index, value)
    print("List after insert: ", lst)


def handle_remove(lst):
    value = input("Enter a value to remove:-> ")
    try:
        lst.remove(value)
        print("List after remove: ", lst)
    except ValueError:
        print("Value not found in the list:")


def handle_pop(lst):
    index = input("Enter a value to pop:-> ")
    if index:
        try:
            index = int(index)
            element = lst.pop(index)
            print(element)
            print("List after pop: ", lst)
        except IndexError:
            print("Index out of range.")
    else:
        lst.pop()
        print("List after pop: ", lst)


def handle_clear(lst):
    lst.clear()
    print("list after cler; ", lst)


def handle_index(lst):
    value = input("Enter a value to index:-> ")
    try:
        lst = value.index(value)
        print("Index of value:-> ", lst)
    except ValueError:
        print("Value not found in the list.")


def handle_count(lst):
    value = input("Enter a value to count:->")
    lst.count(value)
    print("List after count: ", lst)


def handle_sort(lst):
    lst.sort()
    print("List after sort: .", lst)


def handle_reverse(lst):
    lst.reverse()
    print("List after reverse: ", lst)


def handle_copy(lst):
    lst.copy()
    print("List after copy: ", lst)


def main():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
