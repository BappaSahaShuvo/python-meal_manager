# Meal Manager - Single File Python Version (No Database)
# -------------------------------------------------------
# Console-based application inspired by the original C# project.

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.meals = 0
        self.deposit = 0
        self.expense = 0

    def __str__(self):
        return f"[{self.member_id}] {self.name} | Meals: {self.meals}, Deposit: {self.deposit}, Expense: {self.expense}"


class MealManager:
    def __init__(self):
        self.members = {}
        self.expenses = []
        self.next_member_id = 1

    # ---------- Member ----------
    def add_member(self, name):
        member = Member(self.next_member_id, name)
        self.members[self.next_member_id] = member
        self.next_member_id += 1
        print(f"✅ Member '{name}' added successfully!")

    def view_members(self):
        if not self.members:
            print("❌ No members available.")
        else:
            for m in self.members.values():
                print(m)

    # ---------- Meal ----------
    def add_meal(self, member_id, count):
        if member_id in self.members:
            self.members[member_id].meals += count
            print(f"✅ Added {count} meal(s) for {self.members[member_id].name}")
        else:
            print("❌ Member not found!")

    # ---------- Deposit ----------
    def add_deposit(self, member_id, amount):
        if member_id in self.members:
            self.members[member_id].deposit += amount
            print(f"✅ {amount} deposited for {self.members[member_id].name}")
        else:
            print("❌ Member not found!")

    # ---------- Expense ----------
    def add_expense(self, description, amount):
        self.expenses.append((description, amount))
        print(f"✅ Expense added: {description} - {amount}")

    # ---------- Reports ----------
    def monthly_report(self):
        total_meals = sum(m.meals for m in self.members.values())
        total_deposit = sum(m.deposit for m in self.members.values())
        total_expense = sum(amount for _, amount in self.expenses)

        meal_rate = (total_expense / total_meals) if total_meals > 0 else 0

        print("\n📊 Monthly Report")
        print("-" * 40)
        print(f"Total Meals   : {total_meals}")
        print(f"Total Deposit : {total_deposit}")
        print(f"Total Expense : {total_expense}")
        print(f"Meal Rate     : {meal_rate:.2f}")
        print("-" * 40)

        for m in self.members.values():
            meal_cost = m.meals * meal_rate
            balance = m.deposit - meal_cost
            print(f"{m.name}: Meals={m.meals}, Deposit={m.deposit}, Cost={meal_cost:.2f}, Balance={balance:.2f}")
        print("-" * 40)


# ---------- Main Program ----------
def main():
    manager = MealManager()

    while True:
        print("\n====== Meal Manager ======")
        print("1. Add Member")
        print("2. View Members")
        print("3. Add Meal")
        print("4. Add Deposit")
        print("5. Add Expense")
        print("6. Monthly Report")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter member name: ")
            manager.add_member(name)

        elif choice == "2":
            manager.view_members()

        elif choice == "3":
            try:
                member_id = int(input("Enter member ID: "))
                count = int(input("Enter meal count: "))
                manager.add_meal(member_id, count)
            except ValueError:
                print("❌ Invalid input!")

        elif choice == "4":
            try:
                member_id = int(input("Enter member ID: "))
                amount = float(input("Enter deposit amount: "))
                manager.add_deposit(member_id, amount)
            except ValueError:
                print("❌ Invalid input!")

        elif choice == "5":
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter expense amount: "))
                manager.add_expense(description, amount)
            except ValueError:
                print("❌ Invalid amount!")

        elif choice == "6":
            manager.monthly_report()

        elif choice == "0":
            print("👋 Exiting Meal Manager...")
            break

        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
