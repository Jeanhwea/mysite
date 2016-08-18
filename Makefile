#########################################################################
#         _                          _                                  #
#        | |                        | |                                 #
#        | |   ___    __ _   _ __   | |__   __      __   ___    __ _    #
#    _   | |  / _ \  / _` | | '_ \  | '_ \  \ \ /\ / /  / _ \  / _` |   #
#   | |__| | |  __/ | (_| | | | | | | | | |  \ V  V /  |  __/ | (_| |   #
#    \____/   \___|  \__,_| |_| |_| |_| |_|   \_/\_/    \___|  \__,_|   #
#                                                                       #
#                                                                       #
# This file create on 2016-08-15                                        #
# It's free for you to use and share.                                   #
#                                                                       #
# Author : Jinghui Hu                                                   #
# Email  : hujinghui@buaa.edu.cn                                        #
# Github : https://github.com/Jeanhwea/                                 #
#                                                                       #
#########################################################################

MANAGE := ./manage.py

all: check test

check:
	$(MANAGE) check

test:
	$(MANAGE) test

collectstatic:
	$(MANAGE) collectstatic

server:
	$(MANAGE) runserver

create:
	$(MANAGE) createsuperuser

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

upload:
	rsync -rva -e ssh --delete --exclude='mysite/settings.py' --exclude='*.pyc' . ubuntu@aws:/home/ubuntu/codes/mysite
