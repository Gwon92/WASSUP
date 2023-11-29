#!/usr/bin/env python
# coding: utf-8

# In[15]:


phone = {'홍길동':'010-123-4567'}

while True:
    print("""
    ----------------------------------------------
    1 : 연락처 추가
    2 : 연락처 전체 보기
    3 : 연락처 검색
    4 : 연락처 수정
    5 : 연락처 삭제
    6 : 프로그램 종료
    -----------------------------------------------
    """)

    choice = input("원하는 기능의 번호를 입력하세요.")

    if choice == "1":
        name = input("이름 입력:")
        number = input("번호 입력:")
        phone[name] = number
        print("\n***전화번호가 추가되었습니다***")
    elif choice == "2":
        print("\n***번호 리스트***")
        for key,value in phone.items():
            print("이름:"+key)
            print("번호:"+value)
    elif choice == "3":
        name = input("이름 입력:")
        if name in phone.keys():
            print(f"\n{name}님의 전화번호는 {phone[name]}입니다.")
        else:
            print("\n존재하지 않는 이름입니다.")
    elif choice == "4":
        name = input("이름 입력:")
        number = input("새로운 번호 입력:")
        if name in phone.keys():
            phone[name] = number
            print("\n***번호가 업데이트 되었습니다.***")
        else:
            print("\n존재하지 않는 이름입니다.")
    elif choice == "5":
        name = input("이름 입력:")
        if name in phone.keys():
            del phone[name]
            print("\n***삭제가 완료되었습니다***")
        else:
            print("\n존재하지 않는 이름입니다.")
    elif choice == "6":
        print("***종료합니다.***")
        break

