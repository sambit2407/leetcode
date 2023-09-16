#input : arr = [0,1,0,3,12]
#output : arr = [1,3,12,0,0]

arr = [7,1,0,3,12]

def movezeros(arr:list[int]):
    prev_idx = 0
    for i in range(len(arr)):
        if arr[i]!=0:
          hold = arr[prev_idx]
          arr[prev_idx] = arr[i]
          arr[i] = hold

          prev_idx+=1


print(arr)
movezeros(arr)
print(arr)



