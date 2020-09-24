# Collaborators (including web sites where you got help: https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
#

def avg(user_list):
    length = len(user_list)
    total = sum(user_list)
    average = total/length
    return average


if __name__ == '__main__':
    # test your fucntion with this print statement before writing the input loop
    #print(avg([3, 4, 5]))    # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
 try:
    user_list = []

    while True:
        user_list.append(int(input("Enter a number (enter a letter to stop): ")))
 except:
    print (avg(user_list))
    # Write a loop to allow the user to input the values to be averaged
