class Record:
  def __init__(self, id, user, content):
    self.id = id
    self.user = user
    self.content = content

  def to_text(self):
    return "{},{},{}".format(self.id, self.user, self.content)