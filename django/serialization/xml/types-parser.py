x="""<foo>
   <bar>
      <type foobar="1"/>
      <type foobar="2"/>
   </bar>
</foo>"""

y=BeautifulSoup(x)
print(y.foo.bar.type["foobar"])
