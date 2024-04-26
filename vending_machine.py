# Selling items and details
selling_items = {  
                    0: { 'label': 'item_1', 'price': 3, 'quantity': 30 }, 
                    1: { 'label': 'item_2', 'price': 20, 'quantity': 30 }, 
                    2: { 'label': 'item_3', 'price': 30, 'quantity': 30 } 
                }

# Current machine notes
notes = { 
            1: 20, 
            5: 1, 
            10: 1, 
            20: 1, 
            50: 2
        }

def calculateRamining(input):
    # Recorder
    amount = {}

    # Get current item details
    current_item = selling_items[input['item_id']]
    current_item_quantity = current_item['quantity']

    # Check input quantity
    if(input['quantity'] > current_item_quantity):
        return "Order quantity too much"

    # Count total price
    total_price = current_item['price'] * input['quantity']

    # Get current payment
    payment = input['notes']

    # Count return amount
    remaining = payment - total_price
    if(remaining == 0):
        return "No changes."

    if(remaining < 0):
        return "Insufficient payment."

    if(remaining > 0):
        sortedNotes= (sorted(notes.items(), reverse=True))
        sortedNotes=dict(sortedNotes)

        for x,y in sortedNotes.items():

            # Check need how many notes to return
            notes_quantity = int(remaining/x)

            # If greater than current notes stock will break
            if(notes_quantity > y):
                notes_quantity = 1

            # Count remaining
            remaining = remaining - (x * notes_quantity)

            # If current notes is not enough to pay then skip
            if(notes_quantity <= 0):
                continue
            amount[x]=notes_quantity

            if(remaining == 0):
                break
        
        if(len(amount) == 0):
            return "Current machines dont have enought notes"
        
    return amount

# Sample input
current_input = { 'item_id': 0, 'quantity': 1, 'notes': 20 }
print(calculateRamining(current_input))