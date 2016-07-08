import url_manager,html_downloader,html_outputer,html_parser
import os
import MySQLdb
class SpiderMain(object):
	def __init__(self):
		self.urls=url_manager.UrlManager()
		self.downloader=html_downloader.HtmlDownloader()
		self.parser=html_parser.HtmlParser()
		self.outputer=html_outputer.HtmlOutputer()
	#start method
	def craw(self,root_url):
		count=1
		#create db
		conn=MySQLdb.Connect(
				host='127.0.0.1',
				port=3306,
				user='root',
				passwd='m',
				charset='utf8'
				)
		cursor=conn.cursor()
		cursor.execute("set names utf8")
		cursor.execute("use job")   #use job database
		#sql="INSERT INTO job_xjtu_info VALUES('job','2016-07-07 21:09:00','/home/m/URL/268907517.html','http://job.xjtu.edu.cn:80/jobsHtml/268907517.html')"
		
		#cursor.execute(sql)
		#print cursor.rowcount
		#cursor.execute("select * from job_xjtu_info")
		#rs=cursor.fetchall()
		#print rs
		#print conn
		#print cursor


		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				url=self.urls.get_new_url()
				#parse
				print 'craw %d : %s' % (count,url)
				html_str=self.downloader.download(url)
				#print len(html_str)	
				new_url,new_datas=self.parser.parse(url,html_str)
				print new_url
				self.urls.add_new_url(new_url)
				if len(new_datas)==0:
					continue


				for new_data in new_datas:
					html_info=self.downloader.download(new_data)
					#the method return a table include some data for database
					print len(html_info)
					# return a table     include : title time path source
					infos=self.parser.get_data(new_data,html_info)  
					if len(infos)!=0:
						sql="INSERT INTO job_xjtu_info VALUES('%s','%s','%s','%s')" % (infos[0],infos[1],infos[2],infos[3])
						try:
							cursor.execute(sql)
							conn.commit()
						except Exception as e:
							print e
							conn.rollback()
					#run database port : add data in mysql database`
			except:
				print 'craw failed'
			if count==10:
				break;
			count=count+1


		sql="select * from job_xjtu_info"
		cursor.execute(sql)
		conn.commit()
		rs=cursor.fetchall()
		self.outputer.output_html('/home/m/HTTP',rs)

		

		cursor.close()
		conn.close()

		

if __name__=="__main__":
	root_url="http://job.xjtu.edu.cn/jobmore.do"   #index
	obj_spider=SpiderMain()
	obj_spider.craw(root_url) # run method
