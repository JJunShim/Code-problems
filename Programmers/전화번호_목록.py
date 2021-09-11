def solution(phone_book: list) -> bool:
    phone_book.sort()
    for i, n in enumerate(phone_book[1:]):
        if n.startswith(phone_book[i]):
            return False
    return True
