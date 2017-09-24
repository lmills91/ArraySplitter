_author_ = 'Laura Mills'
_project_ = 'TwigCodingChallenge'

# This is a short function to break one array up in to a 2d array.
# On running the code, the user is asked for the length of array then the number of blocks it should be broken in to.
# Output are the starting and ending arrays
# This is a simple function which can be run simply from the console in pycharm or other ide.
# In Pycharm, simply press shift + F10 to start the function.


def get_array_and_number(length_of_array, n):
    # first get length of array, then get the number of sub-arrays to split the main array in to.
    # keep asking until a positive, whole number is entered.

    if length_of_array and n > 0:
        # create array from the length given
        array = get_array(length_of_array)

        print("Starting array {}, in to {} blocks".format(array, n))

        # get max iterations
        num = get_num(length_of_array, n)
        maximum = get_max(num, n)

        # create output array by iteration.
        output_array = get_output(maximum, num, array)
        print("Output array {}".format(output_array))
        return True

    else:
        print("length and number of blocks must be > 0")
        return False


def get_array(length_of_array):
    array = []
    j = 0
    while j < length_of_array:
        array.append(j + 1)
        j += 1
    return array


def get_num(length_of_array, n):
    # get the number of items in each sub-array and append these to a blank one to give the result.
    remainder = length_of_array % n
    if not n == 1:
        num = round((length_of_array - remainder) / (n - 1))
    else:
        num = length_of_array

    return num


def get_max(num, n):
    maximum = (n - 1) * int(num)
    return maximum


def get_output(maximum, num, array):
    output_array = [array[i:i + int(num)] for i in range(0, maximum, int(num))]
    output_array.append(array[maximum:])
    return output_array


get_array_and_number(5, 3)

