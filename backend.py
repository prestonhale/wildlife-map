import web
import json
import os

urls = (
	'/', 'index',
	'/data/', 'data',
	'/images/(.*)', 'images'
	)

class index:
	def GET(self):
		index = open('index.html', 'r')
		return index


class data:
	def GET(self):
		data  = open('mom_data.json', 'r')
		return data

	def POST(self):
		data = web.data()
		with open('mom_data.json', 'a') as file:
			file.seek(-1, os.SEEK_END)
			file.truncate()
			file.write(',')
			file.write(data)
			file.write(']')
		return data

class images:
	def GET(self, name):
		ext = name.split(".")[-1]

		cType = {
			"png" : "images/png",
			"jpg" : "images/jpg",
			"gif" : "images/gif",
			"ico" : "images/x-icon"
		}

		if name in os.listdir('images'):
			web.header("Content-Type", cType[ext])
			return open('images/{0}'.format(name),"rb").read()
		else:
			raise web.notfound()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()