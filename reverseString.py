

def input_str(input_list):
    left = 0
    right = len(input_list)-1
    while left<right:
        hold = input_list[left]
        input_list[left] = input_list[right]
        input_list[right] = hold
        left+=1
        right-=1

    return input_list



print(input_str(["e","v","o","l"]))

