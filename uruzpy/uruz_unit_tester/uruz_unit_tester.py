# SPDX-License-Identifier: Uruz Open Commercial License (UOCL)-1.0
# Created: 2026-10-06
# Author: Uruz - Utku Ün (Kurt)
__version__ = "1.0.0"


from status_type import StatusType


class UruzUnitTester:
    """
    UruzUnitTest sınıfı, basit test ve sonuç raporlama için bir temel sağlar.

    Bu sınıf, yapılan testlerin sonuçlarını bir listeye kaydeder ve
    bu liste üzerinden özet, istatistik ve raporlama işlemleri yapılmasına imkan tanır.

    Methods:
        - __str__()

        - @instancemethod, calculate_stats(self, ...): 
            - @capsulemethod, 
        - 

        - 
    """


    def __init__(self):
        self.output_list = []  # çıktı listesi


    def __str__(self):
        """
        Sınıf örneği yazdırıldığında test sonuçlarını ve istatistikleri
        okunabilir bir formatta döndürür.

        Returns:
            str: Test sonuçlarınının ve başarı/başarısızlık oranlarının
                özet çıktısı.
        
        Examples:
        ```
        ...
        # output:
        ```
        """
        separator = f"\n{79 * "-"}"

        indexed_output_list = self._index_output_list()
        summary_all = self._create_summary(result_list=indexed_output_list) # test özetleri
        
        success_list = self._filter_output_list(
            indexed_list=indexed_output_list,
            status=StatusType.SUCCESS
        )
        summary_success = self._create_summary(success_list) # başarı özetleri
        
        failures_list = self._filter_output_list(
            indexed_list=indexed_output_list,
            status=StatusType.FAILURE
        )
        summary_failure = self._create_summary(failures_list) # başarısızlık özetleri
        
        stats = self._claculate_stats()  # istatistikler
        return (
            f"\n# Summary\n"
            f"{summary_all}"
            f"{separator}"
            f"\n# Success\n"
            f"{summary_success}"
            f"{separator}"
            f"\n# Failures\n"
            f"{summary_failure}"
            f"{separator}"
            f"\n# Result\n"
            f"Total: {stats['total']} | "
            f"Succes: {stats['ok']} | "
            f"Failure: {stats['fail']} | "
            f"Success Rate: {stats['success_rate']:.2f}% | "
            f"Failure Rate: {stats['failure_rate']:.2f}%"
            f"{separator}"
        )


    ### HELPER METHODS FOR REPORTING
    def _index_output_list(self) -> list[tuple[StatusType, str]]:
        """
        Çıktı listesindeki test sonuçlarını indeksleyerek yeni bir liste
        döndürür.

        Her bir test sonucu için sıra numarası (index), durum (`StatusType`)
        ve açıklama mesajı bir tuple olarak oluşturulur. Aynı mesaj birden
        fazla kez geçse bile 'enumerate' sayesinde benzersiz indeksler atanır.

        Returns:
            list[tuple[int, StatusType, str]]: İndekslenmiş test sonuçlarının
                listesi. Her eleman `(index, status, message)` formatındadır.

        Examples:
        ```
        >>> unit_tester = UruzUnitTester()
        >>> unit_tester.output_list.append((StatusType.SUCCESS, "Test successed."))
        >>> unit_tester.output_list.append((StatusType.FAILURE, "Test failured."))
        >>> indexed_output_list = unit_tester._index_outpulist()
        >>> print(indexed_output_list)
        [(1, StatusType.SUCCESS, 'Test success.'),
         (2, StatusType.FAILURE, 'Test failured.')]
        ```
        """
        return [
            # tuple = (test index - status value - message)
            ( i+1, s, msg)
            # enumerate: aynı değer birden fazla olduğunda,
            # aynı indeksi kullanmaz.
            for i, (s, msg) in enumerate(self.output_list)
        ]


    
    @staticmethod
    def _filter_output_list(
        indexed_list: list[tuple[int, StatusType, str]],
        status: StatusType
    ) -> list[tuple[int, StatusType, str]]:
        """
        İndesklenmiş çıktı listesindeki test sonuçlarını verilen statüye göre
        filtreler.

        Args:
            indexed_list (list[tuple[int, StatusType, str]): İndekslenmiş test
                sonuçlarının listesi. Her eleman `(index, status, message)`
                formatındadır.
            status (StatusType): Filtrelenecek durum
            (örneğin `StatusType.SUCCESS` veya `StatusType.FAILURE`).

        Results:
            list[tuple[int, StatusType, str]]: Belirtilen statüye sahip test
            sonuçlarının listesi. Her eleman `(index, status, message)`
            formatındadır.

        Examples:
        ```
        >>> unit_tester = UruzUnitTester()
        >>> unit_tester.output_list.append((StatusType.SUCCESS, "Test successed."))
        >>> unit_tester.output_list.append((StatusType.FAILURE, "Test failured."))
        >>> indexed_output_list = unit_tester._index_outpulist()
        >>> success_result_list = unit_tester._filter_output_list(indexed_output_list, StatusType.SUCCESS)
        >>> print(success_result_list)
        [(1, StatusType.SUCCESS, 'Test successed.')]
        ```
        """
        return list(
            # tuple = (test index - status value - message)
            (i, s, msg)
            for i, s, msg in indexed_list if s == status
        )


    @staticmethod
    def _create_summary(
        result_list: list[tuple[int, StatusType, str]]
        ) -> str:
        """
        indekslenmiş test sonuçlarını özetleyen bir string döndürür.

        Her bir test sonucu için sıra numarası (index), durum (`StatusType`)
        ve açıklama mesajı bir satır halinde birleştirilir. Sonuçlar satır
        satır birleştirilerek okunabilir bir özet oluşturulur. 

        Args:
            result_list (list[tuple[int, StatusType, str]]): İndekslenmiş test
                sonuçlarının listesi. Her eleman `(index, status, message)`
                formatındadır. 

        Returns:
            str: Test sonuçlarının özet çıktısı. Her satırda
            'index satatus message' formatı bulunur.

        Examples:
        ```
        >>> unit_tester = UruzUnitTester()
        >>> unit_tester.output_list.append((StatusType.SUCCESS, "Test successed."))
        >>> unit_tester.output_list.append((StatusType.FAILURE, "Test failured."))
        >>> indexed_output_list = unit_tester._index_outpulist()
        >>> summary = unit_tester._create_summary(indexed_output_list)
        >>> print(summary)
        1 [OK] Test successed.
        2 [FAIL] Test failured.
        ```
        """         
        return "\n".join(
            # str = "test index - status value - message"
            f"{index} {status.value} {msg}"
            for index, status, msg in result_list
        )


    def _claculate_stats(self) -> dict:
        """
        Çıktı listesindeki test sonuçlarına göre istatistik hesaplar.

        Toplam test sayısını, başarılı başarısız test sayısını,
        ayrıca başarı ve hata oranlarını yüzdesel olarak döndürür.

        Returns:
            dict: İstatistikleri içeren sözlük. Anahtarlar: 
                - "total" (int):
                - "ok" (int):
                - "fail" (int): 
                - "success_rate" (float): Başarı oranı (%)
                - "failure_rate" (float): Hata oranı (%).
        
        Examples:
        ```
        >>> unit_tester = UruzUnitTester()
        >>> unit_tester.output_list.append((StatusType.SUCCESS, "Test successed."))
        >>> unit_tester.output_list.append((StatusType.FAILURE, "Test failured."))
        >>> stats = unit_tester._claculate_stats()
        >>> print(stats)
        {'total': 2, 'ok': 1, "fail": 1, 'success_rate': 50.0, 'failure_rate': 50.0}
        ```
        """


        def calculate_rate(numerator: int, denominator: int) -> float:
            """
            Oran hesaplayan yardımcı fonksiyon.

            Args:
                numerator (int): Pay
                    (örneğin başarılı veya hatalı testlerin sayısı).
                denominator (int): Payda (toplam test sayısı).

            Returns:
                float: Oran yüzdesi. Eğer payda sıfırsa 0 döner.
            
            Examples:
            ```
            >>> calculate_rate(3, 5)
            60.0
            >>> calculate_rate(0, 0)
            0 
            ```
            """
            return numerator / denominator * 100 if denominator > 0 else 0


        total = len(self.output_list)
        ok = sum(
            1 for status, _ in self.output_list if status == StatusType.SUCCESS
        )
        fail = total - ok  
        return {
            "total": total,  # toplam test sayısı
            "ok": ok,  # başarılı test sayısı
            "fail": fail,  # başarısız test sayısı 
            "success_rate": calculate_rate(numerator=ok, denominator=total),  # doğruluk oranı
            "failure_rate": calculate_rate(numerator=fail, denominator=total)  # hata oranı 
        }


    def _analyze_and_append_status(self, boolean: bool, msg: str) -> None:
        """
        Koşulu değerlendirir, sonucu bir `tuple` olarak oluşturur ve
        çıktı listesine ekler.

        Args:
            boolean (bool): Test edilecek koşulun mantıksal sonucu.
            message (str): Test açıklaması.

        Returns:
            None

        Examples:
        ```
        >>> unit_tester = UruzUnitTester()
        >>> unit_tester._analyze_and_append_status(True, "The condition is true.")
        >>> print(unit_tester.output_list)
        [(StatusType.SUCCESS, 'The condition is true.')]
        ```
        """
        result = (
            StatusType.SUCCESS, msg
        ) if boolean else (
            StatusType.FAILURE, msg
        )
        self.output_list.append(result)


    ### SUCCESS and FAILURE TESTS  ###
    def assert_equal(self, value, expected, message: str) -> None:
        """
        Elde edilen değer ve beklenen değerin eşit olup olmadığını
        test eder.
         
        Sonucu değerlendirir ve çıktı listesine ekler.

        Args:
            value: Test edilecek değer.
            expected: Beklenen değer.
            message (str): Test açıklaması.

        Returns:
            None
        
        Examples:
        ```
        >>> unit_tester = UruzUnitTester()
        >>> unit_tester.assert_equal(5, 5, "The obtained value is equal to the expected value (5).")
        >>> print(unit_tester.output_list)
        [(StatusType.SUCCESS, "The obtained value is equal to the expected value (5).")]
        >>> print(unit_tester)
        # Summary
        1 [OK] The obtained value is equal to the expected value (5).
        -------------------------------------------------------------------------------
        # Success
        1 [OK] The obtained value is equal to the expected value (5).
        -------------------------------------------------------------------------------
        # Failures
        None
        -------------------------------------------------------------------------------
        # Result
        Total: 1 | Succes: 1 | Failure: 0 | Success Rate: 100.00% | Failure Rate: 0.00%
        -------------------------------------------------------------------------------
        ```
        """
        condition = value == expected
        self._analyze_and_append_status(boolean=condition, msg=message)


    def assert_true(self, condition, message: str) -> None:
        """
        Bir koşulun doğru olup olmadığını test eder.

        Sonucu değerlendirir ve çıktı listesine ekler.

        Args:
            condition: Test edilecek koşul.
            message (str): Test açıklaması.

        Examples:
        ```
        >>> unit_tester = UruzUnitTester()
        >>> unit_tester.assert_true("abc".isalpha(), "The obtained value consists solely of letters.")
        >>> unit_tester.assert_true("abc-123".isalpha(), "The obtained value consists solely of letters.")
        >>> print(unit_tester.output_list)
        [(
        StatusType.SUCCESS, 'The obtained value consists solely of letters.',
        StatusType.FAILURE, 'The obtained value consists solely of letters.'
        )]
        >>> print(unit_tester)
        # Summary
        1 [OK] The obtained value consists solely of letters.
        2 [FAIL] 'The obtained value consists solely of letters.'
        -------------------------------------------------------------------------------
        # Success
        1 [OK] The obtained value consists solely of letters.
        -------------------------------------------------------------------------------
        # Failures
        2 [FAIL] 'The obtained value consists solely of letters.'
        -------------------------------------------------------------------------------
        # Result
        Total: 2 | Succes: 1 | Failure: 1 | Success Rate: 50.00% | Failure Rate: 50.00%
        -------------------------------------------------------------------------------
        ```
        """
        self._analyze_and_append_status(boolean=condition, msg=message)


