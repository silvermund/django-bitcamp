class Member(object):

    id = ''
    pw = ''
    name = ''
    email = ''

    def join(self):
        pass

    def login(self):
        pass

    def mypage(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    @staticmethod
    def main():
        member = Member()
        while 1:
            menu = input('0.Exit 1.회원가입 2.로그인 3.마이페이지 4.회원정보수정 5.회원탈퇴')
            if menu == '0':
                break
            elif menu == '1':
                member.id = ''
                member.pw = ''
                member.name = ''
                member.email = ''
                member.join()
            elif menu == '2':
                member.id = ''
                member.pw = ''
                member.login()
            elif menu == '3':
                member.id = ''
                member.mypage()
            elif menu == '4':
                member.id = ''
                member.pw = ''
                member.name = ''
                member.email = ''
                member.update()
            else:
                print('Wrong Number')
                continue

Member.main()
