import logging
import json

def read_json_file(filename):
    """Đọc danh sách triều đại từ file JSON."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            dynasties = json.load(f)
        return dynasties
    except Exception as e:
        logging.error(f"❌ Lỗi khi đọc file {filename}: {e}")
        return []
    