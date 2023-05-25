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
DIRECT_TEMPLATES = ['blogindex']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Libre+Baskerville:400,400i,700,700i%7CSource+Code+Pro:400,400i,600',
               '/static/m-light.css']
M_THEME_COLOR = '#297ac3'
#这个颜色没改记得自己改


PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.htmlsanity']

# 配置量
SITENAME = 'The_toast'
SITEURL = ''

M_BLOG_NAME = 'The_toast Blog'
M_BLOG_URL = 'blog/'

M_FAVICON = ('m.css/pelican-theme/static/images/20230502-myphoto.jpg')
M_BLOG_FAVICON = ('m.css/pelican-theme/static/images/20230502-myphoto.jpg')

# 顶部导航栏

M_SITE_LOGO_TEXT = 'The_toast Blog'

M_LINKS_NAVBAR1 = [('博客首页', 'category/shou-ye.html', 'hgxblog', []),
                   ('pelican教程', 'category/pelicanjiao-cheng.html', '1111', []),
                   ('markdown语法', 'category/markdownyu-fa.html', '2222', [])]

M_LINKS_NAVBAR2 = [('默认misc', 'category/misc.html', '[blog]', [
                        ('download', 'category/download.html', ''),
                        ('6666', '66666', '')]),
                   ('Contact', 'contact/', 'contact', [])]




# 页脚导航

M_FINE_PRINT = SITENAME + """. Powered by `Pelican <https://getpelican.com>`_
    and `m.css <https://mcss.mosra.cz>`_."""




M_BLOG_NAME = "The_toast Blog"
M_BLOG_URL = 'https://blog.your.brand/'
M_BLOG_DESCRIPTION = "Your Brand is the brand that provides all that\'s needed."

M_SOCIAL_TWITTER_SITE = '@your.brand'
M_SOCIAL_TWITTER_SITE_ID = 1234567890
M_SOCIAL_IMAGE = 'https://your.brand/static/site.png'
M_SOCIAL_BLOG_SUMMARY = "This is the brand you need"





USE_FOLDER_AS_CATEGORY = True

PORT = 8002


# 文字目录为文件夹
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'


# 文字标题为文件名
FILENAME_METADATA = '(?P<title>.*)'


# 未指定日期 DEFAULT_DATE 设置为 'fs' ，Pelican将依赖文件的“mtime”时间戳，并且类别可以由文件所在的目录确定
DEFAULT_DATE = 'fs'