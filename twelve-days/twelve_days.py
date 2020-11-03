def recite(start_verse, end_verse):
    
    nth = {1: "first",
           2: "second",
           3: "third",
           4: "fourth",
           5: "fifth",
           6: "sixth",
           7: "seventh",
           8: "eighth",
           9: "ninth",
           10: "tenth",
           11: "eleventh",
           12: "twelfth"}

    gifts = {1: "a Partridge in a Pear Tree.",
             2: "two Turtle Doves",
             3: "three French Hens",
             4: "four Calling Birds",
             5: "five Gold Rings",
             6: "six Geese-a-Laying",
             7: "seven Swans-a-Swimming",
             8: "eight Maids-a-Milking",
             9: "nine Ladies Dancing",
             10: "ten Lords-a-Leaping",
             11: "eleven Pipers Piping",
             12: "twelve Drummers Drumming"}

    words = []
    _gifts = ""

    for i in range(1, end_verse+1):
        if i == 2:
            _gifts = gifts.get(i) + ", and " + _gifts
        else: 
            _gifts = gifts.get(i) + ", " + _gifts 
            
        if i >= start_verse: 
            words.append("On the " + nth.get(i) + " day of Christmas my true love gave to me: " + _gifts[:-2])
        
    return(words)


print(recite(1, 3))
