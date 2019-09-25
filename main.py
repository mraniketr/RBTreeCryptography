from rbt import *
rbt = RedBlackTree()


print("CRYPTOGRAPHY USING RED BLACK TREES")
print("1. ENCRYPTION \n2. DECRYPTION\n3. EXIT")
print("Enter your choice ->")
choice=int(input())

if(choice==1):
    print("Enter a string to encrypt")
    str = input()

    l2 = list(range(1, len(str) + 1))
    for i in range(0, len(l2)):
        rbt.insert(l2[i])

    rbt.p_print()

    l3 = []
    print("Enter the number of red nodes")
    n = int(input())

    print("Enter red nodes")
    for i in range(n):
        l3.append(int(input()) - 1)

    # convert string to list

    l4 = [char for char in str]

    # Calculating the red keys
    l5 = []
    for i in range(len(l4)):
        if i in l3:
            l5.append(ord(l4[i]) + 1)
        else:
            l5.append(ord(l4[i]) + 2)

    # sort the list on the order

    l6 = []
    print("Input order")
    for i in range(0, len(l4)):
        l6.append(int(input()))

    l7 = [x for _, x in sorted(zip(l6, l5), key=lambda pair: pair[0])]

    # FINAL OUTPUT
    print("The encryption was successful \n")

    l8 = []
    for i in range(len(l4)):
        l8.append(chr(l7[i]))

    print(l8)
elif (choice==2):
    print("Enter the string to decrypt")
    str = input()

    l2 = list(range(1, len(str) + 1))
    for i in range(0, len(l2)):
        rbt.insert(l2[i])

    rbt.p_print()

    l3 = []
    print("Enter the number of red nodes")
    n = int(input())

    print("Enter the red nodes")
    for i in range(n):
        l3.append(int(input()) - 1)

    # convert string to list
    l4 = [char for char in str]

    # sort the list on the order
    l6 = []
    print("input order")
    for i in range(0, len(l4)):
        l6.append(int(input()))

    l7 = [x for _, x in sorted(zip(l6, l4), key=lambda pair: pair[0])]

    # Calculating the red keys
    l8 = []
    for i in range(len(l4)):
        if i in l3:
            l8.append(ord(l7[i]) - 1)
        else:
            l8.append(ord(l7[i]) - 2)

    # FINAL OUTPUT
    print("The decryption was successful \n")
    l9 = []
    for i in range(len(l4)):
        l9.append(chr(l8[i]))
    print(l9)
else:
    sys.exit(0)
