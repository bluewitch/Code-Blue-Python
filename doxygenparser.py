# doxygenparser.py

'''
A class to strip all the setting from a Doxyfile and configure some of them.

like where I'm going with this?  abrahamvanhelpsing@gmail.com - it's a stackexchange joke...
'''
import subprocess


class DoxyConfig:
	def __init__(self, url=''):
		'''
		'''
		pass

	def __gen_strip(self):
		'''
		'''
		p = subprocess.Popen(["doxygen","-g"], stdout=subprocess.PIPE)
		p.wait()
		p1 = subprocess.Popen(["cat","Doxyfile"], stdout=subprocess.PIPE)
		p2 = subprocess.Popen(["grep","-v","\#"], stdin=p1.stdout, stdout=subprocess.PIPE)
		p3 = subprocess.Popen(["grep","-v","^$"], stdin=p2.stdout, stdout=subprocess.PIPE)
		p1.stdout.close()
		p2.stdout.close()
		p3.wait()
		temp_list = []
		for line in p3.stdout:
			line = str(line)
			i=0
			items = []
			for item in line.split('='):
				items.append(item.lstrip().rstrip())
			temp_list.append(items)
		self.settings = temp_list

	def __set(self, change_setting):
		'''
		Derpity derp derp
		'''
		for item, val in change_setting.iteritems():
			try:
				self.settings[self.settings.index(item)]=val
			except:
				self.settings.append([item, val])

	def gen(self):
		'''
		'''
		self.__gen_strip()

	def set(self, change_setting={}, default=True):
		'''
		'''
		if default:
			change_setting = {
				'GENERATE_XML' : 'YES',
				'ENABLE_PREPROCESSING' : 'YES',
				'MACRO_EXPANSION' : 'YES',
				'EXPAND_ONLY_PREDEF' : 'YES',
				'EXPAND_AS_DEFINED' : 'CONTAINER',
				'OUTPUT_DIRECTORY' : '/tmp/autowrapper',
				'INPUT' : '?',
				'FILE_PATTERNS' : '.h, .hpp',
				'RECURSIVE' : 'YES',
				'EXTRACT_ALL' : 'YES',
				'EXTRACT_PRIVATE' : 'YES',
				'EXTRACT_STATIC' : 'YES'
				}
		self.__set(change_setting)

	def __format(self):
		'''
		'''
		retval = []
		leaders = []
		for i in self.settings:
			leaders.append(i[0])
		min_width = len(max(leaders, key=len))
		for i, j in self.settings:
			retval.append(i.ljust(min_width) + '= ' + j)
		return retval


	def save(self, to_save, file_name=False):
		'''
		'''
		print to_save
		pass

	def __call__(self):
		self.boom_goes_the_dynamite()

	def boom_goes_the_dynamite(self, auto=True):
		'''
		'''
		self.__gen_strip()
		if auto:
			self.set()
			self.save(self.__format())

class DoxyParse:
	def __init__(self):
		pass
	def __call__(self):
		pass

class Doxy:
	def __init__(self):
		self.doxy_conf = DoxyConfig()
		self.doxy_run = DoxyParse()

	def run(self):
		self.doxy_conf()
		self.doxy_run()

if __name__ == '__main__':
	doxy = Doxy()
	doxy.run()
