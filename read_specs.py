# -*- coding: utf-8 -*-
import os
import glob
import sys

# 設置輸出編碼為 UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

base_dir = "__LEGACY_ARCHIVE__/251223TAITS最大完備檔"

# 讀取關鍵文件
key_files = [
    "TAITS_PROJECT_PROMPT.md",
    "TAITS_專案總覽與使用說明（README）__251220.md",
    "TAITS_本地執行與運算環境規範（LOCAL_ENV）__251219.md",
    "TAITS_母體總憲法與核心鐵律（MASTER_ARCH）__251219.md",
    "TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）__251219.md",
    "TAITS_全系統架構總覽（FULL_ARCH）__251219.md",
    "TAITS_系統架構與流程細化說明（ARCH_FLOW）__251219.md"
]

for filename in key_files:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        print(f"\n{'='*80}")
        print(f"文件: {filename}")
        print('='*80)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # 輸出全部內容到文件
                output_file = f"spec_{filename.replace('/', '_').replace('（', '_').replace('）', '_').replace('×', '_')}.txt"
                with open(output_file, 'w', encoding='utf-8') as out:
                    out.write(content)
                print(f"已保存到: {output_file}")
                print(content[:8000])  # 前8000字符
                if len(content) > 8000:
                    print("\n... (文件繼續，完整內容已保存)")
        except Exception as e:
            print(f"讀取錯誤: {e}")
            import traceback
            traceback.print_exc()
