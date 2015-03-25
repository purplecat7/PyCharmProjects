class ItemList(list):
    '''
    FUNCTIONS:
        GetItem: Return a single item object from the list
    '''
    def GetItem(self,parameter):
        '''
        Searches for an item object in the itemlist given the parameter
    
        ARGS:
            parameter:
                A value to match against the item can be
                    Int: Unique ID of the item
                    String: The title of the item
                
        RETURNS:
            Item:
                An item object matching the parameter
        '''
        # Check the type of the parameter
        if type(parameter) == int:
            parameterType = 'ID'
            
        elif type(parameter) == str:
            parameterType = 'Title'
            
        else:
            raise Exception

        # Loop over items
        for item in self:
            itemParameter = item.getParameter(parameterType)
            # Check whether the item is the requested item
            if parameter == itemParameter:
                # Yes - Return the item matching the ID
                return item
        # If no item is found raise an exception
        raise ItemNotFoundException()
        
class UserItemList(ItemList):
    '''
    FUNCTIONS:
        GetFines:
            Accumulates the fines from each overdue item
    '''
    def GetFines(self):
        '''
        Calculates the fines from each item in the list
        '''
        #
        for item in self:
            





        