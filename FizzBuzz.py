# to print Fizz/Buzz for integers upto n - problem statement here 
#http://c2.com/cgi/wiki?FizzBuzzTest

def FizzBuzz(n):
    for i in range(1,n+1):
        if i%15==0:
            print "FizzBizz"
        elif i%3==0:
            print "Fizz"
        elif i%5==0:
            print "Buzz"
        else :
            print i
#usage
FizzBuzz(10)
