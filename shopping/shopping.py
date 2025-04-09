def calculate_total_with_tax(items, tax_rate=0.07):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return round(total, 2)

if __name__ == "__main__":
    shopping_list = [12.99, 5.49, 3.75, 9.20]
    total = calculate_total_with_tax(shopping_list)
    print(f"Total with 7% tax: ${total}")
