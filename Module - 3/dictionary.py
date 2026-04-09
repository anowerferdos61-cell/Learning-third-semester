# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.values())
# print (thisdict.keys())
# print (thisdict.items())

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'year' : 2026,
  'color' : ['red', 'blue', 'white']
}
print(thisdict.values())


d = {"a": 1, "b": 2}
val = d.get("c", 3)
print(val)