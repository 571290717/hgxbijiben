AUTHOR = 'hgx'
SITENAME = 'hgx'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Libre+Baskerville:400,400i,700,700i%7CSource+Code+Pro:400,400i,600',
               '/static/m-light.css']
M_THEME_COLOR = '#cb4b16'

PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.htmlsanity']

# 配置量
SITENAME = 'the_toast'
SITEURL = ''

M_BLOG_NAME = 'Your the_toast Blog'
M_BLOG_URL = 'blog/'

M_FAVICON = ('favicon.ico', 'image/x-ico')
M_BLOG_FAVICON = ('favicon-blog.png', 'image/png')

# 顶部导航栏
M_SITE_LOGO_TEXT = 'Your Brand'

M_LINKS_NAVBAR1 = [('Features', 'features/', 'features', []),
                   ('Showcase', 'showcase/', 'showcase', []),
                   ('Download', 'download/', 'download', [])]

M_LINKS_NAVBAR2 = [('Blog', 'blog/', '[blog]', [
                        ('News', 'blog/news/', ''),
                        ('Archive', 'blog/archive/', '')]),
                   ('Contact', 'contact/', 'contact', [])]




# 页脚导航

M_FINE_PRINT = SITENAME + """. Powered by `Pelican <https://getpelican.com>`_
    and `m.css <https://mcss.mosra.cz>`_."""



M_BLOG_NAME = "Your Brand Blog"
M_BLOG_URL = 'https://blog.your.brand/'
M_BLOG_DESCRIPTION = "Your Brand is the brand that provides all that\'s needed."

M_SOCIAL_TWITTER_SITE = '@your.brand'
M_SOCIAL_TWITTER_SITE_ID = 1234567890
M_SOCIAL_IMAGE = 'https://your.brand/static/site.png'
M_SOCIAL_BLOG_SUMMARY = "This is the brand you need"


USE_FOLDER_AS_CATEGORY = True

PORT = 8002