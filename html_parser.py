# coding:utf8
import re
from bs4 import BeautifulSoup
import urlparse
import html_outputer
import html5lib
class HtmlParser(object):
	def _get_new_url(self,page_url,soup):
		link =soup.find('a',text="下一页")
		if len(link)==0:
			return None
		new_url=link['href']
		new_url=urlparse.urljoin(page_url,new_url)
		return new_url
		#for link in links:
			#new_info=link.get_text();
			#if new_info=='下一页':
			#	new_url=link['href']
			#	print new_url
			#	new_url=urlparse.urljoin(page_url,new_url)
			#	return new_url
			#return link['href']
		
		
	def _get_new_datas(self,soup):
		res_datas = []
		reg=re.compile("http://job.xjtu.edu.cn:80/jobsHtml/\d+\.html")
		a_infos=soup.find_all('a',href=reg)
		print len(a_infos)
		for a_info in a_infos:		
			url= a_info['href']
			print url
			res_datas.append(url)
		return res_datas

	def get_title(self,soup):
		
		title_node=soup.find('h1',class_='artititle')
		#print title_node.get_text()
		return title_node.get_text()
	def get_time(self,soup):
		time_nodes=soup.find('div',class_='artInfo')
		info=time_nodes.get_text().encode('utf-8')
		#print info
		year='年'
		month='月'
		day='日'
		info=info.replace(year,'-')
		#print info
		info=info.replace(month,'-')
		info=info.replace(day,' ')
		info=info.replace('\n','')
		info=info.replace('\r','')

		info=info+':00'
		#print info[-15:-1]
		return info[-19:]

	def create_htmlfile(self,index_dictory,page_url,soup):
		if page_url is None:
			return None
		#print page_url
		sp=page_url.split('/')
		URL_name=index_dictory+sp[-1]
		file=open(URL_name,"w")
		info=soup.find('div',class_='artibody')
		#print info

		file.write(str(info))
		
		#print URL_name
		file.close()
		return URL_name

	def get_data(self,page_url,html_str):
		
		if page_url==None or html_str==None:
			return None
		infos=[]  #include: title time path sorce...
	
		soup= BeautifulSoup(html_str,'html.parser',from_encoding='utf-8')
		#get title
		title=self.get_title(soup)
		infos.append(title.strip())
		#get time
		infos.append(self.get_time(soup).strip())
		#create HTML file & get path
		#outputer= html_outputer.HtmlOutputer()
		#path=outputer.download_data(page_url)
		#print path
		
		path=self.create_htmlfile("/home/m/URL/",page_url,soup)
		#print path
		
		infos.append(path.strip())
		
		#get source
		infos.append(page_url)
		#return infos
		return infos






	def parse(self,page_url,html_str):
		if page_url is None or html_str is None:
			return None
		
		soup= BeautifulSoup(html_str,'html5lib',from_encoding='utf-8')
	
		new_url=self._get_new_url(page_url,soup)
		
		new_datas=self._get_new_datas(soup)

		
		return new_url,new_datas
