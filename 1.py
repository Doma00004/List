def list():

    input_str = input("Enter integer values separated by spaces: ")
    values = input_str.split()

    try:
        a = [int(x) for x in values]
    except ValueError:
        print("Please enter only integer values separated by spaces.")
        list()

    print(a)
    n=len(a)

    t=int(input('Enter target number: '))

    result="pair ({},{}) found"
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] + a[j] == t:
                count=count+1
                print(result.format(a[i],a[j]))
    if count==0:
        print('pair not found')

list()