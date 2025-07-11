def presenteer(dict, totaal):
    uit = []
    for element in dict:
        uit.append(f"{element} : {dict[element]} euro")
    uit.append(int(26) * "=")
    uit.append(f"Totaal : {totaal} euro")
    return "\n".join(uit)

'''
mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
totaal = 50

presenteer(mijn_dict, totaal)
print()
'''
