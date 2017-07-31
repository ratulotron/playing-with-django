from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


tokens = []

def generate_tokens():    
    for user in User.objects.all():
        token = Token.objects.create(user=user)
        tokens.append({
            user.username,
            token.key
        })    
        print(token.key)


def get_all_tokens():
    print(tokens)