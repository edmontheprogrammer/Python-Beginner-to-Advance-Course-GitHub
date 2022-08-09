class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __set__item(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
