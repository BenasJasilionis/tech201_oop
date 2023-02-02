# Methods

class MethodExamples:

    #this_can_be_accessed_easily = "Hi, I am easily found!"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, I am easily found!"

# x = MethodExamples()
#
# print(x.this_can_be_accessed_easily)
# x.this_can_be_accessed_easily = "I have been changed!"
# print(x.this_can_be_accessed_easily)

# Usually dont want class variables to be accessible
# In many languages need to use Public and Private to determine who can access __init__
def __init__(self):
    self._this_can_be_accessed_easily = "Hi, I am easily found!"
# def get_this_can_be_accessed_easily(self):
#     return self.this_can_be_accessed_easily
#
# def set_this_can_be_accessed_easily(self, value_to_be_set):
#     self.this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()
# To protect attributes, use _, to protect methods, use __

print(x._this_can_be_accessed_easily)
x.set_this_can_be_accessed_easily = "I have been changed!"
print(x._this_can_be_accessed_easily)

# Look into setting public and private attributes and methods on python (wont be on test)