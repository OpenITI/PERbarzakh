import re
import os

multivol = dict()
uri_d = dict()
empty_d = dict()
for fn in os.listdir("."):
    if re.findall("AOCP", fn) and not fn.endswith(".yml"):
        book_uri = ".".join(fn.split(".")[:2])
        with open(fn, mode="r", encoding="utf-8") as file:
            text = file.read()
        volumes = set(re.findall("PageV\d+", text))
        if len(volumes) > 1:
            if not book_uri in multivol:
                multivol[book_uri] = []
            multivol[book_uri].append([fn, volumes])
        if book_uri not in uri_d:
            uri_d[book_uri] = []
        uri_d[book_uri].append([fn, volumes])
        text = re.sub("!\[.+", "", text)
        empty_pages = re.findall("PageV\d+P\d+[\r\n#~% ]+(?=Page)", text)
        if empty_pages:
            empty_d[fn] = len(empty_pages)
            
print("MULTIVOLUME:")
for k, v in multivol.items():
    print(k, v)
    print("---------------")

print("URIs with more than one file:")
for uri, fns in uri_d.items():
    if len(fns) > 1:
        print(uri, len(fns))
        for fn, volumes in fns:
            print("    -", fn)
            print("        =>", volumes)

print("-------------")
print("Empty pages:")
for fn in empty_d:
    print(fn, empty_d[fn])

            
            
