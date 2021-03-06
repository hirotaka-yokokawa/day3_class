import unittest

from address_seacher import AddressSearcher


class TestAddressSearcher(unittest.TestCase):
    def test_岩手県八幡平市大更を郵便番号から取得できる(self):
        address_searcher = AddressSearcher()

        actual = address_searcher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)

    def test_東京都練馬区豊玉南を郵便番号から取得できる(self):
        address_searcher = AddressSearcher()

        actual = address_searcher.search(postal_code="1760014")

        self.assertEqual("東京都練馬区豊玉南", actual)

    def test_存在しない郵便番号を入力したらエラーメッセージを表示する(self):
        address_searcher = AddressSearcher()
        expected = "該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。"
        actual = address_searcher.search(postal_code="1234567")

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
