# Selenium + pytest 自动化测试项目

## 项目结构

```
test_project/
├── tests/                  # 测试代码
│   ├── __init__.py
│   ├── conftest.py         # pytest 配置（fixture）
│   └── test_search.py      # 搜索功能测试
├── reports/                # 测试报告
├── requirements.txt        # 依赖列表
└── README.md               # 本文件
```

## 运行测试

```bash
cd E:\test_project
pytest tests/ -v
```

## 生成 HTML 报告

```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```