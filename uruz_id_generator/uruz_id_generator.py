# SPDX-License-Identifier: Uruz Open Commercial License (UOCL)-1.0
# Created: 2026-10-02
# Author: Uruz - Utku Ün (Kurt)
__version__ = "1.0.0"


from datetime import datetime
import uuid
import random


class UruzIDGenerator:
    """
    **UruzIDGenerator** sınıfı, farklı mantıklara dayalı
    benzersiz kimlik (ID) üretim yöntemleri sağlar.

    Bu sınıf, zaman damgası, hex tabanlı rastgele diziler, yalnızca harflerden
    veya yalnızca rakamlardan oluşan diziler gibi çeşitli ID üretim
    stratejilerini içerir. Ayrıca, birden fazla ID parçasını birleştirerek
    daha güçlü ve modüler kimlikler oluşturma imkanı sunar.

    Attributes:
        None

    Methods:
        - @staticmethod, **combine_ids(...)**:
            Verilen ID parçalarını birleştirerek yeni bir ID üretir.

        - @staticmethod, **generate_timestamp()**:
            YYYYMMDDHHMMSS formatında zaman damgası üretir.

        - @staticmethod, **generate_randomcharacterarray(...)**:
            Hex tabanlı rastgele karakter dizisi üretir.

        - @staticmethod, **generate_randommixedletters(...)**:
            Sadece harflerden oluşan rastgele dizi üretir.

        - @staticmethod, **generate_randomnumericarray(...)**:
            Sadece rakamlardan oluşan rastgele dizi üretir.
    """


    @staticmethod
    def combine_ids(*parts: str, separator: str = "-") -> str:
        """
        Verilen ID parçalarını birleştirerek yeni bir ID üretir.

        Args:
            *parts (str): Birleştirilecek ID parçaları.
            seperator (str): Bölümler arasındaki ayraç.
                Varsayılan değer: '-'
        
        Returns:
            str: birleştirilmiş ID.
        
        Examples:
        ```
        timestamp_id = UruzIDGenerator().generate_timestamp()
        hex8_id = UruzIDGenerator().generate_randomcharacterarray(size=8)
        combined_id_1 = UruzIDGenerator().combine_ids(timestamp_id, hex8_id, separator="-")
        print(combined_id_1)
        # output: 20261006124127-e9ade109

        mixedletters_id = UruzIDGenerator().generate_randommixedletters(size=8)
        numeric_id = UruzIDGenerator().generate_randomnumericarray(size=8)
        combined_id_2 = UruzIDGenerator.combine_ids(mixedletters_id, numeric_id, separator=":")
        print(combined_id_2)
        # output: MNOUDPZA:18230553
        ```
        """
        return separator.join(parts)


    @staticmethod
    def generate_timestamp() -> str:
        """"
        YYYYMMDDHHMMSS formatında zaman damgası üretir

        Returns:
            str: YYYYMMDDHHMMSS formatında zaman damgası.

        Examples:
        ```
        timestamp_id = UruzIDGenerator().generate_timestamp()
        print(timestamp_id)
        # output: 20261006120314
        ```
        """
        return datetime.now().strftime("%Y%m%d%H%M%S")


    @staticmethod
    def generate_randomcharacterarray(size: int = 8) -> str:
        """
        Hex tabanlı rastgele bir karakter dizisi üretir.
        
        Args:
            size (int): kaç karakterlik rastgele bir dizi istendiğini belirtir.
                Varsayılan değer: 8

        Returns:
            str: X karakterlik rastgele bir karakter dizisi.

        Examples:
        ```
        hex8_id = UruzIDGenerator().generate_randomcharacterarray(size=8)
        print(hex8_id)
        # output: a1f626ca
        ```
        """
        return uuid.uuid4().hex[:size]


    @staticmethod
    def generate_randommixedletters(size: int = 8) -> str:
        """
        Sadece harflerden oluşan rastgele bir karakter dizisi üretir.

        Args:
            size (int): kaç karakterlik rastgele bir dizi istendiğini belirtir.
                Varsayılan değer: 8

        Returns:
            str: X karakterlik rastgele bir karakter dizisi.

        Examples:
        ```
        mixedletters_id = UruzIDGenerator().generate_randommixedletters(size=8)
        print(mixedletters_id)
        # output: UMRRTEMG
        ```
        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(letters) for _ in range(size))


    @staticmethod
    def generate_randomnumericarray(size: int = 8) -> str:
        """
        Sadece rakamlardan oluşan rastgele bir karakter dizisi üretir.

        Args:
            size (int): kaç karakterlik rastgele bir dizi istendiğini belirtir.
                Varsayılan değer: 8

        Returns:
            str: X karakterlik rastgele bir karakter dizisi.

        Examples:
        ```
        numeric_id = UruzIDGenerator().generate_randomnumericarray(size=8)
        print(numeric_id)
        # output: 55822974
        ```
        """
        numbers = "0123456789"
        return ''.join(random.choice(numbers) for _ in range(size))


# Modül için uygulamalı test örnekleri.
# Bu kod bloğu, modül doğrudan çalıştırılmadığı sürece çalışmaz. 
if __name__ == "__main__":
    timestamp_id = UruzIDGenerator().generate_timestamp()
    print(timestamp_id)

    hex8_id = UruzIDGenerator().generate_randomcharacterarray(size=8)
    print(hex8_id)

    mixedletters_id = UruzIDGenerator().generate_randommixedletters(size=8)
    print(mixedletters_id)

    numeric_id = UruzIDGenerator().generate_randomnumericarray(size=8)
    print(numeric_id)

    combined_id_1 = UruzIDGenerator().combine_ids(timestamp_id, hex8_id, separator="-")
    print(combined_id_1)

    combined_id_2 = UruzIDGenerator.combine_ids(mixedletters_id, numeric_id, separator=":")
    print(combined_id_2)
