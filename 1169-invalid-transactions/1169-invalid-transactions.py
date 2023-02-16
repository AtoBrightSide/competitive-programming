class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        tracker = defaultdict(list)
        for i, transaction in enumerate(transactions):
            n, t, a, c = transaction.split(",")
            if int(a) > 1000:
                # invalid.append(f"{n},{t},{a},{c}")
                invalid.add(i)
            if n in tracker:
                for trs in tracker[n]:
                    time, amt, city, idx = trs
                    if abs(int(time) - int(t)) <= 60 and city != c:
                        invalid.add(idx)
                        invalid.add(i)
            
            tracker[n].append([t, a, c, i])
        
        invalid = [transactions[i] for i in invalid]
        return invalid
            