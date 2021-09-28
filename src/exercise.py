def main():
    #write your code below this line
    nums = []
    while True:
        num = int(input())
        if (num == 9999):
            break
        else:
            nums.append(num)
    smallest = nums[0]
    for i in range(len(nums)):
        if (nums[i] < smallest):
            smallest = nums[i]
    print("Smallest number: " + str(smallest))
    for j in range(len(nums)):
        if (nums[j] == smallest):
            print("Found at index: " + str(j))

if __name__ == '__main__':
    main()
