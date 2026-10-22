import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="app.log",           # ← 写到文件
    encoding="utf-8",
)
logging.debug("这是调试信息，INFO 级别下不会显示")
logging.info("用户登录成功")
logging.warning("余额不足")
logging.error("数据库连接失败")
logging.critical("服务即将停止")