from django.conf import settings


URL_NAMES = getattr(
    settings,
    'MENUS_URL_NAMES',
    (
        ('index', 'Home page'),
        ('why_visit', 'Why Visit UNSW?'),
        ('organising_visit', 'Organising Visit'),
        ('campus', 'Our Campus'),
        ('sydney', 'Sydney'),
        ('contact', 'Contact Us'),
        ('search', 'Search')
    )
)
