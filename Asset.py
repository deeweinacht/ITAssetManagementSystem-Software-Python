
class Asset:
    def __init__(self, asset_id, brand='', category='',
                 department='', status='', acquired=None):
        self.ID = asset_id
        self.brand = brand
        self.category = category
        self.department = department
        self.status = status
        self.acquired = acquired

    def get_ID(self):
        return self.ID

    def set_ID(self, new_ID):
        self.ID = new_ID

    def get_brand(self):
        return self.brand

    def set_brand(self, new_brand):
        self.brand = new_brand

    def get_category(self):
        return self.category

    def set_category(self, new_category):
        self.category = new_category

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status