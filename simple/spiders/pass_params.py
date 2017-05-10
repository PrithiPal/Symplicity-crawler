import getopt
import os
import sys



#start accepting arguments




def printError() :
    print("Usage : connect_spider [-u|—username=] <connectUsername> [-p|—pasword=] <connectPassword>")
    sys.exit(1)

def process() :
    user = ''
    passw = ''
    opt = ''
    options, args = getopt.getopt(sys.argv[1:],'u:p:',['username=','password='])

    first_condition = opt in ('-u','--username')
    second_condition = opt in ('-p','--password')

    try :
        for opt,arg in options :
            if opt in ('-u','--username') :
                user = str(arg)
            elif opt in ('-p','--password') :
                passw = str(arg)
            elif not opts:
                printError()

    except getopt.GetoptError as e :
        print(str(e))
        printError()

    if ((user is not '') and (passw is not '')) :
        print("USER: ",str(user))


        next_command = 'scrapy crawl makdi -a username=' + str(user) + ' -a password=' + str(passw) 
        os.system(next_command) # pass the command to the connect_spider.py scrapy file.
    else :
        printError()

#main method
if __name__ == "__main__" :
    process()
