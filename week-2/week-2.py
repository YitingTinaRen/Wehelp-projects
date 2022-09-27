## Print sum of a specific range
def calculate(min, max,step):
    if max<min:
        print("Error! %d > %d" %(max,min))
        return
    answer=0
    for i in range(min, max+1, step) :
        answer+=i
        ##print(i)
        
    print(answer)
    return 

print("Requirement 1 results:")
calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

## print average number with a confinement
def avg(data):
    sum=0
    employeeNumber=0
    for employeeData in data['employees']:
        if not employeeData['manager']:
            sum+=employeeData['salary']
            employeeNumber+=1;
    average=sum/employeeNumber
    print(average)
    return

print("Requirement 2 results:")
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]})

# currying format
def func(a):
    def func_inner(b,c):
        return print(a+(b*c))
    return func_inner

print("Requirement 3 results:")
func(2)(3,4)
func(5)(1,-5)
func(-3)(2,9)

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    max_1=nums.pop(nums.index(max(nums)))
    min_1=nums.pop(nums.index(min(nums)))
    if len(nums)==0:
        return print(max_1*min_1)
    elif max_1*max(nums)>=min_1*min(nums):
        return print(max_1*max(nums))
    else:
        return print(min_1*min(nums))

print("Requirement 4 results:")
maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([10, -20, 0, -3]) # 得到 60 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([5,-1, -2, 0]) # 得到 2 
maxProduct([-5, -2]) # 得到 10

def twoSum(nums, target):
    # your code here
    for i in nums:
        remainder = target-i
        if remainder <0:
            continue
        elif remainder in nums:
            return [nums.index(i), nums.index(remainder)]

print("Requirement 5 results:")
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 

def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊 maxZeros([0, 1, 0, 0]) # 得到 2
    counter=0
    maxlen=0
    start=0
    if start== len(nums): return 0 # empty list
    for i in nums:
        if i==1:
            if counter>=maxlen:
                maxlen=counter
            counter=0
        else:
            counter+=1
    if counter>=maxlen:
        maxlen=counter
    print(maxlen)
print("Requirement 6 results:")
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3