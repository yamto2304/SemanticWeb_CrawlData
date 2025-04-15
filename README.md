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