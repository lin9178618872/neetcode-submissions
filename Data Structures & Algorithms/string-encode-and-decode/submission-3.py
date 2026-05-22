class Solution:
    def encode(self, strs):
        if not strs:
            return " "
        
        separator = chr(1)
        encoded_string = separator.join(strs)
        return encoded_string

    def decode(self, s):
        if s == " ":
            return []
        
        separator = chr(1)
        decoded_list = s.split(separator)
        return decoded_list