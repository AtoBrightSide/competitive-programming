class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # processing denoted by 1
        # done denoted by 2
        # initial state denoted by 0
        
        graph = defaultdict(list)
        for i, recipe in enumerate(recipes):
            for ingd in ingredients[i]:
                graph[recipe].append(ingd)
                
        curr_state = defaultdict(int)
        supplies = set(supplies)        
        def dfs(meal):
            if curr_state[meal] == 2 or meal in supplies:   return True
            elif curr_state[meal] == 1:   return False
            
            can_make = True
            curr_state[meal] = 1
            for ing in graph[meal]:
                can_make = can_make and dfs(ing)
            
            curr_state[meal] = 2 if can_make and len(graph[meal]) > 0 else 0
            return can_make if len(graph[meal]) > 0 else False
        
        ans = []
        for recipe in recipes:  
            if dfs(recipe): ans.append(recipe)
        
        return ans