class CommandSubmarine:
    def get_order(order):
        return order.split(" ")

    def apply_order(orders):
        x = 0
        depth = 0
        for order in orders:
            real_order = CommandSubmarine.get_order(order)
            if real_order[0] == "forward":
                x += int(real_order[1])
            elif real_order[0] == "down":
                depth += int(real_order[1])
            elif real_order[0] == "up":
                depth -= int(real_order[1])
        return [x, depth]

    def apply_real_order(orders):
        x = 0
        depth = 0
        aim = 0
        for order in orders:
            real_order = CommandSubmarine.get_order(order)
            if real_order[0] == "forward":
                x += int(real_order[1])
                depth += int(real_order[1]) * aim
            elif real_order[0] == "down":
                aim += int(real_order[1])
            elif real_order[0] == "up":
                aim -= int(real_order[1])
        return [x, depth, aim]

    def get_submarine_position(postion):
        return postion[0] * postion[1]
