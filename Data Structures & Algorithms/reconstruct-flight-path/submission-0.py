class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dir_graph = defaultdict(list)
        for i in range(len(tickets)):
            dir_graph[tickets[i][0]].append((tickets[i][1],i))

        for  src, lst_tickets in dir_graph.items():
            lst_tickets.sort()


        used_ticket = set()

        def dfs(source):
            for ticket in dir_graph[source]:
                if ticket[1] in used_ticket:
                    continue
                used_ticket.add(ticket[1])
                rem_path = dfs(ticket[0])
                if len(used_ticket) == len(tickets):
                    return [source] + rem_path
                used_ticket.remove(ticket[1])
            return [source]

        return dfs("JFK")


        