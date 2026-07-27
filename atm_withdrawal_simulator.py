balance = 500.0

withdrawal_amount = float(input("Enter withdrawal amount: "))

new_balance = balance - withdrawal_amount

if withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0.")
elif withdrawal_amount < balance:
    print(f"Withdrawal successful. New balance is: R{new_balance:.2f}")
elif withdrawal_amount == balance:
    print("Withdrawal successful. Your account balance is now zero.")
else:
    print("Insufficient funds. Withdrawal failed.")