import unittest
from unittest.mock import patch, MagicMock
from person_crawler import is_person
from person_crawler import get_famous_people_in_dynasty
from unittest.mock import mock_open
import json

class TestIsPerson(unittest.TestCase):
    @patch("person_crawler.SPARQLWrapper.query")
    def test_is_person_true(self, mock_query):
        """Kiểm tra khi đối tượng là Person."""
        # Mock kết quả trả về từ SPARQL query
        mock_query.return_value.convert.return_value = {
            "results": {
                "bindings": [
                    {"type": {"value": "http://dbpedia.org/ontology/Person"}}
                ]
            }
        }
        uri = "http://dbpedia.org/resource/Lý_Cao_Tông"
        self.assertTrue(is_person(uri))

    @patch("person_crawler.SPARQLWrapper.query")
    def test_is_person_false(self, mock_query):
        """Kiểm tra khi đối tượng không phải là Person."""
        # Mock kết quả trả về từ SPARQL query
        mock_query.return_value.convert.return_value = {
            "results": {
                "bindings": [
                    {"type": {"value": "http://dbpedia.org/ontology/Place"}}
                ]
            }
        }
        uri = "http://dbpedia.org/resource/Lý_Thái_Tổ"
        self.assertFalse(is_person(uri))

    @patch("person_crawler.SPARQLWrapper.query")
    def test_is_person_no_results(self, mock_query):
        """Kiểm tra khi không có kết quả trả về."""
        # Mock kết quả trả về từ SPARQL query
        mock_query.return_value.convert.return_value = {
            "results": {"bindings": []}
        }
        uri = "http://dbpedia.org/resource/Unknown"
        self.assertFalse(is_person(uri))

class TestGetFamousPeopleInDynasty(unittest.TestCase):
    @patch("person_crawler.is_person")
    @patch("person_crawler.read_json_file")
    @patch("builtins.open", new_callable=mock_open)
    def test_get_famous_people_in_dynasty(self, mock_open_file, mock_read_json_file, mock_is_person):
        """Kiểm tra hàm get_famous_people_in_dynasty với dữ liệu giả lập."""
        # Dữ liệu giả lập từ file JSON
        mock_read_json_file.return_value = [
            {"value": "http://dbpedia.org/resource/Lý_Cao_Tông"},
            {"value": "http://dbpedia.org/resource/Lý_Thái_Tổ"},
            {"value": "http://dbpedia.org/resource/Nhà_Lý"}
        ]

        # Giả lập kết quả của hàm is_person
        mock_is_person.side_effect = [True, True, False]

        # Gọi hàm cần kiểm tra
        input_file = "vietnamese_dynasties_details.json"
        output_file = "vietnamese_people.json"
        get_famous_people_in_dynasty(input_file, output_file)

        # Kiểm tra xem hàm read_json_file được gọi đúng với file đầu vào
        mock_read_json_file.assert_called_once_with(input_file)

        # Kiểm tra hàm is_person được gọi đúng số lần và với các URI tương ứng
        mock_is_person.assert_any_call("http://dbpedia.org/resource/Lý_Cao_Tông")
        mock_is_person.assert_any_call("http://dbpedia.org/resource/Lý_Thái_Tổ")
        mock_is_person.assert_any_call("http://dbpedia.org/resource/Nhà_Lý")
        self.assertEqual(mock_is_person.call_count, 3)

        # Kiểm tra dữ liệu được ghi vào file đầu ra
        expected_output = [
            {"value": "http://dbpedia.org/resource/Lý_Cao_Tông"},
            {"value": "http://dbpedia.org/resource/Lý_Thái_Tổ"}
        ]
        # Lấy nội dung đã ghi vào file
        handle = mock_open_file()
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertEqual(json.loads(written_data), expected_output)


if __name__ == "__main__":
    unittest.main()