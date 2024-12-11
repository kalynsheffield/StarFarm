
class Crop:
    list =[]
    index = 0

    def __init__(self, crop = "", amount = int):
        self.crop = crop
        self.amount = amount
    
    def __eq__(self, other):
        if isinstance(other, Crop):
            return self.selecrop == other.selecrop
        return False


    def addToList(self, crop, amount):
        info = Crop(crop, amount)
        Crop.list.append(info)

    def SubAmount(self, crop, amount):
        crop = crop + " seed(s)"
        check = Crop(crop, amount)
        for obj in Crop.list:
            if obj.crop == check.crop:
                obj.amount -= amount
    
    def Grown(self, crop="", amount=int, start_index=int):
        for obj in Crop.list:
            if Crop.index >= start_index:
                new_crop = obj.crop.replace(' seed(s)', '')
                if crop == new_crop:
                    if obj.amount == amount:
                        obj.crop = obj.crop.replace(' seed(s)', '(s)')
                    else:
                        obj.amount -= amount
                        new_crop = new_crop + "(s)"
                        Crop.addToList(self,new_crop, amount)
            else:
                Crop.index += 1
                continue
           

    def CheckList(self,check):
        if check in Crop.list:
            print("You do not have the seeds for", check)
            quit()


    def printList(self):
        for obj in Crop.list:
            print(obj.amount, obj.crop, sep = ' ')