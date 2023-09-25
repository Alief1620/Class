class BankAccount:
    def __init__(self, card_number, user_name_card, balance):
        self.card_number = self.is_valid_card_number(card_number)
        self.user_name_card = self.is_valid_user_name_card(user_name_card)
        self.balance = self.is_valid_balance(balance)


    def is_valid_card_number(self, card_number):
        if len(card_number) != 16:
            raise ValueError('The card number must be 16 digits')
        return card_number


    def is_valid_user_name_card(self, user_name_card):
        if not user_name_card:
            raise ValueError("The card user's name cannot be empty")
        return user_name_card

    def is_valid_balance(self, balance):
        if balance < 0:
            raise ValueError('Balance must not be negative')
        return balance

    def __str__(self):
        return f'Score: {self.card_number}, Name: {self.user_name_card}, Balance: {self.balance}'

    # пополнение карточки
    def replenishment_of_the_card(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Replenished - {amount} PLN. Current balance: {self.balance} PLN')
        else:
            print('The amount paid must be greater than zero') #Выплачиваемая сумма должна быть больше нуля

    # снятие средств
    def withdrawal_of_funds(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Paid - {amount} PLN. Current balance: {self.balance} PLN')
        elif amount <= 0:
            print('Amount to withdraw must be greater than zero') #сумма должна быть больше 0
        else:
            print('Insufficient funds on the card') #недостаточно средств на карте


# Сберегательный счет
class SavingsAccount(BankAccount):

    def __init__(self, card_number, user_name_card, balance, interest_rate):
        super().__init__(card_number, user_name_card, balance)
        self.interest_rate = interest_rate

    # Добавление процентной ставки
    def add_interest_rate(self):
        interest = self.balance * (self.interest_rate / 100)
        self.replenishment_of_the_card(interest)
        print(f'Interest added: {interest} PLN') #ставка добавлена


# добавление и удаление счетов
class Bank:
    def __init__(self):
        self.scores = {}

    # добавление счета
    def create_score(self, card_number, user_name_card, balance):
        new_score = BankAccount(card_number, user_name_card, balance)
        self.scores[card_number] = new_score
        print(f'Add new score: {card_number}')

    # удаление счета
    def delete_scores(self, card_number):
        if card_number in self.scores:
            del self.scores[card_number]
            print(f'Scores delete: {card_number}')
        else:
            print(f'Scores not found: {card_number}')

    #информация о выводе средств
    def withdraw_scores_information(self, card_number):
        if card_number in self.scores:
            scores = self.scores[card_number]
            print(scores)
        else:
            print(f'Score not found: {card_number}') #счета не найдено

    # перевод денежных средств
    def remittance_funds(self, from_card_number, to_card_number, amount):
        if from_card_number in self.scores and to_card_number in self.scores:
            from_account = self.scores[from_card_number]
            to_account = self.scores[to_card_number]

            if from_account.balance >= amount:
                from_account.withdrawal_of_funds(amount)
                to_account.replenishment_of_the_card(amount)
                print(f"Funds remittance from {from_card_number} to {to_card_number}: {amount} PLN")
            else:
                print('Insufficient funds to make the remittance')  # недостаточно средств для осуществления денежного перевода


bank = Bank()
bank.create_score('1234545632147856', 'Sara Hive', 100000)
bank.create_score('5432145879563214', 'Varia Ger', 150000)
bank.withdraw_scores_information('1234545632147856')
bank.withdraw_scores_information('5432145879563214')
bank.remittance_funds('1234545632147856', '5432145879563214', 15000)
bank.withdraw_scores_information('1234545632147856')
bank.withdraw_scores_information('5432145879563214')
bank.delete_scores('5432145879563214')

#second example
bank.create_score('1458796325874102', 'Katya Des', 1000)
bank.create_score('9685741236985026', 'Denis Van', 500)
bank.withdraw_scores_information('1458796325874102')
bank.withdraw_scores_information('9685741236985026')
bank.remittance_funds('1458796325874102', '9685741236985026', 500)
bank.withdraw_scores_information('1458796325874102')
bank.withdraw_scores_information('9685741236985026')
bank.delete_scores('1458796325874102')

