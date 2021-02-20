class Parking_Lot:
    def __init__(self):
        self.space = []

    def CreateParkingLot(self, size):

        for i in range(size):
            self.space.append([i + 1])
        print(f"Created a parking lot with {size} slots")

    def Activities(self, Statement):
        sub_statement = list(Statement.split())
        if sub_statement[0] == "park" and len(sub_statement) == 3:
            temp = "false"
            for i in range(len(self.space)):
                if len(self.space[i]) == 1:
                    self.space[i].append(sub_statement[1])
                    self.space[i].append(sub_statement[2])
                    print(f"Allocated slot number: {self.space[i][0]}")
                    temp = "true"
                    break
            if temp == "false":
                print("Parking lot is full")
        elif sub_statement[0] == "leave":
            target = (self.space[int(sub_statement[1]) - 1])
            if len(target) > 1:
                while len(target) != 1:
                    target.pop(1)
                print(f"Slot no {sub_statement[1]} is free")
            else:
                print(f"slot no {sub_statement[1]} is already empty")
        elif sub_statement[0] == "status":
            print("Slot No. Registration No Colour")
            for i in self.space:
                if len(i) == 3:
                    for j in i:
                        print(j, end=" ")
                    print()
        elif sub_statement[0] == "registration_numbers_for_cars_with_colour":
            if len(sub_statement) == 2:
                colour = sub_statement[1]
                arr = []
                for i in range(len(self.space)):
                    if colour in self.space[i]:
                        arr.append(self.space[i][1])
                for j in arr:
                    if j == arr[-1]:
                        print(j)
                    else:
                        print(j, end = (","))
        elif sub_statement[0] == "slot_numbers_for_cars_with_colour":
            if len(sub_statement) == 2:
                colour=sub_statement[1]
                arr = []
                for i in range(len(self.space)):
                    if colour in self.space[i]:
                        arr.append(self.space[i][0])
                for j in arr:
                    if j == arr[-1]:
                        print(j)
                    else:
                        print(j, end = (","))
        elif sub_statement[0] == "slot_number_for_registration_number":
            if len(sub_statement) == 2:
                for i in range(len(self.space)):
                    if sub_statement[1] in self.space[i]:
                        print(self.space[i][0])
                        break
                else:
                    print("Not Found")
