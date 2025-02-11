class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_transactions = set()
        tracker = defaultdict(list)
        
        for i, curr_transaction in enumerate(transactions):
            name, time, amt, city = curr_transaction.split(",")
            if int(amt) > 1000:
                invalid_transactions.add(i)
                
            for other_transaction in tracker[name]:
                idx, time_2, city_2 = other_transaction
                if abs(time_2 - int(time)) <= 60 and city_2 != city:
                    invalid_transactions.add(idx)
                    invalid_transactions.add(i)
            
            tracker[name].append([i, int(time), city])
        
        return [transactions[i] for i in invalid_transactions]