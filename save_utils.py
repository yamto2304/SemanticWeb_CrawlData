import pandas as pd
import logging
import json

def save_to_csv(data, columns, filename):
    if len(data) == 0:
        logging.warning(f"Không có dữ liệu để lưu vào file {filename}.")
        return
    
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    logging.info(f"✅ Đã lưu vào CSV: {filename}")


def save_to_excel(data, columns, filename):
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(filename, index=False)
    print(f"✅ Đã lưu vào Excel: '{filename}'")


def save_to_json(data, columns, filename):
    df = pd.DataFrame(data, columns=columns)
    df.to_json(filename, orient='records', force_ascii=False, indent=2)
    print(f"✅ Đã lưu vào JSON: '{filename}'")

# Lưu chi tiết tất cả triều đại vào file
def save_all_dynasties_details(all_dynasty_details, output_file):
    """Lưu tất cả chi tiết triều đại vào file JSON."""
    if not all_dynasty_details:
        print("Không có dữ liệu chi tiết để lưu.")
        return
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_dynasty_details, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu tất cả chi tiết vào: '{output_file}'")