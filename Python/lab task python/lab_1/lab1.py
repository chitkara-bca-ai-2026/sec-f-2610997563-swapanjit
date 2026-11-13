tuition_fee=int(input("Enter tuition fee: "))
lab_fee=int(input("Enter lab fee: "))
library_fee=int(input("Enter library fee: "))
exam_fee=int(input("Enter exam fee: "))
discount_amount=int(input("Enter discount amount"))
total_fee=tuition_fee+lab_fee+library_fee+exam_fee
fee_after_discount=total_fee-discount_amount
annual_fee=2*fee_after_discount
monthly_installment=annual_fee/12 
print("\n-------FEE DETAILS-------")
print(f"Tuition Fee        : {tuition_fee:.1f}")
print(f"Lab Fee            : {lab_fee:.1f}")
print(f"Library fee        : {library_fee:.1f}")
print(f"Exam Fee           : {exam_fee:.1f}")
print(f"Total Fee          : {total_fee:.1f}")
print(f"Discount           : {discount_amount}")
print(f"Fee after Discount : {fee_after_discount:.1f}")
print(f"Annual Fee         : {annual_fee:.1f}")
print(f"Monthly Installment: {monthly_installment:.1f}")
