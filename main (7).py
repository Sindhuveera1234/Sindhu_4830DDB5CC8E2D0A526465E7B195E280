def LinearSearchProduct(productlist, targetproduct):
  play = []
  for index, products in enumerate(productlist):
    if products == targetproduct:
      play.append(index)
  return play


products = [
    "shoes", "boot", "loafr", "shoes", "sandal", " shoes", "sandal", "shoes"
]
target = "shoes"
result = LinearSearchProduct(products, target)
print(result)
