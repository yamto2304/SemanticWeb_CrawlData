I. Query dữ liệu dynasty:
=========
```
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?dynasty ?_founderOfDynasty ?_formedIn ?_start ?_end ?_span
WHERE {
    VALUES ?dynasty {
        <http://dbpedia.org/resource/Lý_dynasty>
        <http://dbpedia.org/resource/Early_Lý_dynasty>
        <http://dbpedia.org/resource/Đinh_dynasty>
        <http://dbpedia.org/resource/Mạc_dynasty>
        <http://dbpedia.org/resource/Lê_dynasty>
        <http://dbpedia.org/resource/Trần_dynasty>
        <http://dbpedia.org/resource/Nguyễn_dynasty>
        <http://dbpedia.org/resource/Ngô_dynasty>
        <http://dbpedia.org/resource/Revival_Lê_dynasty>
    }
    OPTIONAL { ?dynasty dbp:founder ?_founderOfDynasty . }
    OPTIONAL { ?dynasty dbp:eventStart ?_formedIn . }
    OPTIONAL { ?dynasty dbp:yearStart ?_start . }
    OPTIONAL { ?dynasty dbp:yearEnd ?_end . }
    BIND(xsd:integer(?_end) - xsd:integer(?_start) AS ?_span)
}
```
Note: Missing _founderOfDynasty at some dynasties

II. Query dữ liệu Historical Figures and their Degrees
===============

1. Triều Lý
```
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gold: <http://purl.org/linguistics/gold/>

SELECT DISTINCT ?person 
       (GROUP_CONCAT(DISTINCT ?_son; separator=", ") AS ?_son)
       (GROUP_CONCAT(DISTINCT ?_birthPlace; separator=", ") AS ?_birthPlace)
       (GROUP_CONCAT(DISTINCT ?_deathPlaces; separator=", ") AS ?_deathPlaces)
       (GROUP_CONCAT(DISTINCT ?_father; separator=", ") AS ?_fathers)
       (GROUP_CONCAT(DISTINCT ?_fullName; separator=", ") AS ?_fullNames)
       (GROUP_CONCAT(DISTINCT ?_mother; separator=", ") AS ?_mothers)
       (GROUP_CONCAT(DISTINCT ?_religion; separator=", ") AS ?_religions)
       (GROUP_CONCAT(DISTINCT ?_positionTitle; separator=", ") AS ?_positionTitles)
       (GROUP_CONCAT(DISTINCT ?_buriedPlace; separator=", ") AS ?_buriedPlace)
       (GROUP_CONCAT(DISTINCT ?deathCategory; separator=", ") AS ?deathCategories)
       (GROUP_CONCAT(DISTINCT ?_deathDate; separator=", ") AS ?_deathDates)
       (GROUP_CONCAT(DISTINCT ?_liveIn; separator=", ") AS ?_liveIn)
WHERE {
    <http://dbpedia.org/resource/Lý_dynasty> ?property ?person .
    ?person rdf:type ?type .
    FILTER(?type IN (
        dbo:Person,
        <http://xmlns.com/foaf/0.1/Person>,
        <http://schema.org/Person>,
        <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#NaturalPerson>,
        <http://dbpedia.org/class/yago/Person100007846>
    ))
    OPTIONAL {
        ?person dbo:wikiPageWikiLink ?deathCategory .
        FILTER regex(STR(?deathCategory), "deaths$", "i")
    }
    OPTIONAL { ?person dbo:child ?_son . }
    OPTIONAL { ?person dbp:birthPlace ?_birthPlace . }
    OPTIONAL { ?person dbp:deathPlace ?_deathPlaces . }
    OPTIONAL { ?person dbp:father ?_father . }
    OPTIONAL { ?person dbp:fullName ?_fullName . }
    OPTIONAL { ?person dbp:mother ?_mother . }
    OPTIONAL { ?person dbp:religion ?_religion . }
    OPTIONAL { ?person gold:hypernym ?_positionTitle. }
    OPTIONAL { ?person dbp:placeOfBurial ?_buriedPlace. }
    OPTIONAL { ?person dbp:deathDate ?_deathDate . }
    BIND("http://dbpedia.org/resource/Lý_dynasty" AS ?_liveIn)
}
GROUP BY ?person
```
Note: Một số nhân vật không có con, không rõ nơi sinh, nơi sinh bị lẫn field thừa: http://dbpedia.org/resource/Names_of_Vietnam, http://dbpedia.org/resource/Đại_Cồ_Việt
http://dbpedia.org/resource/Lý_dynasty
Field yago:Person100007846 khong phai la nguoi!

Thay tên triều Lý bằng các triều đại khác trong List:
```
    <http://dbpedia.org/resource/Lý_dynasty>
    <http://dbpedia.org/resource/Early_Lý_dynasty>
    <http://dbpedia.org/resource/Đinh_dynasty>
    <http://dbpedia.org/resource/Mạc_dynasty>
    <http://dbpedia.org/resource/Lê_dynasty>
    <http://dbpedia.org/resource/Trần_dynasty>
    <http://dbpedia.org/resource/Nguyễn_dynasty>
    <http://dbpedia.org/resource/Ngô_dynasty>
    <http://dbpedia.org/resource/Revival_Lê_dynasty>
```