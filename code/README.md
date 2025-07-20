# MCP Stdio 文件解析服务器

## 依赖安装
```bash
pip install -r requirements.txt
```

## 启动
```bash
python mcp_server.py
```

## 使用
通过标准输入传入如下json：
```json
{"file": "文件url", "AGENT_USER_INPUT": "你的指令"}
```
服务器会输出解析后的json结果。 