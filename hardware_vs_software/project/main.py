
from system import System


def zero_test():
    System.register_power_hardware("HDD", 200, 200)
    System.register_heavy_hardware("SSD", 400, 400)
    print(System.analyze())
    System.register_light_software("HDD", "Test", 0, 10)
    print(System.register_express_software("HDD", "Test2", 100, 100))
    System.register_express_software("HDD", "Test3", 50, 100)
    System.register_light_software("SSD", "Windows", 20, 50)
    System.register_express_software("SSD", "Linux", 50, 100)
    System.register_light_software("SSD", "Unix", 20, 50)
    print(System.analyze())
    System.release_software_component("SSD", "Linux")
    print(System.system_split())



# def test1():
#     System.register_power_hardware('phard', 100, 100)
#     System.register_light_software('phard', 'soft', 1, 1)
#     print(System.release_software_component('phard', 'soft'))
#
#
# def test2():
#     System.register_heavy_hardware('heavy', 1000, 1000)
#     print(System.register_light_software('heavy', 'lightSoft', 100000, 1))
#     print('system soft', System._software)
#     print('system hard', System._hardware)
#     print('system hard comps', System._hardware[0].software_components)


if __name__ == "__main__":
    zero_test()