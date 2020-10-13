from request_api import *


print(response.status_code)
print(response.headers)

if response.status_code == 200:
   print("successful web is live and status code is " + str(response.status_code))

elif response_status_code == 404:
    print("unsuccessful web is not live and status code is " + str(response.status_code))
else:
    print(" OOPs... something went wrong..")