import func

menu = {
    'a': ('멜론 100', func.m100),
    'b': ('멜론 50', func.m50),
    'c': ('멜론 10', func.m10),
    'd': ('AI 추천 노래', func.m_random),
    'e': ('가수 이름 검색', lambda: func.search_singer(input("검색할 가수 이름: "))),
    'f': ('파일에 저장(멜론 100)', lambda: func.save_to_file("melon100.txt")),
    'g': ('원하는 만큼의 순위', func.m000),
    'q': ('종료', None)
}

def display_menu():
    print("\n=================")
    for key, (description, _) in menu.items():
        print(f"{key}. {description}")
    print("=================")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("메뉴 선택 (알파벳 입력): ").lower()
        if choice in menu:
            _, action = menu[choice]
            if action:
                action(menu[choice][0]) if choice in ['a', 'b', 'c', 'd', 'g'] else action()
            elif choice == 'q':
                print("프로그램을 종료합니다.")
                break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
