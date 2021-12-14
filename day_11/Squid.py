class Squid:
    def __init__(self, count, hasFlashed, name):
        self.count = count
        self.hasFlashed = hasFlashed
        self.neighbours = []
        self.name = name
        self.total_flash_count = 0

    def increaseCount(self):
        self.count += 1

    def check(self):
        if self.count == 9 and not self.hasFlashed: self.flash()

    def flash(self):
        self.total_flash_count += 1
        self.count = 0
        self.hasFlashed = True
        for n in self.neighbours:
            if n.count == 9 and not n.hasFlashed: n.flash()
            else:
                if not n.hasFlashed: n.increaseCount()
            n.check()
