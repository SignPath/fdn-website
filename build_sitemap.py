import sys
import os
import glob
from datetime import datetime, timedelta
import subprocess
import yaml
from yaml.loader import SafeLoader

verbose: bool = False

# create sitemap.xml 
#
# list all *.md and *.html files using
# * their relative file path
# * unless they specify a 'permaurl' in front matter
# * special handling for project pages 
# and include their last modified date 
# * if specified: 'last_modified_at' from front matter/html comment
# * if file or 'layout' (from front matter) have been modified vs. git repo: current time + x (see 'publish_date' variable) 
# * otherwise: latest of
#   * file commit date
#   * date for 'layout' file from front matter (this algorithm applied recursively)
#   * latest date for yaml listed in front matter 'datasource' (comma-separated; e.g. editions = _data/editions.yml)
#   * 'date' from front matter
#   * 'last_modified_at' dates in global include files (see 'global_includes' variable)
#
# Syntax for HTML file comments:
#   <!-- last_modified_at: ... --> (in first line)

# The page will be updated after committing and pushing main branch. When generating the sitemap, we can only assume when this will occur
publish_date = datetime.now() + timedelta (minutes=1)

global_includes = ['_includes/header.html', '_includes/footer.html']

includes_date: datetime
layout_dates: dict[str, datetime] = {}

# quick&dirty hack. import dateutil didn't work
def parse_datetime (str: str, file, key) -> datetime:
    str = str.split('+')[0].strip() # strip time zone info + whitespace
    try: return datetime.strptime(str, '%Y-%m-%d %H:%M:%S');
    except:
        try: return datetime.strptime(str, '%Y-%m-%d %H:%M');
        except:
            try: return datetime.strptime(str, '%Y-%m-%d');
            except: print (f'{file}: could not parse {key}: "{str}"', file=sys.stderr)

def git_is_modified (filename):
    status_output: str = subprocess.check_output (f'git status "{filename}"', shell=True, encoding='ascii')
    return '\tmodified:' in status_output

def git_get_commitdate (filename) -> datetime:
    strval = subprocess.check_output (f'git log -1 --pretty="format:%ci" "{filename}"', shell=True, encoding='ascii')
    return parse_datetime (strval, filename, 'git log commit date')

def get_html_file_date (filename) -> datetime:
    with open (filename, 'r', encoding='utf-8') as f:
        line = f.readline()
        date = get_comment_date (filename, line) if line else None
        if date: 
            print (f'{filename}: {date}')
        return date

def get_comment_date (filename, line: str) -> datetime:
    line = line.strip()
    if line.startswith('<!--') and line.endswith('-->'):
        comment = line[4:-3].strip()
        key = 'last_modified_at:'
        if comment.startswith(key):
            value = comment[len(key):].strip()
            return parse_datetime (value, filename, key[:-1]) if any(value) else None

def get_file_date (filename) -> datetime:
    if git_is_modified (filename):
        return publish_date
    else:
        return git_get_commitdate (filename)

