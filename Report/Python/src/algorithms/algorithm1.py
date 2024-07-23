class Algorithm1:
    def __init__(self, param1: int, param2: str):
        """
        Bu fonksiyon Algorithm1 sınıfı çağrıldığında direk olarak çalıştırılıp, gerekli olan parametrelerin değerlerini
        atacayacaktır

        :param param1:
        :param param2:
        """
        self.param1 = param1

    @staticmethod
    def static_method() -> int:
        """
        Static methodlar sınıftan herhangi bir değer veya fonksiyon almaz, işini yapar sadece diğer fonksiyonlarla
        bağımlılığı yoktur
        :return:
        """
        return 1

    def control_parameter(self):
        """
        Bu fonksiyon param1 parametreesinin aralığını kontrol eder
        :return:
        """
        if self.param1 == 0:
            raise ValueError("Param1 0'dan farklı olması lazım")
        else:
            return 2
