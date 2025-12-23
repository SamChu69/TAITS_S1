# -*- coding: utf-8 -*-
import os
import glob
import json

base_dir = "__LEGACY_ARCHIVE__/251223TAITS最大完備檔"
specs_dir = "specs"

os.makedirs(specs_dir, exist_ok=True)

files = glob.glob(os.path.join(base_dir, "*.md"))
print(f"找到 {len(files)} 個規格文件")

specs_summary = {}

for filepath in files:
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 保存完整內容
        output_file = os.path.join(specs_dir, filename.replace('/', '_').replace('（', '_').replace('）', '_').replace('×', '_') + '.txt')
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(content)
        
        # 提取 doc_key
        doc_key = None
        for line in content.split('\n')[:50]:
            if 'doc_key' in line.lower() or 'doc_key：' in line:
                parts = line.split('：') if '：' in line else line.split(':')
                if len(parts) > 1:
                    doc_key = parts[1].strip()
                    break
        
        specs_summary[filename] = {
            'doc_key': doc_key,
            'size': len(content),
            'saved_to': output_file
        }
        print(f"[OK] {filename} -> {output_file}")
    except Exception as e:
        print(f"[ERROR] {filename}: {e}")

# 保存摘要
with open(os.path.join(specs_dir, 'specs_summary.json'), 'w', encoding='utf-8') as f:
    json.dump(specs_summary, f, ensure_ascii=False, indent=2)

print(f"\n已保存 {len(specs_summary)} 個規格文件到 {specs_dir}/")
