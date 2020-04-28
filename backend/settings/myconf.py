from datetime import timedelta
import os


THITD_PARTY_APPS = [
    'rest_framework',
    'djoser',
    # my-apps,
    # 'backend.account',
    'backend.api.order',
        'storages',
    'backend.api.product',
    'backend.api.comment'
]


# AUTH_USER_MODEL = 'account.User'

# SOCIAL AUTH
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Payment
# BrainTree settings
# We'll need this later to switch between the sandbox and live account
BRAINTREE_PRODUCTION = not os.getenv("DEVELOPMENT")
BRAINTREE_MERCHANT_ID = os.getenv("BRAINTREE_MERCHANT_ID")
BRAINTREE_PUBLIC_KEY = os.getenv("BRAINTREE_PUBLIC_KEY")
BRAINTREE_PRIVATE_KEY = os.getenv("BRAINTREE_PRIVATE_KEY")


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ['rest_framework_simplejwt.tokens.AccessToken'],
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# STORAGE

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = '3ce24guUPuAAAAAAAAAAGNSh-QAdtQzAoYw0mhRhZDaljMgZI_qvCL-5MWlEmTGS'