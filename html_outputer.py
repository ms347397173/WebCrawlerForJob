import urllib
class HtmlOutputer(object):

	def download_data(self,data):
		if len(data)==0:
			print "URL table is None"
			return None
		print data
		sp=data.split('/')
		URL_name='/home/m/URL/'+sp[-1]
		download_URL=urllib.urlretrieve(data,URL_name)
		return URL_name

#	def output_html(self):
#		fout=open('output.html','w')
#		fout.write("<html>")
#		fout.write("<body>")
#		fout.write("<table>")
#
#		for data in self.datas:	
#			fout.write("<tr>")		
#			fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
#			fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
#			fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
#			fout.write("</tr>")
#
#		fout.write("</table>")
#		fout.write("</body>")
#		fout.write("</html>")
#
