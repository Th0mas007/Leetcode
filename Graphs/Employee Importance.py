class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps={emp.id: emp for emp in employees}

        def dfs(target_id):
            res_sum=emps[target_id].importance
            for subs in emps[target_id].subordinates:
                res_sum+=dfs(subs)
            return res_sum
        return dfs(id)
