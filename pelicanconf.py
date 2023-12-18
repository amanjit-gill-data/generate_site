from datetime import date 

AUTHOR = 'Amanjit Gill'
SITENAME = 'Amanjit Gill'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'EN'

# Don't generate any feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("github", "https://github.com/amanjit-gill-data"),
)

DEFAULT_PAGINATION = 5

### ADDED BY AMANJIT ### 

OUTPUT_PATH = "../amanjit-gill-data.github.io/"

# Overwrite entire output directory, but retain .git data 
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

DEFAULT_DATE = "fs"

THEME = "C:\\Users\\amanj\\miniconda3\\envs\\blog\\Lib\\site-packages\\pelican\\themes\\Flex"

# Flex defines main menu as small links across top of page 
MAIN_MENU = False 

# Stops display of 'about' page, so I can put it last in the links 
DISPLAY_PAGES_ON_MENU = False

# Flex uses this for sidebar links 
# must have comma after last tuple
LINKS = (
    ("home", "/"),
    ("analysis", "/category/analysis.html"),
    ("mathematics", "/category/mathematics.html"),
    ("programming", "/category/programming.html"),
    ("computing", "/category/computing.html"),
    ("opinion", "/category/opinion.html"),
    ("about", "/pages/about.html"),
)

# Pelican will copy these directly into the generated output, inc parent dirs
STATIC_PATHS = ["extra/CNAME", "extra/custom.css", "extra/headshot.png"]

# redirect static files to their proper locations in generated output
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/headshot.png": {"path": "static/headshot.png"}
}

# where to put generated articles 
ARTICLE_URL = ARTICLE_SAVE_AS = "category/{category}/posts/{slug}.html"

# Don't need Authors list, Author page, Tags list and Tag page 
# also don't need Categories list, as I've put category links in sidebar 
CATEGORIES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""

# where to put additional pages 
# url should be index/2, analysis/2, etc 
# save location should be index/2.html, analysis/2.html, etc 
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{name}/{number}', '{name}/{number}.html'),
)

# date as it appears on posts 
DEFAULT_DATE_FORMAT = "%a %d %b %Y"

### FLEX SETTINGS ### 

CUSTOM_CSS = "static/custom.css"

SITETITLE = "Amanjit Gill"

SITELOGO = SITEURL + "/static/headshot.png"

# Links go to top of page, not to title
DISABLE_URL_HASH = True

COPYRIGHT_NAME = "Amanjit Gill"

def get_copyright_years():

    initial_year = 2023 
    current_year = date.today().year 

    if initial_year == current_year:
        return f"{initial_year}"
    else:
        return f"{initial_year}-{current_year}"

COPYRIGHT_YEAR = get_copyright_years()

