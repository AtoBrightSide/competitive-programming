class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_use = {}
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] in can_use:
                    can_use[ingredients[i][j]].append(recipes[i])
                else:
                    can_use[ingredients[i][j]] = [recipes[i]]
        
        to_make = {}
        for i, rec in enumerate(recipes):
            to_make[rec] = len(ingredients[i])
            
        recipes = set(recipes)
        queue = deque()
        ans = []
        for sup in supplies:
            queue.append(sup)
        while queue:
            curr = queue.popleft()
            if curr in recipes:
                ans.append(curr)
            if curr in can_use:
                for meal in can_use[curr]:
                    to_make[meal] -= 1
                    if to_make[meal] == 0:
                        queue.append(meal)
                    
        return ans