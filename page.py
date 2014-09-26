from mongoengine import *

class Page(Document):
	title = StringField(max_length=200, required=True)
	tag = StringField(max_length=500)

connect('mongodb_test_db')

page = Page(_id=1, title="hello title", tag="tag1, tag2")

page.save()

page = Page(_id=1, title="hey title", tag="tag1, tag3")

page.save()

for page in Page.objects(title="hey title"):
	print "title:" + page.title + " tag: " + page.tag

for page in Page.objects():
	print "title:" + page.title + " tag:" + page.tag