def get_page_data (filename) -> tuple[datetime, str]:
    fm_lastmod: datetime = None
    fm_date: datetime = None
    fm_layout: str = None
    fm_datasource: str = None
    fm_permalink: str = None
    modified: bool = git_is_modified(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
        if line != '---\n': 
            fm_lastmod = get_comment_date (filename, line)
        else:
            while line:
                line = f.readline()
                if line == '---\n': 
                    break;
                colpos = line.find(":")
                if colpos == -1:
                    continue
                key = line[:colpos]
                value = line[colpos+1:].strip()
                match key:
                    case 'last_modified_at': 
                        fm_lastmod = parse_datetime(value, filename, key);
                    case 'date': 
                        fm_date = parse_datetime(value, filename, key);
                    case 'layout':
                        fm_layout = f'_layouts/{value}.html'
                    case 'datasource':
                        fm_datasource = value
                    case 'permalink':
                        fm_permalink = value[1:] if value.startswith('/') else value
                    case 'redirect_to':
                        return None, None # skip file
                    case 'sitemap':
                        if value == 'false': return None, None # skip file
    
    if fm_lastmod: 
        date = fm_lastmod # if explicitly specified, take it
        if verbose: print(f'{filename}: fm_lastmod={fm_lastmod}')
    elif modified:
        date = publish_date
        if verbose: print(f'{filename}: publish_date={publish_date}')
    else:
        commit_date: datetime = git_get_commitdate (filename)

        layout_date: datetime = None
        if fm_layout:
            if not os.path.isfile(fm_layout): 
                print(f'{filename}: layout {fm_layout} not found', file=sys.stderr)
            else:
                layout_date = layout_dates.get(fm_layout)
                if not layout_date:
                    layout_date, _ = get_page_data (fm_layout)
                    layout_dates[fm_layout] = layout_date 
                if verbose: print(f'  {fm_layout}: {layout_date}')

        datasource_date: datetime = None
        if fm_datasource:
            for ds in fm_datasource.split(","):
                dsfile: str = f'_data/{ds}.yml'
                if not os.path.isfile(dsfile): 
                    print(f'{filename}: data file {dsfile} not found', file=sys.stderr)
                else:
                    dsfiledate: date = get_file_date (dsfile)
                    if verbose: print(f'  {dsfile}: {dsfiledate}')
                    if datasource_date == None or datasource_date < dsfiledate:
                        datasource_date = dsfiledate

        date = max(dt for dt in [commit_date, layout_date, datasource_date, fm_date, includes_date] if dt != None) # otherwise take highest non-null date
        if verbose: print(f'{filename}: commit_date={commit_date}, layout_date={layout_date}, datasource_date={datasource_date}, fm_date={fm_date}, includes_date={includes_date}')

    return date, fm_permalink

def process (filename: str, relpath: str):
    #print (filename)

    lastmod, permalink = get_page_data (filename)
    if not lastmod:
        return

    if permalink:
        relpath = permalink
    else:
        relpath = relpath if relpath else filename
        relpath = relpath.replace('\\', '/') 

        relpath,ext = os.path.splitext(relpath)
        fpath, fname = os.path.split(relpath)
        if fname == 'index':
            relpath = fpath

    url = baseurl + relpath
    sitemap.write('  <url>\n')        
    sitemap.write(f'    <loc>{url}</loc>\n')        

    #print (f'lastmod:       {lastmod}\n')
    if lastmod:
        sitemap.write(f'    <lastmod>{lastmod.astimezone().isoformat("T")}</lastmod>\n')        

    sitemap.write('  </url>\n')

def generate_for_project_pages():
    with open("_data/projects.yml", encoding="utf-8") as f:
        projects = yaml.load(f, Loader=SafeLoader)
        for project in projects:

            url = baseurl + 'projects/' + project["id"]

            sitemap.write('  <url>\n')        
            sitemap.write(f'    <loc>{url}</loc>\n')        
            sitemap.write('  </url>\n')

# main

if len(sys.argv) == 2:
    baseurl = sys.argv[1]
else:
    baseurl = 'https://signpath.org/'
    print(f'using default baseurl {baseurl}')

os.chdir ('docs')
try:
    include_dates = [date for date in [get_html_file_date(inc) for inc in global_includes] if date != None]
    includes_date = max (include_dates) if any (include_dates) else None

    with open("sitemap.xml", 'w', encoding='utf-8') as sitemap:
        sitemap.write ('<?xml version="1.0" encoding="UTF-8"?>\n')
        sitemap.write ('<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        files = glob.glob ('*.md', recursive=False) \
                + glob.glob ('*.html', recursive=False) \
                + glob.glob ('[a-z]*/**/*.md', recursive=True) \
                + glob.glob ('[a-z]*/**/*.html', recursive=True)
        for file in files:
            process (file, None)
        generate_for_project_pages()
        sitemap.write ('</urlset>')
finally:
    os.chdir('..')