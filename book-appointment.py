def validate_appointment(slot, userid):

    if slot <= 0:
        return False

    if userid <= 0:
        return False

    return userid < slot


# Test cases
assert validate_appointment(10, 5) == True
assert validate_appointment(10, 15) == False
assert validate_appointment(10, 0) == False
assert validate_appointment(10, -2) == False
assert validate_appointment(0, 5) == False