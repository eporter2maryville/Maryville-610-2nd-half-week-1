# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 1.1 Reinforcement and Punishment

#multiple calculator
def multiple(x,y):
    x=x
    y=y
    
    if y % x == 0:
        print ( '{0} is a multiple of {1}!'.format(y,x) )
    else:
        print ('{0} is NOT a multiple of {1}!'.format(y,x) )

def main():
    x = int(input("Please give me a factor: "))
    y = int(input("Please give me a number to check for multiples: "))
    multiple(x,y)
    
main()
    

#Spam Statement repeater
for sentance in range (100):
    print('I will never spam my friends again.')
    