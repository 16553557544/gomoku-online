import pathlib
import sys

raw = pathlib.Path("page.html").read_text(encoding="utf-8")
cut = raw.find(">\n<meta charset=\"UTF-8\">")
if cut < 0:
    sys.exit("boundary marker not found in fetched page")

html = '<!DOCTYPE html>\n<html lang="zh-CN">\n<head' + raw[cut:]

site = pathlib.Path("site")
site.mkdir(exist_ok=True)
(site / "index.html").write_text(html, encoding="utf-8")
print("bytes:", len(html.encode("utf-8")))
