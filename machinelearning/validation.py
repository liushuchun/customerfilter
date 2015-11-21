#!/usr/bin/python
# encoding:utf-8
# validation function


def phone_check(s):
    # the prefixion of the tel number
    phoneprefix = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '150',
                   '151', '152', '153', '156', '158', '159', '170', '183', '182', '185', '186', '188', '189']
    # check if the length of the number is legal
    s=str(s)
    if len(s) != 11:
        #print "The length of phonenum is 11."
        return 0
    else:
         # check if the number is all digital
        if s.isdigit():
             # che the prefixion 
            if s[:3] in phoneprefix:
                #print "The phone num is valid."
                return 1
            else:
                #print "The phone num is invalid."
                return 0
        else:
            #print "The phone num is not made up of digits."
            return 0
    return 0

if __name__ == "__main__":
    phonenum = raw_input("Input your phone num:")
    phone_check(phonenum)
