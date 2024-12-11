class Plot:
    out_plot = []
    row = 0
    col = 0
    plot_hold = 0 
    plot_amt = 0

    def __init__(self, selecrop="",watered= False):
        self.selecrop = selecrop
        self.watered = watered

    def __eq__(self, other):
        if isinstance(other, Plot):
            return self.selecrop ==  other.selecrop
        return False
    
    def CreatePlot(self,row, col):
        self.row = row
        self.col = col 
        Plot.plot_hold = row * col

    def AddCrops(self, crop="", amount=int):
        Plot.plot_amt += amount
        if Plot.plot_amt <= Plot.plot_hold:
            check = 0
            for i in range(self.row):
                in_plot =[]
                for j in range(self.col):
                    if check != amount:
                        check += 1
                        info = Plot(crop, False)
                        in_plot.append(info)
                    else:
                        break
                Plot.out_plot.append(in_plot)
        else:
            print("not enough plot to plant", crop)
            quit()

    def Water(self):
        for row in Plot.out_plot:
            for obj in row:
                obj.watered = True
        Plot.plot_amt = 0

    def DelCrops(self, crop="", amount=int):
        Plot.plot_amt -= amount
        check = Plot(crop, False)
        for row in Plot.out_plot:
            if check in row:
                row.remove(check)
            else:
                continue


#Plot1 = Plot()
#Plot1.CreatePlot(5, 3)
#Plot1.AddCrops("Carrot", 5)
#Plot1.AddCrops("Parsnip", 10)
#Plot1.DelCrops("Carrot")
#Plot1.Water()

#for row in Plot1.out_plot:
 #  for obj in row:
  #     print(obj.selecrop, obj.watered, sep =' ')

#for row in Plot1.out_plot:
# for obj in row:
#     print(obj.watered)

