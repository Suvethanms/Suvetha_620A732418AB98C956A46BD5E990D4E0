#challeng3.1

def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
          
    return indices

# Sample list of products
product_list = ["orange", "banana", "orange", "apple", "grape", "apple","orange"]

target_product = "orange"
target_product="juice"
result = linear_search_product(product_list, target_product)

# Print the result
print(result)