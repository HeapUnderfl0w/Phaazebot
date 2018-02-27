import json, requests
import traceback
import _API_.Utils as utils

import _API_.Discord as discord
import _API_.DataBase as db
import _API_.Admin as admin

def call(BASE, web_info):
	"""
	used to process api calls from the web, comming in a /api/[module]/[function] scheme

	all function are also accessable via BASE.api.[module].[function]()
	"""

	if not BASE.active.api:
		class r (object):
			content = json.dumps(dict(status="error", msg="api_endpoint_closed")).encode("UTF-8")
			response = 403
			header = [('Content-Type', 'application/json')]
		return r

	web_info['path'].pop(0)

	if len(web_info['path']) == 0:
		class r (object):
			content = json.dumps(dict(status="error", msg="no_path", _m="Trying to find out the PhaazeAPI?. Try looking at phaaze.net/wiki?page=api")).encode("UTF-8")
			response = 400
			header = [('Content-Type', 'application/json')]
		return r

	function_call = ".".join(step for step in web_info['path'])
	function_call = "BASE.api." + function_call + "(BASE, info=web_info, from_web=True)"

	try:
		return eval(function_call)
	except:
		traceback.print_exc()

		class r (object):
			content = json.dumps(dict(status="error", msg="not_found")).encode("UTF-8")
			response = 400
			header = [('Content-Type', 'application/json')]
		return r
