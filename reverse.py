def int_reverse ():
    int_num = int(input('Enter a number: ')) #prompts for input
    reverse = int(str(int_num)[::-1]) #goes through the number entered backwards, outputs every value in that order
    print (reverse) #prints number
int_reverse() #calls function