# Function to find the missing number.
# To increase the optimality of the solution, this function uses the modified version 
# of binary search to find the missing number as the provided numbers are sorted.
def FindMissingNumber(numbers):
    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = left + (right - left)//2

        if numbers[mid] == mid+2 and numbers[mid-1] == mid:
            return mid+1

        elif numbers[mid] == mid+1:
            left = mid + 1

        else:
            right = mid - 1

    return left + 1

def main():
    n = int(input("Enter total numbers: "))
    string_of_digits = input("Enter string of digits: ")

    numbers = []
    left_index = 0
    right_index = 1
    addition = 1

    while len(numbers) < n-1:
        temp = int(string_of_digits[left_index:right_index])
        numbers.append(temp)

        left_index += addition
        right_index += addition

        # if the currently extracted value from the string is 9 than set the indexes to start extracting 2 digits from the string.
        if temp == 9:
            right_index += 1
            addition += 1

        # if the currently extracted value is 8 and the next digit is not 9 than set the indexes to start extracting 2 digits from the string.
        if temp == 8 and string_of_digits[left_index] == "1":
            right_index += 1
            addition += 1

        # if the currently extracted value from the string is 99 than set the indexes to start extracting 3 digits from the string.
        if temp == 99:
            right_index += 1
            addition += 1

        # if the currently extracted value is 98 and the next digit is not 99 than set the indexes to start extracting 3 digits from the string.
        if temp == 98 and string_of_digits[left_index] == "1":
            right_index += 1
            addition += 1

    print("Missing Number: " + str(FindMissingNumber(numbers)))

if __name__=="__main__":
    main()