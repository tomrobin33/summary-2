try:
    import requests
    import pandas
    import pptx
    import docx
    import lxml
    import PIL
    print("所有依赖导入成功")
except Exception as e:
    print("依赖导入失败:", e)
    import sys; sys.exit(1)
import sys
import json
from file_parser import parse_file

def main():
    for line in sys.stdin:
        try:
            req = json.loads(line)
            file_url = req.get("file")
            user_input = req.get("AGENT_USER_INPUT", "")
            if not file_url:
                resp = {"error": "未检测到文件URL"}
            else:
                file_json = parse_file(file_url)
                resp = {
                    "key0": user_input + "hello",
                    "key1": ["hello", "world"],
                    "key2": {"key21": "hi"},
                    "file_json": file_json
                }
        except Exception as e:
            resp = {"error": str(e)}
        print(json.dumps(resp, ensure_ascii=False), flush=True)

if __name__ == "__main__":
    main() 