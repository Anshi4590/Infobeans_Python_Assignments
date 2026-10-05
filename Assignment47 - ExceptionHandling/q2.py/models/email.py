class DotException(Exception):
    pass

class AtTheRateException(Exception):
    pass

class DomainException(Exception):
    pass



def validateemail(email):

    if email.count("@")!=1:

        raise AtTheRateException("Invalid @ usage")


    if email.count(".")!=1:

        raise DotException("Invalid Dot usage")
 
    if domain not in ["com","in","net","biz"]:

        raise DomainException("Invalid Domain")
