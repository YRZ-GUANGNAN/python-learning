# Python 学习记录

我的 Python 学习项目，记录从基础语法到调用 API 的完整过程。

## 主要项目：天气查询工具

`weather_app.py` — 命令行天气查询工具

**功能：**

- 查询任意城市的实时天气（数据来自高德地图 API）
- 查询历史自动保存到本地文件
- 查看历史 / 清空历史

**运行方法：**

1. 在项目根目录新建 `config.py`，填入你的高德地图 API key
2. 运行 `python weather_app.py`

## 其他练习文件

- `utils.py` / `main.py` — 模块化练习
- `net_test.py` — 网络连通性测试
- `conflict_demo.txt` — Git 冲突处理实验

## 学到的东西

- **Python 基础**：变量、条件、循环、函数、异常处理、文件读写、JSON
- **调用 API**：requests、JSON 解析、API key 管理
- **Git**：提交、分支、合并、解决冲突、远程仓库