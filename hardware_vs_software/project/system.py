from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware = []
    _software = []

    @staticmethod
    def find_hardware(name):
        hw: Hardware
        for hw in System._hardware:
            if hw.name == name:
                return hw

    @staticmethod
    def find_software(name):
        sf: Software
        for sf in System._software:
            if sf.name == name:
                return sf

    @staticmethod
    def register_software(hardware, software):
        try:
            hardware.install(software)
        except Exception as e:
            return str(e)
        System._software.append(software)

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.find_hardware(hardware_name)
        if hardware is None:
            return 'Hardware does not exist'
        return System.register_software(hardware, software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.find_hardware(hardware_name)
        if hardware is None:
            return 'Hardware does not exist'
        return System.register_software(hardware, software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        software = System.find_software(software_name)
        hardware = System.find_hardware(hardware_name)
        if software is None or hardware is None:
            return 'Some of the components do not exist'
        else:
            hardware.uninstall(software)
            System._software.remove(software)

    @staticmethod
    def analyze():
        result = ""
        sf: Software
        hw: Hardware
        hardware_count = len(System._hardware)
        software_count = len(System._software)
        used_memory, used_capacity, total_memory, total_capacity = 0, 0, 0, 0
        for sf in System._software:
            used_memory += sf.memory_consumption
            used_capacity += sf.capacity_consumption

        for hw in System._hardware:
            total_memory += hw.memory
            total_capacity += hw.capacity

        result += f'System Analysis\n'
        result += f'Hardware Components: {hardware_count}\n'
        result += f'Software Components: {software_count}\n'
        result += f'Total Operational Memory: {used_memory} / {total_memory}\n'
        result += f'Total Capacity Taken: {used_capacity} / {total_capacity}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for c in System._hardware:
            c: HeavyHardware
            s: LightSoftware
            mem_usage, cap_usage, expr_count, light_count = 0, 0, 0, 0
            components = []
            for s in c.software_components:
                components.append(s.name)
                mem_usage += s.memory_consumption
                cap_usage += s.capacity_consumption
                if s.type == 'Express':
                    expr_count += 1
                else:
                    light_count += 1
            if len(components) == 0:
                comps_list = None
            else:
                comps_list = ', '.join(components)
            result += f'Hardware Component - {c.name}\n'
            result += f'Express Software Components: {expr_count}\n'
            result += f'Light Software Components: {light_count}\n'
            result += f'Memory Usage: {mem_usage} / {c.memory}\n'
            result += f'Capacity Usage: {cap_usage} / {c.capacity}\n'
            result += f'Type: {c.type}\n'
            result += f'Software Components: {comps_list}'
        return result


