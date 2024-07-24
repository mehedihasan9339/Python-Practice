class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud.add("Python") 
cloud.add("python") 
cloud.add("python")
print(cloud.tags) # {'python': 3}

print(cloud.__getitem__("Python")) # 3

cloud.__setitem__("charp", 1)
print(cloud.__getitem__("charp")) # 1
print(cloud.tags) # {'python': 3, 'charp': 1}
print(cloud.__len__()) # 2

for item in cloud.__iter__():
    print(item)

# python
# charp

