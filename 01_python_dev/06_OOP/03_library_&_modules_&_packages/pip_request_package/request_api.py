import requests

response = requests.get("http://www.bbc.co.uk/")

# if response.status_code == 200:
#    print("successful web is live and status code is " + str(response.status_code))
#
# elif response_status_code == 404:
#     print("unsuccessful web is not live and status code is " + str(response.status_code))
# else:
#     print(" OOPs... something went wrong..")

#
# # 2ND ITERATIONS - create a function that will deal with our status code
#
# def check_response_code():
#     if response.status_code == 200:
#         print("successful web is live and status code is " + str(response.status_code))
#
#     elif response.status_code == 404:
#         print("unsuccessful web is not live and status code is " + str(response.status_code))
#     else:
#         print(" OOPs... something went wrong..")
#
#print(check_response_code())
# change the print statement to return

# THIRD ITERATION
def check_status():
    if response:
        return "success"
    elif response:
        return "unsuccessfull"
    else:
        return "OOps someting went wrong.. please try again later"
print(check_status())

# requests goes one step further in simplifying this process for us.
# If you use a response_bcc instance in a conditional expression,
# It will evaluate to True if the status code was between 200 and 400, and False otherwise.
# Therefore, you can simplify the last example by rewriting the if statement as above: