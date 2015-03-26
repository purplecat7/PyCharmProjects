class ItemList(list):
    '''
    FUNCTIONS:            
        return_item:
            Removes an item being checked in to the item list
            
        add_item: 
            Adds an item to the list
        
        remove_item: 
            Removes an item from the list
        
        get_item: 
            Return a single item object from the list
        
        number_of_items:
        
        get_fines:
            Accumulates the fines from each overdue item
            
        checkout_item:
            Adds an item being checked out to the item list
    '''
    def __init__(self):
        pass
    
    def add_item(self,item):
        '''
        Adds an item object to the item list
        '''
        # TODO - Check the item is valid
        self.append(item)
        
    def remove_item(self,item):
        '''
        Removes an item object from the item list
        '''
        self.remove(item)
    
    def get_item(self,parameter):
        '''
        Searches for an item object in the itemlist given the parameter
    
        ARGS:
            parameter:
                A value to match against the item, can be
                    Int: Unique ID of the item
                    String: The title of the item
                
        RETURNS:
            Item:
                An item object matching the parameter
        '''
        # Check the type of the parameter
        if type(parameter) == int:
            parameter_type = 'ID'
            
        elif type(parameter) == str:
            parameter_type = 'Title'
        
        # Raise an exception if the argument is invalid
        else:
            raise TypeError('Item can only be searched on ID or title')

        # Loop over items
        for item in self:
            item_parameter = item.get_parameter(parameter_type)
            # Check whether the item is the requested item
            if parameter == item_parameter:
                # Yes - Return the item matching the ID
                return item
        #If no item is found raise an exception
        # TODO - make this an ItemNotFoundException class
        raise Exception('No item found with ' + parameter_type + ' ' + 
                        str(parameter))
        
    def number_of_items(self):
        return len(self)

    def get_fines(self):
        '''
        Calculates the fines from each item in the list
            
        RETURNS:
            fine:
                Float of the total fine in pounds
        '''
        # Intitialise the fine
        fine = 0.0
        for item in self:
            fine += item.fine()
            
        return fine
        
    def checkout_item(self,item):
        '''
        Adds an item to be checked out to the item list
        
        ARGS:
            item:
                The item to be checked out
        '''
        # Set the checkout on the item
        item.set_checkout()        
        # Add the item to the list
        self.add_item(item)
        
        return
        
    def return_item(self,parameter):
        '''
        Removes an item being checked in from the UserList and resets the 
        checkout
        
        ARGS:
            parameter:
                A value to match against the item, can be
                    Int: Unique ID of the item
                    String: The title of the item
        '''
        # Find the item in this itemlist
        item = self.get_item(parameter)
        # Reset the checkout on the item
        item.reset_checkout()
        # Remove the item from the list
        self.remove_item(item)
        
        return
            





        