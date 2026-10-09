# Python 学习记录

我的 Python 学习项目，记录从基础语法到调用 API 的完整过程。

## 项目

### 1. 天气查询工具

`weather_app.py` — 命令行天气查询工具

**功能：**

- 查询任意城市的实时天气（数据来自高德地图 API）
- 查询历史自动保存到本地文件
- 查看历史 / 清空历史

### 2. AI 对话助手

`ai_chat.py` — 带记忆的命令行 AI 助手### 3. 记账本（MySQL 版）

`book_app.py` — 命令行记账工具，数据存在 MySQL 数据库里

**功能：**

- 记一笔（项目 + 金额）
- 查看所有记录（带时间）
- 按项目统计（笔数、小计、总计）
- 删除记录

**运行方法：**

1. 在 `config.py` 里加上 `db_password`（你的 MySQL 密码）
2. 运行 `python book_app.py`

**功能：**

- 和 AI 多轮对话，支持上下文记忆
- 对话记录自动保存，关掉程序再打开还能继续聊
- 查看完整对话记录

## 运行方法

1. 在项目根目录新建 `config.py`，填入你的 API key：

```python
api_key = "高德地图的 key"
deepseek_key = "DeepSeek 的 key"