from urllib.parse import urlparse, parse_qs

address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)
print(parts)
#ParseResult(scheme='https', netloc='www.google.com', path='/search', params='', query='q=gray+squirrel&tbm=isch', fragment='')
print(parts.query)
#q=gray+squirrel&tbm=isch
query = parse_qs(parts.query)
print(query)
#{'q': ['gray squirrel'], 'tbm': ['isch']}