class Bank:
    @property
    def passward(self):
        return '123'
andy = Bank()
print(andy.passward)
andy.passward = '456'