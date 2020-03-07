from record import Record

class DB:
  def __init__(self):
    self.records = []

# Load records from existing file
  def load(self, path):

    with open(path) as fp:
      line = fp.readline()
      count = 0

      while line:
        self.add_record(line)
        line = fp.readline()
        count += 1

    # print("I found {} records.".format(count))


# Saves records to file
  def save(self, path):
    count = 0

    self.clean_records()

    with open(path, "w") as fp:
      text_output = ""

      for rec in self.records:
        text_output += "{}\n".format(rec.to_text())
        count += 1
        
      fp.write(text_output)
      # print("I wrote {} records.".format(count))

# Add a single record to the current array
  def add_record(self, line):

    contents = line.split(',')
    contents[2] = contents[2].replace("\n", "")

    # Auto assign id if none given
    if(contents[0] == "x"):
      contents[0] = self.highest_record() + 1

    if (not self.read_record(contents[0])):
      new_record = Record(int(contents[0]), contents[1], contents[2])
      self.records.append(new_record)
    else:
      new_record = False
      print("Record with id of {} already exists".format(contents[0]))

    return new_record


# Return a single record object by its id, or false if it does not exist
  def read_record(self, id):
    found_record = False

    for rec in self.records:
      if (rec.id == id):
        found_record = rec

    return found_record

# Update a record's content
  def update_record(self, id, new_content):
    for rec in self.records:
      if (rec.id == id):
        found_record.content = new_content


# Delete a record
  def delete_record(self, id):
    for rec in self.records:
      if (rec.id == id):
        self.records.remove(rec)

# Return record with the highest id
  def highest_record(self):
    highest = 0
    for rec in self.records:
      if (int(rec.id) > highest):
        highest = int(rec.id)

    return highest

# Sort and re-number all records
  def clean_records(self):

    # Bubble sort
    for i in range(0, len(self.records)):
      for j in range(0, len(self.records)-i-1):
        if(self.records[j].id > self.records[j+1].id):
          temp = self.records[j]
          self.records[j] = self.records[j+1]
          self.records[j+1] = temp

    # Renumber
    count = 1
    for rec in self.records:
      rec.id = count
      count += 1