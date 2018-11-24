from address_seacher import AddressSearcher


def main():
    # ユーザーからの郵便番号を受け取る｡ ok
    # 郵便番号を使って地名をとってくる｡
    # 地名をprintする｡

    postal_code = input("郵便番号を入力してください :")

    address_searcher = AddressSearcher()

    location = address_searcher.search(postal_code)

    print(location)


if __name__ == "__main__":
    main()
