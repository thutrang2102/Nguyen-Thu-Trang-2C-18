
#declare dictionary
alpha = {"ABC": '2', "DEF": '3', "GHI": '4', "JKL": '5', "MNO": '6', "PQR": '7', "STUV": '8', "WXYZ": '9'}

  # create method for translating
def Trans(phoneNum):
     # initialize num variable
     num = ""
     #loop over the input
     for i in phoneNum:
        #input = number || = "-" --> append it to result
        if i.isdigit() or i=='-':
            num += i
            continue

        # check alphabet in dictionary & append to result
        for key, value in alpha.items():
            #i: uppercase
            if i.upper() in key:
                #result = its value
                num += alpha[key]
                break
     return num


   #input from user
phoneNum = input("Enter telephone number in the format XXX-XXX-XXXX: ")
print(Trans(phoneNum))

