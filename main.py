# Import the inventory and user_io modules
import inventory as invent
import user_io as io

# Define a main function that runs the program
def main():
  print("Welcome to the Vending Machine!")
  
  money = io.get_money()
  #display inventory_dict
  print("Here is a list of items you can purchase:")

  index = 1
  for key, value in invent.inventory_dict.items():
    print(f'{index}, {key} ({value[0]}) - ({value[1]}) left')
    index += 1

  key_list = list(invent.inventory_dict.items())
  value_list = list(invent.inventory_dict.values())
  product = key_list[choice - 1]
  price = value_list[choice -1][0]
  print(f'You have selected a {product}. The price is ${price}.')


  if money >= price:
    change = money - price
    print(f'You have inserted ${money}. Your change is ${change}.')


  print(f'Thank you for your purchase! Enjoy your {product}!')

if __name__ == "__main__":
  main()
