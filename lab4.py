class Product:
    def __init__(self, name, price, popularity):
        self.name = name
        self.price = price  # Fixed typo (was 'prize')
        self.popularity = popularity

    def __repr__(self):   
        return f"{self.name} - Price: ₹{self.price}, Popularity: {self.popularity}"        

# Merge Sort Algorithm
def merge_sort(products, key):
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left_half = merge_sort(products[:mid], key)
    right_half = merge_sort(products[mid:], key)
    return merge(left_half, right_half, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key == 'price':  # Ascending order
            condition = left[i].price < right[j].price
        elif key == 'popularity':  # Descending order
            condition = left[i].popularity > right[j].popularity
        else:  # Alphabetical order
            condition = left[i].name.lower() < right[j].name.lower()

        if condition:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])    
    return sorted_list 

# Sample Products
products = [
    Product("Lappy", 1000, 90),
    Product("MobilePhone", 500, 95),
    Product("Headphones", 100, 80),
    Product("Keyboard", 50, 85),
    Product("Monitor", 300, 88)
]

def main():
    while True:
        print('\nSort products by:')
        print('1. Price (Lowest to Highest)')
        print('2. Popularity (Most Trending)')
        print('3. Name (A to Z)')
        print('4. Exit')
        choice = input("Enter your choice: ")

        if choice == '1':
            sorted_products = merge_sort(products, 'price')
        elif choice == '2':
            sorted_products = merge_sort(products, 'popularity')  # Fixed mistake
        elif choice == '3':
            sorted_products = merge_sort(products, 'name')
        elif choice == '4':
            print('Exiting program...')
            break
        else:
            print('Invalid choice. Try again.')
            continue

        print('\nSorted Products:')
        for product in sorted_products:
            print(product)

if __name__ == '__main__':
    main()




