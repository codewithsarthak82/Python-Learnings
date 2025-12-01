# we can use match case in different scenerios in python programming -
"""Here we can say that the use of this is following shown in the python
   and this links to find fifferent problems and associate a return value"""

def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(https_status(200))  # returns output as: OK
print(https_status(404))  # returns output as: Not Found
print(https_status(500))  # returns output as: Internal Server Error
print(https_status(5008)) # returns output as: Unknown Status