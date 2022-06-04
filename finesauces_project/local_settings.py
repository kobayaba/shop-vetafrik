#SECRET_KEY = ''
SECRET_KEY = 'django-insecure-l+hw6!*8)=%^j+a%-qpw6o2jn=8zmbngoka=&bgp)t8=%nd$(c'


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
	'default':{
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'finesauces',
		'USER': 'finesaucesadmin',
		'PASSWORD': '09212607Fd',
		'HOST': 'localhost',
		'PORT': 5432,
	}
}

CART_ID = 'cart'