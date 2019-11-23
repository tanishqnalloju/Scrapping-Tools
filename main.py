def parse(self,response):
        token = response.xpath('.//*[@name="form_key"]/@value').extract_first()
        yield scrapy.FormRequest('https://www.foagroup.com/customer/account/loginPost/',
                                 formdata={'form_key':token,'login[password]':'&lt;yourpassword>','login[username]':'dovemattress@yahoo.com','send':''},
                                 callback=self.startscraping)

def startscraping(self,response):
        yield scrapy.Request('https://www.foagroup.com/bedroom/bed.html',callback=self.getcardlinks)

def getcardlinks(self,response):
    print(response.text)

