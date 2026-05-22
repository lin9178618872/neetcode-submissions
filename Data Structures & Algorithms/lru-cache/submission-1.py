class Node:
    def __init__(self, key, val):
        # 单独赋值 key
        self.key = key
        
        # 单独赋值 val
        self.val = val
        
        # prev 单独赋值
        self.prev = None
        
        # next 单独赋值
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # 保存容量
        self.cap = capacity
        
        # 创建字典
        self.cache = {}
        
        # 创建左哨兵节点
        self.left = Node(0, 0)
        
        # 创建右哨兵节点
        self.right = Node(0, 0)
        
        # left.next = right
        self.left.next = self.right
        
        # right.prev = left
        self.right.prev = self.left


    def remove(self, node):
        # 先保存前一个节点
        prev_node = node.prev
        
        # 再保存后一个节点
        next_node = node.next
        
        # 断开前节点的 next
        prev_node.next = next_node
        
        # 断开后节点的 prev
        next_node.prev = prev_node


    def insert(self, node):
        # 取出当前最后一个真实节点
        prev_node = self.right.prev
        
        # 右哨兵
        next_node = self.right
        
        # 让前节点指向新节点
        prev_node.next = node
        
        # 新节点的 prev 指向前节点
        node.prev = prev_node
        
        # 新节点的 next 指向 right
        node.next = next_node
        
        # right 的 prev 指向新节点
        next_node.prev = node


    def get(self, key: int) -> int:
        # 判断 key 是否存在
        if key in self.cache:
            
            # 取出节点
            node = self.cache[key]
            
            # 先移除
            self.remove(node)
            
            # 再插入到最右边（表示最近使用）
            self.insert(node)
            
            # 返回值
            return node.val
        
        # 不存在返回 -1
        return -1


    def put(self, key: int, value: int) -> None:
        
        # 如果 key 已经存在
        if key in self.cache:
            
            # 取出旧节点
            old_node = self.cache[key]
            
            # 删除旧节点
            self.remove(old_node)
        
        # 创建新节点
        new_node = Node(key, value)
        
        # 存入字典
        self.cache[key] = new_node
        
        # 插入到双向链表尾部
        self.insert(new_node)
        
        # 如果超出容量
        if len(self.cache) > self.cap:
            
            # 最久未使用节点
            lru_node = self.left.next
            
            # 从链表删除
            self.remove(lru_node)
            
            # 从字典删除
            del self.cache[lru_node.key]