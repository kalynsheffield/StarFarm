from os.path import dirname, join
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export
from crops import Crop
from plots import Plot
class Farm():
    object = Crop()
    object2 = Plot()
    planted =[]
    amt_planted = []
    planted_index = 0
    season =""
    spring = ["Carrot", "Parsnip", "Potato", "Cauliflower", "Kale", "Garlic", "Rhubarb"]
    summer = ["Melon", "Radish", "Red Cabbage","Summer Squash", "Starfruit","Tomato" ]
    fall = ["Beet", "Broccoli","Pumpkin", "Yam", "Grape", "Bok Choy", "Artichoke", "Eggplant"]
    winter = ["Powdermelon"]

    
    def Error(self, wrongcrop):
        print(wrongcrop , "is not being planted in the correct season.")
        quit()

    def MatchSeason(self, selection):
         match selection:
            case "Spring":
                Farm.season ="Spring"
            case "Summer":
                Farm.season = "Summer"
            case "Fall":
                Farm.season = "Fall"
            case "Winter":
                Farm.season = "Winter"
            case _:
                print(selection, " is not an an accessible season.")
                quit()

    def interpret(self, model):
        for f in model.farms:
            self.MatchSeason(f.selection)
            for c in f.commands:
                if c.__class__.__name__ == "SeedCommand":
                    if Farm.season == "Spring":
                        if c.crop in Farm.spring:
                            new_crop = c.crop + " seed(s)"
                            Farm.object.addToList(new_crop, c.cropseeds)
                        else:
                            self.Error(c.crop)
                    elif Farm.season == "Summer":
                        if c.crop in Farm.summer:
                            new_crop = c.crop + " seed(s)"
                            Farm.object.addToList(new_crop, c.cropseeds)
                        else:
                            self.Error(c.crop)
                    elif Farm.season == "Fall":
                        if c.crop in Farm.fall:
                            new_crop = c.crop + " seed(s)"
                            Farm.object.addToList(new_crop, c.cropseeds)
                        else:
                            self.Error(c.crop)
                    else:
                        if c.crop in Farm.winter:
                            new_crop = c.crop + " seed(s)"
                            Farm.object.addToList(new_crop, c.cropseeds)
                        else:
                            self.Error(c.crop)
                elif c.__class__.__name__ == "GroundCommand":
                    Farm.object2.CreatePlot(c.rows, c.cols)
                
                elif c.__class__.__name__ == "FarmCommand":
                    if c.action == "Plant":
                        if Farm.object2.plot_hold > 0:
                            check = c.sepcrop + " seed(s)"
                            Farm.object.CheckList(check)
                            Farm.object2.AddCrops(c.sepcrop, c.seeds)
                            Farm.planted.append(c.sepcrop)
                            Farm.amt_planted.append(c.seeds)
                        else:
                            print("plot has not been created yet")
                            quit()
                    elif c.action == "Scythe":
                        check = 0
                        for row in Farm.object2.out_plot:
                            for obj in row:
                                if obj.selecrop == c.sepcrop:
                                    check += 1
                                else:
                                    continue
                        if check > 0:
                            #only EVEN NUMBER!!
                            times = int(c.seeds/2)
                            for i in range(times):
                                Farm.object2.DelCrops(c.sepcrop, c.seeds)
                            Farm.object.SubAmount(c.sepcrop, c.seeds)
                        else:
                            print(c.sepcrop, "has not been planted.")
                            quit()
                    
                        for item1, item2 in zip(Farm.planted, Farm.amt_planted):
                            if  item1 == c.sepcrop:
                                item2 -= c.seeds

                    elif c.action == "Collect":
                        print(model.name, "Farm Status:")
                        Farm.object.printList()
                        quit()
                    else:
                        Farm.object2.Water()
                        for item1, item2 in zip(Farm.planted, Farm.amt_planted):
                         Farm.object.Grown(item1, item2, Farm.planted_index)
                         Farm.planted_index += 1
                else:
                    quit()

def main(debug=False):

    this_folder = dirname(__file__)

    starfarm_mm = metamodel_from_file(join(this_folder, 'starfarm.tx'), debug=False)
    metamodel_export(starfarm_mm, join(this_folder, 'starfarm.dot'))


    starfarm_model = starfarm_mm.model_from_file(join(this_folder, 'trial1.sf'))
    model_export(starfarm_model, join(this_folder, 'trial1.dot'))

    farm = Farm()
    farm.interpret(starfarm_model)

if __name__ == "__main__":
    main()