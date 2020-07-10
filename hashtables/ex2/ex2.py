#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    tix_dict = {}
    route = [None] * length

    for t in tickets:
        tix_dict[t.source] = t.destination
        # {'PIT': 'ORD', 'XNA': 'CID', 'SFO': 'BHM', 'FLG': 'XNA', 'NONE': 'LAX', 'LAX': 'SFO', 'CID': 'SLC', 'ORD': 'NONE', 'SLC': 'PIT', 'BHM': 'FLG'}
        # print(tix_dict)

    route[0] = (tix_dict["NONE"])

    for i in range(1, length):
        route[i] = tix_dict[route[i-1]]

    return route


tickets = [
    Ticket(source="PIT", destination="ORD"),
    Ticket(source="XNA", destination="CID"),
    Ticket(source="SFO", destination="BHM"),
    Ticket(source="FLG", destination="XNA"),
    Ticket(source="NONE", destination="LAX"),
    Ticket(source="LAX", destination="SFO"),
    Ticket(source="CID", destination="SLC"),
    Ticket(source="ORD", destination="NONE"),
    Ticket(source="SLC", destination="PIT"),
    Ticket(source="BHM", destination="FLG")
]

length = 9

print(reconstruct_trip(tickets, length))
