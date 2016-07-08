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

	def output_html(self,path,datas):
		fout=open(path+'index.html','w')
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")

		
		fout.write("<tr>")		
		fout.write("<td><h3>title</h3></td>")
		fout.write("<td><h3>time</h3></td>")
		fout.write("<td><h3>URL<h3></td>")
		fout.write("</tr>")

		for data in datas:	
			fout.write("<tr>")		
			fout.write("<td><a href='%s'>%s</a></td>" % (data[2].encode('utf-8'),data[0].encode('utf-8') ))
			fout.write("<td>%s</td>" % data[1])
			fout.write("<td><a href='%s'>%s</a></td>" % (data[3].encode('utf-8'),data[3].encode('utf-8')))
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")

