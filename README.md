# Python 学习记录

> 从零基础到 Web API 的完整学习路径。包含基础语法、数据结构与算法的亲手实现、面向对象、网络请求、数据库操作，以及一个 FastAPI + MySQL 的记账服务。

**Python 3.14** · **FastAPI** · **PyMySQL** · **MySQL 8** · **requests** · 36 个文件 / 约 1,600 行

---

## 学习路径

### 1. 基础语法

变量、`if/elif/else`、`for` / `while`、`list` / `dict`、字符串方法、函数、异常处理、文件读写、JSON。

| 文件 | 内容 |
| --- | --- |
| `first_script.py` | 第一个程序：输入、条件判断、f-string |
| `test_datetime.py` | `datetime` 模块：`now()` / `strptime()` / `strftime()` |

### 2. 面向对象

从「只会用别人写的类」到「自己设计类」。

| 文件 | 内容 |
| --- | --- |
| `oop_practice.py` | `class` / `__init__` / `self` / `__str__` |
| `inherit_practice.py` | 继承、方法重写、`super()`、多态 |

### 3. 语法进阶

| 文件 | 内容 |
| --- | --- |
| `lambda_practice.py` | `lambda` + `sorted(key=)` |
| `kwargs_practice.py` | `*args` / `**kwargs` |
| `decorator_practice.py` | 装饰器：计时器、日志器 |
| `generator_practice.py` | 生成器 `yield` |

### 4. 数据结构（亲手实现）

不依赖 `collections`，每个结构都用 `class` 从零写一遍。

| 文件 | 实现 |
| --- | --- |
| `stack.py` | 栈：`push` / `pop` / `size` |
| `my_queue.py` | 队列：`enqueue` / `dequeue`（先进先出） |
| `LinkedQueue.py` | 链表：`Node` / `append` / `print_all` |
| `linkedQueuefanzhuan.py` | 链表进阶：`delete`（双指针）/ `reverse`（原地反转） |
| `tree.py` | 二叉树：前序 / 中序 / 后序遍历（递归） |
| `bst.py` | 二叉搜索树：`insert` / `search` / `inorder` |
| `graph.py` | 图：BFS（队列）/ DFS（栈） |
| `hash_table.py` | 哈希表：`hash(key) % size` + 链地址法解决冲突 |

### 5. 算法

| 文件 | 实现 |
| --- | --- |
| `sorting.py` | 冒泡（含 `swapped` 提前退出）、选择、插入 |
| `quick_sort.py` | 快速排序（递归 + 分治）、二分查找 |

### 6. 网络与 API

| 文件 | 内容 |
| --- | --- |
| `api_post.py` | `requests.post()` 发送 JSON |
| `net_test.py` | HTTP 请求基础 |
| `weather_app.py` | 项目一：天气查询工具 |

### 7. 数据库

| 文件 | 内容 |
| --- | --- |
| `db_test.py` | 连接 MySQL、建表、插入 |
| `db_read.py` | `SELECT` / `fetchall` / `fetchone` |
| `db_update.py` | `UPDATE` / `DELETE` |
| `db_stats.py` | 聚合：`COUNT` / `SUM` / `AVG` |
| `db_group.py` | `GROUP BY` 分组统计 |
| `db_join.py` | `JOIN` / `LEFT JOIN` |
| `book_app.py` | 项目三：记账本（MySQL 版） |

### 8. Web 后端

| 文件 | 内容 |
| --- | --- |
| `setup_db.py` | 建表脚本 |
| `app.py` | FastAPI 记账服务（见下） |

### 9. 工具链

| 文件 | 内容 |
| --- | --- |
| `info.sh` | Linux shell 脚本（`#!/bin/bash` + `set -e`） |

---

## 项目

### 天气查询工具 · `weather_app.py`

命令行天气查询，调用高德地图 API。

- 城市名 → `geocode` 拿 adcode → `weatherInfo` 拿天气
- 查询历史存 `history.json`，可查看 / 清空
- 业务状态校验（`status != "1"`、`count == "0"`）
- API Key 从 `config.py` 读取（已加入 `.gitignore`）

### AI 对话助手 · `ai_chat.py`

调用 DeepSeek API 的多轮对话工具。

- 双层循环：菜单层 + 对话层
- 对话历史持久化到 `chat_history.json`，每次请求带上完整上下文
- 错误处理：`if "error" in data` 检查业务错误

### 记账本（文件版）· `record_app.py`

`Record` 类 + JSON 持久化。

- 对象 ↔ 字典的双向转换（JSON 只认识字典，不认自定义类）
- 列表推导式读写
- 输入格式校验

### 待办清单 · `todo.py`

- `Todo` 类带 `done` 状态（布尔值）
- 自定义命令 `done N` 标记完成
- JSON 持久化

### 记账本（MySQL 版）· `book_app.py`

- 类封装连接、每个操作自开自关
- 四个功能：记一笔 / 查看 / 按项目统计 / 删除
- `cursor.rowcount` 判断删除是否生效

### 记账 API · `app.py` + `setup_db.py`

**FastAPI + PyMySQL + MySQL**

| 方法 | 路径 | 功能 |
| --- | --- | --- |
| `GET` | `/records` | 查询全部记录 |
| `POST` | `/records` | 新增一条（`pydantic` 自动校验） |
| `DELETE` | `/records/{id}` | 按 id 删除，不存在返回 404 |
| `GET` | `/summary` | 总笔数与总金额 |
| `GET` | `/docs` | Swagger UI（自动生成） |

```bash
pip install fastapi uvicorn pymysql
python setup_db.py
uvicorn app:app --reload
# 打开 http://127.0.0.1:8000/docs
```

---

## 环境与运行

```bash
python -m venv .venv
.venv\Scripts\activate
pip install requests fastapi uvicorn pymysql
```

**本项目需要一个 `config.py`**（未提交，见 `.gitignore`）：

```python
api_key = "高德地图的 key"
deepseek_key = "DeepSeek 的 key"
db_password = "MySQL 密码"
```

> 所有密钥都不入库。请勿提交 `config.py`。

---

## 说明

- 所有代码均为学习过程中的亲手实现，追求「理解原理」而非「调用现成库」
- 数据结构部分刻意不使用 `collections` 等现成实现
- 提交记录按学习阶段递增，可对照 `git log` 查看演进过程
