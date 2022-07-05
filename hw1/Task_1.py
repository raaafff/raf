def domain_name(url):
	   domain = url.split(r'//')[-1]
	   domain = domain.split(r'www.')[-1]
	   domain = domain.split(r'.')[::1][0]
	   return domain
       
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

    
