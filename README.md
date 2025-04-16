Fields for Data Extraction from Semantic Repositories for CHeVIE Ontology
Dựa trên ontology CHeVIE và yêu cầu trích xuất dữ liệu từ các kho ngữ nghĩa như DBPedia, dưới đây là danh sách các trường dữ liệu cần trích xuất cho từng chủ đề chính: Historical Figures, Historical Sites, Historical Events, Cultural Festivals, Administrative Divisions, và Dynasties.

1. Historical Figures
Dữ liệu liên quan đến các nhân vật lịch sử, kế thừa từ lớp Person của CIDOC-CRM và các thuộc tính đặc thù của CHeVIE.


URI: Định danh duy nhất của nhân vật (ví dụ: DBPedia URI như http://dbpedia.org/resource/Quang_Trung).

Name: Tên đầy đủ hoặc tên thường gọi (ví dụ: "Nguyễn Huệ", "Quang Trung").

Birth Date: Ngày/tháng/năm sinh, có thể là time:Instant hoặc time:Interval nếu không chính xác (ví dụ: "1753" hoặc "1752-1754").

Death Date: Ngày/tháng/năm mất, tương tự birth date (ví dụ: "1792-09-16").

Birth Place: Nơi sinh, liên kết với AdministrativeDivision (ví dụ: "Tây Sơn, Bình Định").

Dynasty: Triều đại mà nhân vật phục vụ hoặc liên quan (ví dụ: "Tây Sơn Dynasty").

Related Historical Events: Các sự kiện lịch sử nhân vật tham gia (participatesInEvent), ví dụ: "Trận Ngọc Hồi-Đống Đa".

Academic Degree: Học vị đạt được (ví dụ: "Cử Nhân", "Tiến Sĩ"), kèm năm đạt được nếu có.

Position Title: Chức danh chính thức (ví dụ: "Vua", "Tướng quân"), kèm khoảng thời gian giữ chức (holdingInterval).

Religion: Tôn giáo hoặc tín ngưỡng (ví dụ: "Buddhism", "Folk Religion").

Ethnicity: Dân tộc (ví dụ: "Kinh", "Tày").

Talent: Kỹ năng đặc biệt (ví dụ: "Academics", "Military Strategy").

Related Historical Sites: Di tích liên quan, như nơi tưởng niệm (commemoratedBy) (ví dụ: "Đền thờ Quang Trung").

Related Festivals: Lễ hội tưởng niệm nhân vật (festivalCommemorateHistoricalFigure) (ví dụ: "Lễ hội Tây Sơn").

Provenance: Nguồn gốc dữ liệu (prov:wasDerivedFrom), ví dụ: URL DBPedia hoặc tài liệu tham khảo.

Description: Mô tả ngắn về nhân vật (nếu có trong DBPedia).

2. Historical Sites
Dữ liệu về các di tích lịch sử, thuộc lớp Site với các phân loại cụ thể theo Luật Di sản Văn hóa Việt Nam.


URI: Định danh duy nhất (ví dụ: http://dbpedia.org/resource/Hue_Citadel).

Name: Tên di tích (ví dụ: "Kinh thành Huế").

Site Type: Loại di tích (HistoricalCulturalSite, ArchitecturalArtSite, ArchaeologicalSite, LandscapeSite, RevolutionarySite).

Location: Vị trí địa lý, liên kết với AdministrativeDivision (ví dụ: "Huế, Thừa Thiên Huế").

Construction Year: Năm xây dựng (nếu có, ví dụ: "1805").

Built By: Người/cơ quan xây dựng (ví dụ: "Nhà Nguyễn").

Related Historical Figures: Nhân vật liên quan (attachedToFigure) (ví dụ: "Gia Long").

Related Historical Events: Sự kiện liên quan (siteCommemorateEvent) (ví dụ: "Lễ lên ngôi của Gia Long").

Related Festivals: Lễ hội diễn ra tại di tích (hasFestival) (ví dụ: "Lễ hội Huế").

Site Level: Cấp độ di tích (ví dụ: "SpecialNationalLevel", "NationalLevel").

Renovation History: Thông tin cải tạo/nâng cấp (năm, cơ quan thực hiện, nếu có).

Geographical Coordinates: Tọa độ địa lý (dùng geo:lat, geo:long từ GEO ontology).

Provenance: Nguồn gốc dữ liệu (prov:wasDerivedFrom).

Description: Mô tả ngắn về di tích, bao gồm giá trị lịch sử/văn hóa.

3. Historical Events
Dữ liệu về các sự kiện lịch sử, thuộc lớp HistoricalEvent với các phân loại theo nội dung.


URI: Định danh duy nhất (ví dụ: http://dbpedia.org/resource/Battle_of_Ngoc_Hoi-Dong_Da).

Name: Tên sự kiện (ví dụ: "Trận Ngọc Hồi-Đống Đa").

Event Type: Loại sự kiện (EconomicEvent, PoliticalEvent, MilitaryEvent, DiplomaticEvent).

Date/Time: Thời gian xảy ra (time:Instant hoặc time:Interval, ví dụ: "1789-01").

Location: Địa điểm xảy ra, liên kết với AdministrativeDivision (ví dụ: "Hà Nội").

Related Historical Figures: Nhân vật tham gia (participatesInEvent) (ví dụ: "Quang Trung").

Related Historical Sites: Di tích liên quan (siteCommemorateEvent) (ví dụ: "Đền thờ Ngọc Hồi").

Related Dynasty: Triều đại diễn ra sự kiện (ví dụ: "Tây Sơn Dynasty").

Significance: Mức độ quan trọng (BasicEvent, NonBasicEvent).

Provenance: Nguồn gốc dữ liệu (prov:wasDerivedFrom).

Description: Mô tả ngắn về sự kiện, bao gồm bối cảnh và kết quả.

4. Cultural Festivals
Dữ liệu về các lễ hội văn hóa, thuộc lớp Festival với các phân loại theo Bộ Văn hóa, Thể thao và Du lịch.


URI: Định danh duy nhất (ví dụ: http://dbpedia.org/resource/Hung_Kings_Festival).

Name: Tên lễ hội (ví dụ: "Lễ hội Đền Hùng").

Festival Type: Loại lễ hội (TraditionalFestival, ReligiousFestival, RevolutionHistoryFestival, AbroadFestival).

Date/Time: Thời gian diễn ra (time:Instant hoặc time:Interval, ví dụ: "Mùng 10 tháng 3 âm lịch").

Duration: Thời lượng lễ hội (ví dụ: "3 ngày").

Frequency: Tần suất tổ chức (ví dụ: "Hàng năm").

Location: Địa điểm tổ chức, liên kết với AdministrativeDivision (ví dụ: "Phú Thọ").

Related Ethnicity: Dân tộc liên quan (ví dụ: "Kinh").

Related Religion: Tôn giáo liên quan (ví dụ: "Folk Religion").

Related Historical Figures: Nhân vật được tưởng niệm (festivalCommemorateHistoricalFigure) (ví dụ: "Hùng Vương").

Related Historical Sites: Di tích liên quan (festivalPlace) (ví dụ: "Đền Hùng").

Related Historical Events: Sự kiện liên quan (nếu có, ví dụ: "Lễ kỷ niệm lập quốc").

Provenance: Nguồn gốc dữ liệu (prov:wasDerivedFrom).

Description: Mô tả ngắn về lễ hội, bao gồm ý nghĩa văn hóa.

5. Administrative Divisions
Dữ liệu về các đơn vị hành chính, kế thừa từ Juso:AdministrativeDivision.


URI: Định danh duy nhất (ví dụ: http://dbpedia.org/resource/Hanoi).

Name: Tên đơn vị hành chính (ví dụ: "Hà Nội").

Division Level: Cấp hành chính (ví dụ: "FirstLevelAdministrativeDivision", "SecondLevelAdministrativeDivision").

Parent Division: Đơn vị hành chính cấp cao hơn (juso:parent, ví dụ: "Việt Nam" cho Hà Nội).

Historical Names: Các tên gọi lịch sử (ví dụ: "Thăng Long", "Đông Kinh" cho Hà Nội).

Geographical Coordinates: Tọa độ địa lý (geo:lat, geo:long).

Related Historical Sites: Di tích nằm trong đơn vị (sitePlace) (ví dụ: "Văn Miếu").

Related Festivals: Lễ hội tổ chức trong đơn vị (festivalPlace) (ví dụ: "Lễ hội Gióng").

Related Historical Events: Sự kiện diễn ra trong đơn vị (ví dụ: "Khởi nghĩa Hai Bà Trưng").

Related Historical Figures: Nhân vật sinh ra hoặc hoạt động trong đơn vị (birthPlace, ví dụ: "Hai Bà Trưng").

Provenance: Nguồn gốc dữ liệu (prov:wasDerivedFrom).

Description: Mô tả ngắn về đơn vị hành chính, bao gồm lịch sử và đặc điểm.
===========================================================================================================
6. Dynasties
Dữ liệu về các triều đại lịch sử, là thể hiện của lớp CIDOC-CRM:E4_Period.


URI: Định danh duy nhất (ví dụ: http://dbpedia.org/resource/Nguyen_Dynasty).

Name: Tên triều đại (ví dụ: "Nhà Nguyễn").

Start Date: Năm bắt đầu (time:Instant, ví dụ: "1802").

End Date: Năm kết thúc (time:Instant, ví dụ: "1945").

Related Historical Figures: Nhân vật liên quan, như vua hoặc quan chức (belongsToDynasty) (ví dụ: "Gia Long").

Related Historical Sites: Di tích xây dựng trong triều đại (ví dụ: "Kinh thành Huế").

Related Historical Events: Sự kiện diễn ra trong triều đại (ví dụ: "Hòa ước Nhâm Tuất").

Related Festivals: Lễ hội liên quan đến triều đại (ví dụ: "Lễ tế Nam Giao").

Related Administrative Divisions: Đơn vị hành chính dưới triều đại (ví dụ: "Thuận Hóa").

Provenance: Nguồn gốc dữ liệu (prov:wasDerivedFrom).

Description: Mô tả ngắn về triều đại, bao gồm bối cảnh lịch sử.
Lưu ý


Provenance: Trường prov:wasDerivedFrom là bắt buộc cho mọi chủ đề để đảm bảo tính minh bạch, đặc biệt khi dữ liệu từ DBPedia hoặc Wikidata có thể mâu thuẫn.

Thời gian: Các trường liên quan đến thời gian (birthDate, deathDate, start, end, v.v.) nên hỗ trợ cả time:Instant và time:Interval để xử lý dữ liệu không chính xác.

Tích hợp ontology chuẩn: Các trường được thiết kế để tương thích với CIDOC-CRM, Time Ontology, PROV-O, và Juso Ontology, như mô tả trong tài liệu.

SPARQL Queries: Để trích xuất, có thể sử dụng SPARQL với Property Path để truy vấn các mối quan hệ phức tạp (ví dụ: ?figure :participatesInEvent ?event).
Danh sách này có thể được điều chỉnh thêm nếu bạn có yêu cầu cụ thể về định dạng dữ liệu hoặc các trường bổ sung.
{
    Query SPAQRL cho dynasty:
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbp: <http://dbpedia.org/property/>
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX dbc: <http://dbpedia.org/resource/Category:>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX prov: <http://www.w3.org/ns/prov#>

    SELECT DISTINCT ?dynasty ?name ?startDate ?endDate ?historicalFigure ?historicalSite ?historicalEvent ?festival ?adminDivision ?provenance ?description
    WHERE {
    # Lấy các triều đại thuộc danh mục Vietnamese_dynasties
    ?dynasty dct:subject dbc:Vietnamese_dynasties .
    
    # Lọc các triều đại có dbp:governmentType chứa "Monarchy"
    ?dynasty dbp:governmentType ?govType .
    FILTER (CONTAINS(LCASE(STR(?govType)), "monarchy"))
    
    # Name: Tên triều đại
    ?dynasty rdfs:label ?name .
    FILTER (lang(?name) = "en" || lang(?name) = "vi")
    
    # Start Date: Năm bắt đầu
    OPTIONAL {
        ?dynasty dbp:startDate | dbp:established | dbo:foundingYear | dbp:formation ?startDate .
    }
    
    # End Date: Năm kết thúc
    OPTIONAL {
        ?dynasty dbp:endDate | dbp:abolished | dbo:dissolutionYear | dbp:dissolution ?endDate .
    }
    
    # Related Historical Figures: Nhân vật lịch sử
    OPTIONAL {
        ?dynasty dbp:leader | dbp:monarch | dbo:leader | dbo:founder ?historicalFigure .
        ?historicalFigure rdf:type foaf:Person .
    }
    
    # Related Historical Sites: Di tích lịch sử
    OPTIONAL {
        ?historicalSite dbp:dynasty | dbo:era | dbp:country | dbo:location ?dynasty .
        ?historicalSite rdf:type dbo:Place .
    }
    
    # Related Historical Events: Sự kiện lịch sử
    OPTIONAL {
        ?historicalEvent dbp:dynasty | dbo:era | dbp:country ?dynasty .
        ?historicalEvent rdf:type dbo:Event .
    }
    
    # Related Festivals: Lễ hội
    OPTIONAL {
        ?festival dbp:dynasty | dbo:era | dbp:country ?dynasty .
        ?festival rdf:type dbo:Festival .
    }
    
    # Related Administrative Divisions: Đơn vị hành chính
    OPTIONAL {
        ?adminDivision dbp:dynasty | dbo:country | dbp:era | dbo:location ?dynasty .
        ?adminDivision rdf:type dbo:AdministrativeRegion .
    }
    
    # Provenance: Nguồn gốc dữ liệu
    OPTIONAL {
        ?dynasty prov:wasDerivedFrom ?provenance .
    }
    
    # Description: Mô tả ngắn
    OPTIONAL {
        ?dynasty dbo:abstract ?description .
        FILTER (lang(?description) = "en" || lang(?description) = "vi")
    }
    }
    LIMIT 100
}

list triều đại: https://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=PREFIX+dct%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0APREFIX+dbc%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2FCategory%3A%3E%0D%0APREFIX+dbp%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fproperty%2F%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fdynasty+%3Fname%0D%0AWHERE+%7B%0D%0A++%23+L%E1%BA%A5y+c%C3%A1c+tri%E1%BB%81u+%C4%91%E1%BA%A1i+thu%E1%BB%99c+danh+m%E1%BB%A5c+Vietnamese_dynasties%0D%0A++%3Fdynasty+dct%3Asubject+dbc%3AVietnamese_dynasties+.%0D%0A++%0D%0A++%23+Duy%E1%BB%87t+c%C3%A1c+thu%E1%BB%99c+t%C3%ADnh+c%C3%B3+gi%C3%A1+tr%E1%BB%8B+ch%E1%BB%A9a+%22monarchy%22%0D%0A++%3Fdynasty+%3Fproperty+%3FgovType+.%0D%0A++FILTER+%28%0D%0A++++%3Fproperty+IN+%28dbp%3AgovernmentType%2C+dbp%3Agovernment%29+%26%26%0D%0A++++CONTAINS%28LCASE%28STR%28%3FgovType%29%29%2C+%22monarchy%22%29%0D%0A++%29%0D%0A++%0D%0A++%23+L%E1%BA%A5y+t%C3%AAn+tri%E1%BB%81u+%C4%91%E1%BA%A1i%0D%0A++%3Fdynasty+rdfs%3Alabel+%3Fname+.%0D%0A++FILTER+%28lang%28%3Fname%29+%3D+%22en%22+%7C%7C+lang%28%3Fname%29+%3D+%22vi%22%29%0D%0A%7D%0D%0AORDER+BY+%3Fname%0D%0ALIMIT+50&format=text%2Fhtml&timeout=30000&signal_void=on&signal_unconnected=on

-> kết quả triều đại stored ở file DbPediaResult/dynasty_uri.json -> duyệt file này để query các field cân thiết cho dynasty