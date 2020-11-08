[TOC]

## BeautifulSoup



### 数据解析 + 提取

```python
soup  = Beautifulsoup(html_str,'lxml',from_enconding='utf-8')

soup = Beautifulsoup(open('index.html'))


print(soup.prettify)     # 输出html
```

## 对象种类：

```python
	Beautiful Soup 将复杂 HTML 文档转换成一个复杂的树形结构，每个节点都是 Python
对象，所有对象可以归纳为 4 种：

     Tag :
           title 和 a 标签以及它们里面的内容被称作 Tag 对象
           eg:   soup.a/title   (查找到第一个符合的标签)
            	soup.title.name = 'mysite'  # 修改便签名
                
                soup.p['class']   #提取属性值 （获取标签内的内容）
                
     NavigableString：
    	 获取标签内部的文字
        	eg: 	soup.p.string
              		unicode_string = unicode(soup.p.string)   # 转换成unicode 字符串
     BeautifulSoup：
    		文档的全部内容（BeautifulSoup 对象并不是真正的 HTML 或 XML 的标签）
        
     Comment：
    		文档的注释部分 （利用 .string 来输出它的内容，发现它已经把注释符号去掉）
        
        if type(soup.a.string)==bs4.element.Comment:
            print(soup.a.string)
```

### 遍历文档树：

```python
	Tag 中的.contents 和 .children 是非常重要的。tag的.content 属性可以将 tag 子节点以列表的方式输出：
    		eg: print (soup.head.contents)   # 列表
            	print len(soup.head.contents)
			   print soup.head.contents[0].string
            
  注意：	字符串没有 .contents 属性,因为字符串没有子节点


descendants属性可以对所有 tag 的子孙节点进行递归循环：
			eg: for child in soup.head.descendans:
            		print(child)
```

### 搜索文档树：

```python
find_all():
    搜索当前 tag 的所有 tag 子节点,并判断是否符合过滤器的条件
    
    eg:  find_all(name,attrs,recusive,text,**kwargs)
        
        
        name: 
            查找所有名字为 name 的标签，字符串对象会被自动忽略掉。name参数取值可以是字符串、正则表达式、列表、True 和方法。
        import re
	    for tag in soup.find_all(re.compile("^b")):
 			print(tag.name)    #查找 b开头的标签
        
	 **kwargs：
    		搜索时会把该参数当作指定名字 tag 的属性来搜索。搜索指定名字的属性时可以使用的参数值包括 字符串、正则表达式、列表、True 。
        	print soup.find_all(id='link2')
        import re
		print soup.find_all(href=re.compile("elsie"))  # 查找所有href 属性内涵有elsie的标签
        
        test:
            搜索文档中的字符串内容。与 name 参数的可选值一样, text参数接受字符串、正则表达式、列表、True 。
        print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
		print soup.find_all(text=re.compile("Dormouse"))  
        
        
        limit:
            参数限制返回结果的数量
            print soup.find_all("a", limit=2)
            
       recursive 参数：
    		搜素当前标签的第一个标签
        	print soup.find_all("title", recursive=False)
```

```python
find(name,attrs,recursive,text,**kwargs) 

注释：
	它 与 find_all() 方 法 唯 一 的 区 别 是find_all() 方法的返回结果是所有满足要求的值组成的列表，而 find() 方法直接返回find_all 搜索结果中的第一个值。
```

## css 选择器：

```python
 CSS 也是可以定位元素的位置 ( soup.select()，返回类型是 list)
 
标签名查找：
	直接： 	soup.select('title')
    
    间接：		soup.select('html head title')
    
    标签(子标签)  soup.select('head>title')
    
    查找p 下的id='link':   soup.select('p>#link')
        
    id="link1",class=sisiter 的所有兄弟标签:	soup.select("#link1 ~ .sister")

   id="link1"之后 class=sisiter 的子标签:		soup.select("#link1 + .sister")
```

```python
id 查找：
	print soup.select("a#link2")
    
    
 class类名查找:
    print soup.select(".sister")
    
    
是否存在某个属性来查找:
    print soup.select('a[href]')

属性值来查找:
    print soup.select('a[href^="http://example.com/"]')
    print soup.select('a[href$="tillie"]')
```

## xpath 选择器：

```python
解析：
	BeautifulSoup 和 lxml 的原理不一样，BeautifulSoup 是基于 DOM 的，会载入整
个文档，解析整个 DOM 树，因此时间和内存开销都会大很多。
	lxml 是使用XPath 技术查询和处理 HTML / XML 文档的库，只会局部遍历，
    
    lxml 的 XPath 写起来麻烦，开发效率不如 BeautifulSoup，
```

```python
案例：
    html = etree.HTML(html_str)
    result = etree.tostring(html)
    
    urls = html.xpath(".//*[@class='sister']/@href")
    
 lxml 的一个非常实用的功能就是自动修正 html 代码
```

