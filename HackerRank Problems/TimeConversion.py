#!/bin/python3

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    try:
        newString = s.split(":")
        if ((newString[2][2:4]).lower() == "pm"):
            if (newString[0] == '12'):
                newAnswer = "12" + ":" + str(newString[1]) + ":" + str(newString[2][0:2])
            else:
                newAnswer = str(12 + int(newString[0])) + ":" + str(newString[1]) + ":" + str(newString[2][0:2])
            return newAnswer
        elif ((newString[2][2:4]).lower() == "am"):
            if (newString[0] == '12'):
                newAnswer = "00" + ":" + str(newString[1]) + ":" + str(newString[2][0:2])
            else:
                newAnswer = str(newString[0]) + ":" + str(newString[1]) + ":" + str(newString[2][0:2])
            return newAnswer
        else:
            return "wrong format"
    except:
        pass
    # Write your code here.
    #


print(timeConversion("12:05:45PM"))
'''if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()'''
