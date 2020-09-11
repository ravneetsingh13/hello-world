import sys

if(len(sys.argv) < 2 ):
    print('Please enter the manadatory args to run the script')
else:
    print('The name of script is:', sys.argv[0])
    print('No. of arguments are:', len(sys.argv))
    print('The arguments are is:', str(sys.argv))