def meeting(s):
    s=s.upper()
    l = sorted(list(map(lambda x: ", ".join(x),list(map(lambda x: x[::-1],list(map(lambda x: x.split(":"), s.split(";"))))))))
    return "".join(list(map(lambda x:f'({x})',l)))

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))