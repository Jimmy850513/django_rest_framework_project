from rest_framework_simplejwt.authentication import JWTAuthentication


def get_user_id_and_username(author_headers):
    if author_headers:
        token = author_headers.split(" ")[1]
        token_pay_load_dict = JWTAuthentication().get_validated_token(token)
        user_id = token_pay_load_dict.get('user_profile_id')
        user_name = token_pay_load_dict.get('username')
    else:
        user_id = None
        user_name = None
    return user_id,user_name