# Modül için uygulamalı test örnekleri.
# Bu kod bloğu, modül doğrudan çalıştırılmadığı sürece çalışmaz. 
if __name__ == "__main__":
    unit_tester = UruzUnitTester()

    # success tests
    # 1
    unit_tester.assert_equal(value=24, expected=24, message="'x=24', x = 24")
    # failure tests
    # 2
    unit_tester.assert_equal(value=23, expected=24, message="'x=23', x = 24")

    # success tests
    # 3
    unit_tester.assert_true(
        condition="24".isdigit(),
        message="'24' consists solely of numeric characters."
        )
    # 4
    unit_tester.assert_true("Kurt".isalpha(), message="'Kurt' consists solely of text characters.")
    # failure tests
    # 5
    unit_tester.assert_true(
        condition="Kurt-24".isalpha() or "Kurt-24".isdigit(),
        message="'Kurt-24' consists solely of numeric or text characters."
    )

    print(unit_tester)

    # output:
    """
    # Summary
    1 [OK] 'x=24', x = 24
    2 [FAIL] 'x=23', x = 24
    3 [OK] '24' consists solely of numeric characters.
    4 [OK] 'Kurt' consists solely of text characters.
    5 [FAIL] 'Kurt-24' consists solely of numeric or text characters.
    -------------------------------------------------------------------------------
    # Success
    1 [OK] 'x=24', x = 24
    3 [OK] '24' consists solely of numeric characters.
    4 [OK] 'Kurt' consists solely of text characters.
    -------------------------------------------------------------------------------
    # Failures
    2 [FAIL] 'x=23', x = 24
    5 [FAIL] 'Kurt-24' consists solely of numeric or text characters.
    -------------------------------------------------------------------------------
    # Result
    Total: 5 | Succes: 3 | Failure: 2 | Success Rate: 60.00% | Failure Rate: 40.00%
    -------------------------------------------------------------------------------
    """
