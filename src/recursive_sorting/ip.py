new_arr = []
def ms(arr,new_arr):
    if len(arr) <=1:
        new_arr.append(arr)
    elif len(arr) ==2:
        x = arr[0]
        y = arr[1]
        if x>y:
            arr[0]=y
            arr[1] =x
            new_arr.append(arr)
        else:
            new_arr.append(arr)
    else:
        b,c  = arr[0:len(arr)//2],arr[len(arr)//2:]
        return ms(b,new_arr) , ms(c,new_arr)
def s(n):
    final_a = []
    for i in range(0,len(n),2):
        try:    
            new_a = []
            while (len(n[i])>0) and (len(n[i+1])>0):
                if n[i][0] < n[i+1][0]:
                    z = n[i][0]
                    new_a.append(z)
                    del n[i][0]
                else:
                    z = n[i+1][0]
                    new_a.append( z )
                    del n[i+1][0]
            final_a.append( new_a +n[i]+n[i+1] )
        except:
            #catches and appends the last element if array is odd length
            final_a.append(n[i])
            return s(final_a)
    if len(final_a)>1:
        return s(final_a)
    else:
        return final_a[0]

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    new_arr = []
    ms(arr,new_arr)
    return s(new_arr)


