# List of integers and their sum

def sum_list_of_integers():
    """
    Prompts the user for a list of integers, then calculates and prints the sum.
    """
    integer_list = []
    while True:
        try:
            user_input = input("Enter an integer (or 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            integer = int(user_input)
            integer_list.append(integer)
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")

    if integer_list:  # Check if the list is not empty
        total = sum(integer_list)
        print("The sum of the integers in the list is:", total)
    else:
        print("No integers were entered.")

#sum_list_of_integers()  # Uncomment to run this part

# 2. Tuple of favorite books and printing them

def print_favorite_books():
    """
    Creates a tuple of favorite books and prints each on a new line.
    """
    favorite_books = ("The Lord of the Rings", "Pride and Prejudice", "1984", "The Hitchhiker's Guide to the Galaxy", "Dune")

    print("My favorite books:")
    for book in favorite_books:
        print(book)

#print_favorite_books() # Uncomment to run this part

# 3. Dictionary for person information

def create_person_dictionary():
    """
    Creates a dictionary of person information based on user input and prints it.
    """
    person_info = {}
    person_info['name'] = input("Enter the person's name: ")
    while True:
        try:
            person_info['age'] = int(input("Enter the person's age: "))
            break
        except ValueError:
            print("Invalid age.  Please enter an integer.")
    person_info['favorite_color'] = input("Enter the person's favorite color: ")

    print("Person Information:")
    print(person_info)

#create_person_dictionary() # Uncomment to run this part

# 4. Sets of integers and their intersection

def find_common_elements():
    """
    Creates two sets of integers from user input and finds their intersection.
    """

    def get_set_from_input(set_name):
        """Helper function to get a set of integers from user input."""
        integer_set = set()
        print(f"Enter integers for set {set_name} (or 'done' to finish):")
        while True:
            try:
                user_input = input()
                if user_input.lower() == 'done':
                    break
                integer = int(user_input)
                integer_set.add(integer)
            except ValueError:
                print("Invalid input. Please enter an integer or 'done'.")
        return integer_set

    set1 = get_set_from_input("A")
    set2 = get_set_from_input("B")

    common_elements = set1.intersection(set2)

    print("Common elements between the two sets:", common_elements)

#find_common_elements() # Uncomment to run this part

# 5. List comprehension for words with odd length

def find_odd_length_words():
    """
    Finds words with odd length from a list using list comprehension.
    """
    word_list = ["apple", "banana", "kiwi", "orange", "grape", "strawberry"]  # Example list. Can be user-input, too.
    #or you can ask the user for input here too:
    #word_list = input("Enter a list of words separated by space: ").split()


    odd_length_words = [word for word in word_list if len(word) % 2 != 0]

    print("Words with odd lengths:", odd_length_words)

#find_odd_length_words() # Uncomment to run this part