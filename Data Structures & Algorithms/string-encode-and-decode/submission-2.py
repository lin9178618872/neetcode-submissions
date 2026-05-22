class Solution:
    def encode(self, strs):
        # Step 1: 处理空列表情况
        if not strs:  
            return " "  # 如果 strs 为空列表，则返回一个空格字符串
        
        # Step 2: 使用特殊字符 chr(1) 连接字符串列表
        separator = chr(1)  # 选择 ASCII 值为 1 的字符作为分隔符
        encoded_string = separator.join(strs)  # 用该分隔符连接所有字符串
        return encoded_string  # 返回编码后的字符串
    def decode(self, s):
        # Step 1: 处理特殊空格情况
        if s == " ":  
            return []  # 如果输入是 " "，说明原来的列表是空的，返回空列表
        
        # Step 2: 使用相同的分隔符 chr(1) 进行拆分
        separator = chr(1)  # 获取之前用的分隔符
        decoded_list = s.split(separator)  # 按分隔符拆分字符串，恢复原始列表
        return decoded_list  # 返回解码后的字符串列表
