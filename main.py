from SPARQLWrapper import SPARQLWrapper, JSON
from initiation import init_sparql, create_dynasties_query, create_dynasty_details_query
from save_utils import save_to_csv, save_to_json, save_all_dynasties_details
from read_utils import read_dynasties_json
import pandas as pd
import logging

# Thiết lập logging
logging.basicConfig(level=logging.INFO)


# Thực thi truy vấn SPARQL
def execute_query(sparql, query):
    """Thực thi truy vấn SPARQL và trả về kết quả."""
    sparql.setQuery(query)
    try:
        results = sparql.query().convert()
        return results["results"]["bindings"]
    except Exception as e:
        logging.error(f"❌ Lỗi khi thực thi truy vấn: {e}")
        return []
    
# Xử lý kết quả truy vấn
def process_dynasties_results(bindings):
    """Xử lý và lọc kết quả để chỉ lấy triều đại."""
    data = []
    exclude_keywords = [
        "Domination", "Era", "Period", "Rebellion", "Uprising", 
        "List", "Family tree", "monarchs", "era name"
    ]  
    for result in bindings:
        dynasty_uri = result["dynasty"]["value"]
        label = result["label"]["value"]
        # Loại bỏ nếu label chứa từ khóa không mong muốn
        if not any(keyword.lower() in label.lower() for keyword in exclude_keywords):
            data.append({"uri": dynasty_uri, "label": label})
    return data

# Truy vấn chi tiết cho một triều đại
def fetch_dynasty_details(sparql, dynasty_uri, dynasty_label):
    """Truy vấn chi tiết cho một triều đại và trả về dữ liệu."""
    print(f"\nĐang truy vấn chi tiết cho: {dynasty_label} ({dynasty_uri})")
    query = create_dynasty_details_query(dynasty_uri)
    bindings = execute_query(sparql, query)
    details = process_dynasty_details(bindings)
    
    if details:
        print(f"Tìm thấy {len(details)} thuộc tính:")
        for detail in details:
            print(f"Thuộc tính: {detail['property']}")
            print(f"Giá trị: {detail['value']}")
            print("-" * 50)
    else:
        print("Không tìm thấy chi tiết nào.")
    
    return details

# Hàm 4: Xử lý kết quả chi tiết của triều đại
def process_dynasty_details(bindings):
    """Xử lý kết quả truy vấn để lấy các thuộc tính và giá trị."""
    data = []
    for result in bindings:
        property_uri = result["property"]["value"]
        value = result["value"]["value"]
        data.append({"property": property_uri, "value": value})
    return data

# Tổng hợp chi tiết của tất cả triều đại
def aggregate_dynasties_details(dynasties, sparql):
    """Tổng hợp chi tiết của tất cả triều đại từ danh sách."""
    all_dynasty_details = []
    for dynasty in dynasties:
        dynasty_uri = dynasty["uri"]
        dynasty_label = dynasty["label"]
        details = fetch_dynasty_details(sparql, dynasty_uri, dynasty_label)
        if details:
            dynasty_data = {
                "dynasty_uri": dynasty_uri,
                "dynasty_label": dynasty_label,
                "details": details
            }
            all_dynasty_details.append(dynasty_data)
    return all_dynasty_details

# Hàm chính: Điều phối quy trình lấy chi tiết
def get_dynasty_details(dynasties_file, output_file):
    """Lấy chi tiết của từng triều đại từ file JSON và lưu kết quả."""
    # Đọc danh sách triều đại
    dynasties = read_dynasties_json(dynasties_file)
    if not dynasties:
        print("Không thể đọc danh sách triều đại.")
        return
    
    # Khởi tạo SPARQL
    sparql = init_sparql()
    
    # Tổng hợp chi tiết
    all_dynasty_details = aggregate_dynasties_details(dynasties, sparql)
    
    # Lưu kết quả
    save_all_dynasties_details(all_dynasty_details, output_file)

# Hàm chính 1: Điều phối toàn bộ quy trình
def get_vietnamese_dynasties(category_url):
    """Lấy danh sách triều đại Việt Nam từ category URL."""
    # Chuyển URL sang URI
    category_uri = category_url.replace("https://dbpedia.org/page/", "http://dbpedia.org/resource/")
    print(f"Category URI: {category_uri}")
    
    # Khởi tạo SPARQL
    sparql = init_sparql()
    
    # Tạo truy vấn
    query = create_dynasties_query(category_uri)
    
    # Thực thi truy vấn
    bindings = execute_query(sparql, query)
    
    # Xử lý kết quả
    dynasties = process_dynasties_results(bindings)
    
    # In kết quả
    if dynasties:
        print(f"\nTìm thấy {len(dynasties)} triều đại:")
        for dynasty in dynasties:
            print(f"Triều đại: {dynasty['label']}")
            print(f"Đường dẫn: {dynasty['uri']}")
            print("-" * 50)
    else:
        print("Không tìm thấy triều đại nào.")
    
    # Lưu vào json
    columns = ["uri", "label"]
    save_to_json(dynasties, columns, "vietnamese_dynasties.json")
    
    return dynasties

# Chạy chương trình
def main():
    # category_url = "https://dbpedia.org/page/Category:Vietnamese_dynasties"
    # print(f"Đang truy vấn danh sách triều đại từ: {category_url}")
    # get_vietnamese_dynasties(category_url)
    dynasties_file = "vietnamese_dynasties.json"
    output_file = "vietnamese_dynasties_details.json"
    print(f"Đang xử lý file: {dynasties_file}")
    get_dynasty_details(dynasties_file, output_file)

if __name__ == "__main__":
    main()