class mymap:
  def __init__(self):
    self.list = []
    self.currentSize = 0

  def put(self, key, value):
    # Write code to add the element in your implementation
    # Find the index in which to store it by hashing the key: hash(key), then mod by your list length
    # Use Pythons internal hash function unless you have another one you want to use:
    print("Hash the key: " + str(key) + " to get it's hash value: " + str(hash(key)))

  def get(self, key):
    print("Implement this.")

  def contains(self, key):
    print("Implement this.")

  def size(self):
    print("Implement this.")
