from django import forms

import pandas as pd
from .models import Employee

from .models import CostData_Year, CostData

class ReportYearForm(forms.Form):
    report_year = forms.IntegerField(label='报表年份')

class ReportMonthForm(forms.Form):
    report_month = forms.IntegerField(label='报表月份')

class ImportSAPSingleMonthForm(forms.Form):
    sap_single_month_file = forms.FileField(label='导入SAP单月人工成本表')

class ImportSAPMultiMonthForm(forms.Form):
    sap_multi_month_file = forms.FileField(label='导入SAP多月人工成本表')

"""上传Excel文件的部分
class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='上传Excel文件')

    def clean_excel_file(self):
        excel_file = self.cleaned_data['excel_file']
        # 在这里添加你的文件处理逻辑，提取所需信息
        # 例如，使用 pandas 库来读取 Excel 文件
        # 然后从中提取所需的信息，并返回给视图处理
        return excel_file
"""