from SPARQLWrapper import SPARQLWrapper, JSON
from read_utils import read_json_file
import json
from urllib.parse import quote, urlparse
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def is_valid_uri(value):
    """
    Kiểm tra xem một chuỗi có phải là URI hợp lệ hay không.
    
    Args:
        value (str): Chuỗi cần kiểm tra.
    
    Returns:
        bool: True nếu chuỗi là URI hợp lệ, False nếu không.
    """
    try:
        result = urlparse(value)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def is_person(uri):
    """Kiểm tra xem đối tượng có rdf:type là một loại 'Người' không."""
    if not is_valid_uri(uri):
        logging.warning(f"URI không hợp lệ: {uri}")
        return False

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    # encoded_uri = quote(uri, safe=":/")

    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?type
    WHERE {{
        <{uri}> rdf:type ?type .
    }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    person_types = {
        "http://dbpedia.org/ontology/Person",
        "http://xmlns.com/foaf/0.1/Person",
        "http://schema.org/Person",
        "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#NaturalPerson",
        "http://dbpedia.org/class/yago/Person100007846",
        "http://dbpedia.org/class/yago/Ruler110541229",
        "http://dbpedia.org/ontology/Ruler"
    }

    try:
        results = sparql.query().convert()
        if not results["results"]["bindings"]:
            logging.warning(f"Truy vấn SPARQL không trả về kết quả cho URI: {uri}")
            return False

        for result in results["results"]["bindings"]:
            type_value = result["type"]["value"]
            if type_value in person_types:
                logging.info(f"Đối tượng {uri} được xác định là người với loại: {type_value}")
                return True
        logging.info(f"Đối tượng {uri} không phải là người.")
        return False
    except Exception as e:
        logging.error(f"Lỗi khi truy vấn SPARQL cho URI {uri}: {e}")
        return False

def get_famous_people_in_dynasty(input_file, output_file):
    """
    Xử lý dữ liệu triều đại, lọc các đối tượng là người và lưu vào file mới theo định dạng yêu cầu.
    
    Args:
        input_file (str): Đường dẫn tới file JSON đầu vào.
        output_file (str): Đường dẫn tới file JSON đầu ra.
    """
    logging.info(f"Đang đọc dữ liệu từ file: {input_file}")
    # Sử dụng hàm read_json_file để đọc dữ liệu
    dynasties = read_json_file(input_file)

    # Kiểm tra dữ liệu có phải là danh sách hay không
    if not isinstance(dynasties, list):
        logging.error("Dữ liệu không phải là danh sách. Vui lòng kiểm tra file JSON.")
        return

    logging.info(f"Đã đọc được {len(dynasties)} triều đại từ file.")

    # Kết quả cuối cùng
    result = []

    # Duyệt qua từng triều đại
    for dynasty in dynasties:
        dynasty_uri = dynasty.get("dynasty_uri")
        dynasty_label = dynasty.get("dynasty_label")
        details = dynasty.get("details", [])

        logging.info(f"Đang xử lý triều đại: {dynasty_label} ({dynasty_uri})")
        logging.info(f"Số lượng chi tiết cần kiểm tra: {len(details)}")

        # Danh sách các nhân vật nổi tiếng
        famous_people = []
        for detail in details:
            uri = detail.get("value")
            if uri:
                logging.info(f"Đang kiểm tra URI: {uri}")
                if is_person(uri):  # Kiểm tra xem đối tượng có phải là người không
                    logging.info(f"Đối tượng là người: {uri}")
                    famous_people.append({
                        "person_uri": uri,
                        "person_label": uri.split("/")[-1].replace("_", " ")  # Lấy nhãn từ URI
                    })
                else:
                    logging.info(f"Đối tượng không phải là người: {uri}")

        # Thêm thông tin triều đại vào kết quả
        result.append({
            "dynasty_uri": dynasty_uri,
            "dynasty_label": dynasty_label,
            "famous_people": famous_people
        })

        logging.info(f"Số lượng nhân vật nổi tiếng trong triều đại {dynasty_label}: {len(famous_people)}")

    # Ghi kết quả vào file đầu ra
    logging.info(f"Đang ghi kết quả vào file: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    logging.info(f"Đã lưu thông tin các triều đại và nhân vật nổi tiếng vào file '{output_file}'.")