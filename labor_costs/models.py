from django.db import models

# Create your models here.
class Employee(models.Model):
    """员工信息"""
    sap_id = models.IntegerField() # SAP工号
    p_name = models.CharField(max_length=100) # 员工姓名


    def __str__(self):
        return f"{self.sap_id} - {self.p_name}"
    
class CostData_Year(models.Model):
    """人工成本年份"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) # 关联Employee类
    cost_year = models.IntegerField() # 成本年份

    def __str__(self):
        return f"{self.employee.sap_id} - {self.employee.p_name} - {self.cost_year}"
    
class CostData(models.Model):
    """人工成本月份数据"""
    cost_year = models.ForeignKey(CostData_Year, on_delete=models.CASCADE) # 关联CostDate_Year类
    cost_month = models.IntegerField() # 成本月份
    p_group = models.CharField(max_length=100) # 员工组
    p_area = models.CharField(max_length=100) # 区域
    p_company = models.CharField(max_length=100) # 公司
    p_department = models.CharField(max_length=100) # 员工部门
    p_function = models.CharField(max_length=100) # 职能条线
    p_state = models.CharField(max_length=100) # 在职状态
    p_classification = models.CharField(max_length=100) # 人员分类
    p_position_function = models.CharField(max_length=100) # 岗位职能
    cost_sb_simple = models.DecimalField(max_digits=10, decimal_places=2) # 社保金额-单月
    cost_gjj_simple = models.DecimalField(max_digits=10, decimal_places=2) # 公积金金额-单月
    cost_salary_simple = models.DecimalField(max_digits=10, decimal_places=2) # 工资金额-单月
    cost_sb_multiple = models.DecimalField(max_digits=10, decimal_places=2) # 社保金额-多月
    cost_gjj_multiple = models.DecimalField(max_digits=10, decimal_places=2) # 公积金金额-多月
    cost_salary_multiple = models.DecimalField(max_digits=10, decimal_places=2) # 工资金额-多月
    cost_compensation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 补偿金金额
    cost_sbgjj_estimate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 社保公积金-全年预估
    cost_salary_estimate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 工资-全年预估

    def __str__(self):
        return f"{self.cost_year} - {self.cost_month}"