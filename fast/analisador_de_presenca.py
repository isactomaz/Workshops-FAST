from typing import List


class AnalisadorDePresenca:
    def __init__(self, atas: List[str]):
        self.__atas = atas

    def ColaboradoresQueViram2WorkshopsSeguidos(self) -> List[str]:
        workshops = list(map(lambda ata: set(ata.split(" ")), self.__atas))
        result = []
        for index in range(len(self.__atas) - 1):
            intersection = workshops[index].intersection(workshops[index + 1])
            if intersection != set():
                result.extend(intersection)
        return sorted(set(result))
