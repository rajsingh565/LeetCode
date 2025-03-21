class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes = {rec: ingr for rec, ingr in zip(recipes, ingredients)}
        supplies = set(supplies)

        @cache
        def dfs(item: str) -> bool:
            if item not in recipes:
                return item in supplies

            if item in in_progress:
                return False
            in_progress.add(item)

            for ingr in recipes[item]:
                if not dfs(ingr):
                    return False

            in_progress.remove(item)
            return True

        res = []
        in_progress = set()
        for rec in recipes:
            if dfs(rec):
                res.append(rec)
        return res