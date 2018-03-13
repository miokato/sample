class BMI:
    """
    Calculate BMI
    """
    def __init__(self):
        self.BMI = 22

    def calc_bmi(self, weight, height):
        """
        Calculate BMI
        :param (float) weight: kg
        :param (float) height: m
        :return (float) bmi:
        """
        return round(weight / (height ** 2), 2)

    def right_weight(self, height):
        """
        Calculate right weight
        :param (flaot) height:
        :return (float) right_weight:
        """
        return round((height ** 2) * self.BMI, 2)
