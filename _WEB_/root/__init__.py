def main(BASE, info):
	if not len(info['path']) == 0:
		try:
			eval('import ' + info['path'][0])
			r = eval(info['path'][0] + '.main(BASE, info)')
			return r
		except:
			return page_not_found()

	else:
		class r(object):
			response = 404
			header = ("Content-Type", "text/html")
			content = open('root.html', "rb").read()

		return r


def page_not_found():
	class r(object):
		response = 404
		header = ("Content-Type", "text/html")
		content = open('not_found.html', "rb").read()

	return r
