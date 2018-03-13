
import re
import os
import urllib
import csv


with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print


csv_data =
"""

"""

splat_data = 
"""
Ok, this is demonstration code for simple Python functions.

The first Object is called the hall_of_heros which holds 
the name, twitter address, media, github account

The second is called the github_urls which holds a name and a 
github url of user
"""

#Hall of Heros (A.I./M.L.)
# ~name
# ~twitter account
# ~media link (youtube, etc.)
# ~github account
hall_of_heros =[ 
				 {'Name','Twitter URL','Github Account','Media URL'}
				 {'Naval Ravikant', 'https://twitter.com/naval',''},
                 {'Oriol Vinyals', 'https://twitter.com/OriolVinyalsML', 'http://bit.ly/2p4TWJW'},
                 {'Andrew Trask', 'https://twitter.com/iamtrask',''},
                 {'Balaji Srinivasan ','https://twitter.com/balajis','http://bit.ly/2FIcbyx'},
                 {'Bryan Johnson ','https://twitter.com/bryan_johnson','http://bit.ly/2FNZi68'},
                 {'Tristan Harris','https://twitter.com/tristanharris','http://bit.ly/2Dni4vD'},
                 {'Juan Benet','https://github.com/jbenet',''},
                 {'Trent McConaghy','','http://bit.ly/2FDXzwz'}

                 ]

github_urls =[{'Douglas Kuhn','https://github.com/bluewitch'},
			  {'Juan Benet','https://github.com/jbenet'},
			  {'',''},


]

ewallet_urls = {'https://myetherwallet.github.io/'}

# blockchain_urls, 
# Holds the name and url to important web resources

blockchain_urls = [{'Reatime Blockchain Monitor', 'https://blocks.wizb.it/'},
				   {'Crypto Currecny Activity', 'https://coincheckup.com/analysis/github'},
				   {'',''},
                   {'https://blockstack.org/', ''},
                   ]
