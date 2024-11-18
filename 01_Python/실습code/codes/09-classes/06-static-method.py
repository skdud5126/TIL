class StringUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()


text = 'hello, wolrd!'

res1 = StringUtils.reverse_string(text)

res2 = StringUtils.capitalize_string(text)

print(res1)  # !drlow ,olleh
print(res2)  # Hello, wolrd!