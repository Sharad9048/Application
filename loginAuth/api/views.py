from rest_framework.response import Response
import re

def signIn(request):
    """
    @input : Takes request
    @output : Return authentication token
    """
    uid = request.data['user_id_input']
    password = request.data['password']
    userNamePattern = re.compile('\w+')
    emailPattern = re.compile('\w+@[A-Za-z]+.[a-z]+')
    if emailPattern.match(uid):
        pass
    elif userNamePattern.match(uid):
        pass

    pass