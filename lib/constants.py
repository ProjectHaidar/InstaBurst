# Date: 12/16/2017
# Author: Ethical-H4CK3R
# Description: Contains configurations

version = '0.1.1'
error_log = 'log.txt'
credentials = 'accounts.txt'
database_path = 'sessions/sessions.db'

# colors 
colors = {
 'red': '\033[31m',
 'blue': '\033[34m',
 'white': '\033[0m',
 'green': '\033[32m',
 'yellow': '\033[33m'
 }

_colors = {
 'red': ['\x1b[0;31m', '\x1b[2;31m'],
	'blue': ['\x1b[0;34m', '\x1b[2;34m'], 
	'green': ['\x1b[0;32m', '\x1b[2;32m'],
	'white': ['\x1b[0;37m', '\x1b[2;37m'],
	'yellow': ['\x1b[0;33m', '\x1b[;33m']
}

# tor
tor_port = 9050
tor_ip = '127.0.0.1'

# time settings
proxy_time_out = 5
ip_fetch_timeout = 10
network_manager_time = 75

# limits
banners_tabs_amt  = 2 # the total amount of tabs 
proxies_max_size_ = 8 # total amount of proxies to store
proxies_wait_time = 1 # time to wait before retying IP fetch
failures_max_size = 32 # after this amount of fails change the ip
session_save_time = 6 # the time to write or rewrite the session information to database
passlist_max_size = 16 # maximum size of passwords to hold at once
proxy_total_usage = 16 # the amount of times a proxy can be used before requesting a new proxy
max_threads_usage = 16 # the amount of threads to use for cracking

# Instagram's details
instagram_username_field = 'username'
instagram_password_field = 'password'
home_url = 'https://www.instagram.com/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

site_details = {
 'name':'Instagram',
 'home_url': home_url, 
 'login_url': login_url,
 'username_field': instagram_username_field,
 'password_field': instagram_password_field,
 'header': {'referer': 'https://www.instagram.com'}
 }