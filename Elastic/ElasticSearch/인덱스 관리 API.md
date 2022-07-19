# 인덱스 관리 API

문서를 색인하기 위해서는 기본적으로 인덱스라는 그릇을 생성해야  한다.

인덱스를 통해 입력되는 문서의 필드를 정의하고 각 필드에 알맞은 데이터 타입을 지정할 수 있어야 한다.

> Index vs. Indices

엘라스틱서치를 공부하다 보면 용어가 아리송한 경우가 종종 있다. 대표적인 용어가 “색인”이라는 용어다. 색인은 데이터가 토큰화되어 저장된 자료구조를 의미하며, Index라는 단어를 번역한 것이다. 하지만 엘라스틱서치에서는 인덱스라는 용어를 색인과는 다른의미로 사용한다.

> 

- Index: 색인데이터
- Indexing: 색인하는 과정
- Indices: 매핑 정보를 저장하는 논리적인 데이터 공간

엘라스틱서치에서는 용어에 따른 혼란을 방지하기 위해 색인을 의미할 경우 “index”라는 단어를 사용하고, 매핑 정의 공간을 의미할 경우 “Indices”라는 단어로 표현한다. 이 책에서는 한글로 “인덱스”라는 용어를 사용하고 있는데 이는 “Indices”라는 용어를 번역한 것이라 이해하면된다.

- 엘라스틱서치는 사용 편의성을 위해 스키마 리스라는 기능을 제공한다. (검색시 속도나, 오류로 인해 사용을 자제하자)

### 인덱스 생성

API를 통해 인덱스를 추가 삭제가 가능하다.

```
PUT /movie    # 인덱스 생성. (스키마)
{
	"settings": {
		"number_of_shards": 3,
		"number_of_replicas": 1,
	},
	"mappings": {
		"_doc": {
			"properties": {
				"movieCd": { "type": "integer" },
				"movieNm": { "type": "text" },
				"movieNmEn": { "type": "text" },
				"prdtYear": { "type": "integer" },
				"openDt": { "type": "date" },
				"typeNm": { "type": "keyword"},
				"prdtStatNm": { "type": "keyword" },
				"nationAlt": { "type": "keyword" },
				"genreAlt": { "type": "keyword" },
				"repNationNm": { "type": "keyword" },
				"repGenreNm": { "type": "keyword" }
			}	
		}
	}
}

DELETE /movie
```



# 문서 관리 API

문서 관리 API는 실제 문서를 색인하고 조회, 수정, 삭제를 지원하는 API다. 이를 이용해 문서를 색인하고 내용을 수정하거나 삭제할 수 있다. 엘라스틱서치는 기본적으로 검색엔진이기 때문에 검색을 위해 다양한 검색 패턴을 지원하는 Search API를 별도로 제공한다. 하지만 색인된 문서의 ID를 기준으로 한 건 의 문서를 다뤄야 하는 경우 문서 관리 API를 사용한다.

문서 관리 API는 다음과 같은 세부 기능을 제공한다.

> - Index API: 한 건의 문서를 색인한다.

- Get API: 한건의 문서를 조회한다.
- Delete API: 한 건의 문서를 삭제한다.
- Update API: 한건의 문서를 업데이트한다.

> 

문서 관리 API는 기본적으로 한건의 문서를 처리하기 위한 기능을 제공하며 Single document API라고 부름 → 클러스터를 운영하다 보면 다수의 문서를 처리해야 하는 경우 Multi-document API를 제공한다.

- Multi Get API: 다수의 문서를 조회한다.
- Bulk API: 대량의 문서를 색인한다.
- Delete By Query API : 다수의 문서를 삭제한다.
- Update By Query API; 다수의 문서를 업데이트한다.
- Reindex API: 인덱스의 문서를 다시 색인한다.

```json
POST /movie/_doc/2
{
  "movieCd": "1",
  "movieNm": "살아남은 아이",
  "movieNmEn": "Last Child",
  "prdtYear": "2017",
  "openDt": "207-10-20",
  "typeNM": "장편",
  "prdtStatNm": "기타",
  "nationAlt": "한국",
  "genreAlt": "드라마/가족",
  "repNationNm": "한국",
  "repGenreNm": "드라마"
}

get /movie/_doc/2

DELETE /movie/_doc/1  # 항목삭제
```

id 값을 직접 지정하지 않고 URI에 인덱스명과 타입만 지정하면 엘라스틱 서치가 자동으로 id 값을 생성했다. 이때 id값은 UUID를 통해 무작위로 생성된다.

무작위로 생성된 Id 값 때문에 해당 문서를 업데이트 할 때 애로 사항이 생긴다. 엘라스틱서치와 동기화된 데이터베이스의 데이터가 변경됐다고 가정해보자. 데이터베이스와 주기적으로 동기화해야 하기 때문에 변경된 내용을 따라 동기화돼야할 것이다. 이를 위해서 엘라스틱서치에 색인된 _id값을 데이터베이스의 PK(Primary Key) 혹은 식별이 되는 키 값과 매칭한 정보가 어딘가에는 저장되어 관리돼야 한다.