from swap_meet.item import Item 

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory 

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        else:
            return False 

    def get_by_category(self, category):
        inventory_list = []
        for item in self.inventory: 
            if item.category == category:
                inventory_list.append(item)
        return inventory_list 

    def swap_items(self, friend, my_item, their_item):
        if their_item in friend.inventory and my_item in self.inventory:
            self.add(their_item)
            friend.add(my_item)
            self.remove(my_item)
            friend.remove(their_item)
            return True 
        else:
            return False 

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory: 
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
        return False 

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None 
        best = items[0]
        for item in items:
            if item.condition > best.condition:
                best = item 
        return best 


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best and their_best:
            return False
        return self.swap_items(other,my_best, their_best)