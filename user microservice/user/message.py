

import json

from user.models import User



def process_user_message(key, value):
    try:
        data = json.loads(value)
        User.objects.create(username=data['username'], password=data['password'])
        print('User Created')
    except Exception as e:
        print(f'Error creating User: {e}')