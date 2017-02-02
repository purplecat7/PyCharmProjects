import stormdata as ds


def main():
    storm_data = ds.StormData("../data/ibtracs_storms.dat")
    storm_str = ""
    
    #note: this id does not exist so the call throws an exception and
    #terminates the program. A workaround would be to return a 'not known'
    #error, and provide another function to explicitly return all available
    #keys. The calling program can then validate an entry, and/or iterate
    #over all of them.
#    storm_str = "2349084387935"     
#    w1, w2, w3 = storm_data.windspeed_from_serial_number(storm_str)
    
#    print (storm_str, w1, w2, w3)
    
    #note: this id is for a storm with no wind data at all!
    #It's therefore not loaded into the program's data at all and produces
    #the same error output as above.
    
#    storm_str = "1900032S20410"   
#    w1, w2, w3 = storm_data.windspeed_from_serial_number(storm_str)
    
#    print ("storm_str", w1, w2, w3)
    
    #note: documentation unclear: 'returns a list' vs 'returns: tuple'
    #It's actually a list!
    storm_str = "1900032S20050"   
    w1 = storm_data.windspeed_from_serial_number(storm_str)
    
    print (storm_str, w1)    
    
    
    storm_str = "1980234N36287"   
    w1 = storm_data.windspeed_from_serial_number(storm_str)
    
    print (storm_str, w1)     
    
    
if __name__ == "__main__":
    main()