from django.shortcuts import render, redirect

from .forms import ReportYearForm, ReportMonthForm, ImportSAPSingleMonthForm, ImportSAPMultiMonthForm

def index(request):
    # 人工成本的主页
    return render(request, 'labor_costs/index.html')

def new_data(request):
    """添加新数据"""
    if request.method == 'POST':
        # 检查提交的表单是哪个
        if 'report_year' in request.POST:
            # 如果是报表年份表单提交
            form = ReportYearForm(request.POST)
            if form.is_valid():
                # 处理表单数据
                # 在这里可以执行保存到数据库等操作
                return redirect('labor_costs:index')  # 重定向到下一步页面

        elif 'report_month' in request.POST:
            # 如果是报表月份表单提交
            form = ReportMonthForm(request.POST)
            if form.is_valid():
                # 处理表单数据
                # 在这里可以执行保存到数据库等操作
                return redirect('labor_costs:index')  # 重定向到下一步页面
            
        elif 'import_sap_single_month' in request.POST:
            # 如果是导入SAP单月人工成本表表单提交
            form = ImportSAPSingleMonthForm(request.POST, request.FILES)
            if form.is_valid():
                # 处理表单数据
                # 在这里可以执行保存到数据库等操作
                return redirect('labor_costs:index')  # 重定向到下一步页面

        elif 'import_sap_multi_month' in request.POST:
            # 如果是导入SAP多月人工成本表表单提交
            form = ImportSAPMultiMonthForm(request.POST, request.FILES)
            if form.is_valid():
                # 处理表单数据
                # 在这里可以执行保存到数据库等操作
                return redirect('labor_costs:index')  # 重定向到下一步页面

    else:
        # 如果是 GET 请求，返回空表单
        report_year_form = ReportYearForm()
        report_month_form = ReportMonthForm()
        import_sap_single_month_form = ImportSAPSingleMonthForm()
        import_sap_multi_month_form = ImportSAPMultiMonthForm()

    return render(request, 'labor_costs/new_data.html', {
        'report_year_form': report_year_form,
        'report_month_form': report_month_form,
        'import_sap_single_month_form': import_sap_single_month_form,
        'import_sap_multi_month_form': import_sap_multi_month_form,
    })
        

"""处理导入Excel的部分
from .forms import ExcelUploadForm

def upload_excel_view(request):
    # 导入Excel的页面
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            # 在这里处理上传的 Excel 文件，提取所需信息，并执行数据库操作
            # 例如，使用 pandas 库来读取 Excel 文件并提取信息
            # 然后将信息存入数据库
            # 提示：可以使用 pandas.read_excel 方法来读取 Excel 文件
            # 然后使用 DataFrame 提供的方法来处理数据
            # 最后将处理后的数据存入数据库
            # 示例代码： df = pd.read_excel(excel_file)
            #           # 在这里处理 DataFrame，并将数据存入数据库
            # 重定向或其他操作
    else:
        form = ExcelUploadForm()
    return render(request, 'upload_excel.html', {'form': form})
"""