from django.conf import settings


# @@@ TODO: recurse through available content apps and dynamically set this
POSITION_CHOICES = getattr(
	settings,
	'MENUS_POSITION_CHOICES',
	(
		('main-menu', 'Main Menu'),
		('footer-left-menu', 'Footer Menu'),
		('footer-social-menu', 'Footer Left - Social Icons'),
		('footer-right-menu', 'Footer Right (Logos)'),
	)
)
