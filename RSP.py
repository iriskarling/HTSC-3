
class inventory():
    def __init__(self,inventoryList):
        self.inventoryList = []
    
    def AddGoods(self,SerialNumber,price,EGoodsSpec): #RSP principal
        egoods = EGoods(SerialNumber,price,EGoodsSpec)
        self.inventoryList.append(egoods)

    def get(self,SerialNumber): #RSP principal
        for i in self.inventoryList:
            if i.getSerialNumber == SerialNumber:
                return i
        return None

    def search(self, searchSpec): 
        result = []
        for i in self.inventoryList:
            if i.getSpec().matches(searchSpec):
                result.append(i)
        return result


class EGoods:
    def __init__(self,SerialNumber,price,EGoodsSpec):
        self.SerialNumber = SerialNumber
        self.price = price
        self.EGoodsSpec= EGoodsSpec
    def getSerialNumber(self): #RSP principal
        return self.SerialNumber
    def getPrice(self): #RSP principal
        return self.price
    def setPrice(self,price):#RSP principal
        self.price = price
    def getSpec(self):#RSP principal
        return self.EGoodsSpec

class EGoodsSpec:
    def __init__(self,Properties):
        self.Properties = Properties
    def getProperty(self,propertyName): #RSP principal
        return self.Properties[propertyName]
    def getProperties(self):#RSP principal
        return self.Properties
    def matches(self,OtherSpec): #RSP principal
        for i in OtherSpec.getProperties():
            propertyName = i
            if self.getProperty(propertyName) != OtherSpec.getProperty(propertyName):
                return False
        return True
    def AddProperty(self,propertyName,property):#RSP principal
        self.Properties[propertyName] = property


if __name__ == "__main__":
    # initilise the inventory class and add some Egoods into it
    Inventory = inventory([])
    EGoodsSpec1 = EGoodsSpec({"Brand":"Lenovo","Size":"16.0寸","Processor":"i7","Class":"游戏本"})
    EGoodsSpec2 = EGoodsSpec({"Brand":"Apple","Size":"15.0寸","Processor":"i6","Class":"其他"})
    EGoodsSpec3 = EGoodsSpec({"Brand":"Dell","Size":"14.0寸","Processor":"i7","Class":"二合一笔记本"})
    EGoodsSpec4 = EGoodsSpec({"Brand":"Dell","Size":"14.0寸","Processor":"i7","Class":"二合一笔记本"})
    EGoodsSpec5 = EGoodsSpec({"Brand":"Dell","Size":"14.0寸","Processor":"i6","Class":"二合一笔记本"})
    EGoodsSpec6 = EGoodsSpec({"Brand":"Dell","Size":"14.0寸","Processor":"i7","Class":"二合一笔记本"})


    Inventory.AddGoods('101',4500.00,EGoodsSpec1)
    Inventory.AddGoods('102',6500.00,EGoodsSpec2)
    Inventory.AddGoods('103',3500.00,EGoodsSpec3)
    Inventory.AddGoods('104',7500.00,EGoodsSpec4)
    Inventory.AddGoods('105',9500.00,EGoodsSpec5)
    Inventory.AddGoods('106',8500.00,EGoodsSpec6)

    # the requests of client
    clientSpec = EGoodsSpec({"Brand":"Dell","Size":"14.0寸","Processor":"i7","Class":"二合一笔记本"})
    clientPrice = "3000-8000"
    temp = clientPrice.split("-")
    startPrice,EndPrice = int(temp[0]),int(temp[1])

    # show the results of research
    result = Inventory.search(clientSpec)
    if len(result):
        print("You may like these instruments")
        for i in result:
            spec = i.getSpec()
            if i.getPrice() > startPrice and i.getPrice() < EndPrice:
                print("we have a "+ spec.getProperty("Brand")+" with the following properties")
                for j in spec.getProperties():
                    if j == "Brand":
                        continue
                    print(" "+ j + ":"+spec.getProperty(j))
                print("you can have this " + spec.getProperty("Brand") + "for RMB" + str(i.getPrice()) + "\n")
    else:
        print("sorry, we have nothing for you")