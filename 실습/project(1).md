# pjt-01

### 버전2_영화
```python
def book_info(book):
    # 여기에 코드를 작성합니다.
    info_book = {}
    info_book['id'] = book['id']
    info_book['title'] = book['title']
    info_book['author'] = book['author']
    info_book['priceSales'] = book['priceSales']
    info_book['description'] = book['description']
    info_book['cover'] = book['cover']
    info_book['categoryId'] = book['categoryId']
    return info_book
```
- 데이터를 열어서 json파일로 만들고 그 데이터를 book_info 함수에서 새로운 딕셔너리에 내가 원하는 데이터들만 넣어서 만드는 함수를 만들었습니다.
- 첫 번째 문제인 만큼 큰 어려움은 없었고, 단지 딕셔너리에 키값과 밸류값을 넣을 때, 이런 방법 말고 다른 방법은 없나? 라는 의문을 가지긴 했습니다.

```python
def book_info(book, categories):
    categoryName = []
    for categorie in categories:
        if categorie['id'] in book['categoryId']:
            categoryName.append(categorie['name'])

    info_book = {}
    info_book['id'] = book['id']
    info_book['title'] = book['title']
    info_book['author'] = book['author']
    info_book['priceSales'] = book['priceSales']
    info_book['description'] = book['description']
    info_book['cover'] = book['cover']
    info_book['categoryId'] = categoryName
    return info_book
```
- 두 번째 문제는 첫 번째 문제에서 categoryId에 해당하는 부분의 밸류를 categoires를 가져와 거기에 해당하는 name로 바꿔주는 것 이였습니다.
- 이 문제는 categories부분을 건들여서 값 비교 후 원하는 값을 넣어주면 되는 비교적 쉬운 문제였습니다.
- 해당 문제를 풀기위해 배웠던 for문과 if문을 활용해서 문제를 해결하였습니다.

```python
    info_books = []
    for book in books:
        categoryName = []
        book_info = {}

        for categorie in categories:
            if categorie['id'] in book['categoryId']:
                categoryName.append(categorie['name'])

        book_info['id'] = book['id']
        book_info['title'] = book['title']
        book_info['author'] = book['author']
        book_info['priceSales'] = book['priceSales']
        book_info['description'] = book['description']
        book_info['cover'] = book['cover']
        book_info['categoryId'] = categoryName

        info_books.append(book_info)

    return info_books
```
- 해당 문제는 앞에서 나온 문제를 이제 한권의 책이 아닌 여러권의 책들을 필터링 하는 과정이였습니다.
- 문제를 해결하기 위해 book_info를 for문안에 넣어서 여러 개의 딕셔너리로 이루어진 리스트를 받아 하나씩 넣어서 새로운 리스트인 info_books에 넣어줘 해결했습니다.

```python
    for book in books:
        book_json = open(f"data/books/{book['id']}.json", encoding='utf-8')
        book_list = json.load(book_json)
        if book_list['customerReviewRank'] > max_customer_review_rank:
            max_user = book_list['title']
            max_customer_review_rank = book_list['customerReviewRank']
    return max_user

```
-  이번 문제는 리뷰가 가장 좋은 책을 구해와서 사용하는 것 입니다.
-  이번엔 초기값이 -1인 변수를 구해와서 for문 속 if문을 통해 변수보다 클 때만 변수에 새로 할당하고 그 유저 정보를 담아와서 리턴을 하였습니다.

```python
def new_books(books):
    # 여기에 코드를 작성합니다.
    result = []
    for book in books:
        book_json = open(f"data/books/{book['id']}.json", encoding='utf-8')
        book_list = json.load(book_json)
        pubdate = book_list['pubDate'].split('-')
        if pubdate[0] == '2023':
            result.append(book_list['title'])
    return result
```
- 이번 문제에서 저는 if in을 사용하면 해당 문자가 있으면 바로 걸리는줄 알고 split를 쓰지않고 원본 데이터에 바로 if문을 걸어서 2023을 거르려고 했습니다.
- 하지만 그렇게 출력해본 결과 빈 리스트가 출력이 되어서 그렇게 해서는 안된다고 느꼈습니다.
- 그래서 저는 인덱스를 활용하기 위해 split를 사용해서 인덱스값을 활용해서 문제를 해결하였습니다.

```python
for book in books:
        book_json = open(f"data/books/{book['id']}.json", encoding='utf-8')
        book_list = json.load(book_json)
        pubdate = book_list['pubDate'].split('-')
        if pubdate[0] == '2023':
            if book_list['customerReviewRank'] > max_customer_review_rank:
                max_user = book_list['title']
                max_customer_review_rank = book_list['customerReviewRank']
```
- 이번 문제에서 어려웠던 점은 딱히 없었습니다.

```python
def sorted_cs_books_by_price(books, categories):
    result = []
    cs_id = None
    
    # 컴퓨터 공학 카테고리 ID 찾기
    for categorie in categories:
        if categorie['name'] == '컴퓨터 공학':
            cs_id = categorie['id']
            break

    for book in books:
        book_json = open(f"data/books/{book['id']}.json", encoding='utf-8')
        book_list = json.load(book_json)
        
        category_id = book_list['categoryId']
            
        # categoryId가 리스트인 경우와 정수인 경우를 모두 처리
        if (isinstance(category_id, list) and cs_id in category_id) or category_id == cs_id:
                result.append((book_list['title'], book_list['priceSales']))
    
    
    # 가격 기준으로 정렬
    result_sort = sorted(result, key=lambda x:x[1])
```
- 이번 문제에선 처음부터 고비였습니다 먼저 카테고리를 활용하지 않아서 잠깐 헤메다가 카테고리가 새로 추가 된 것을 확인하고 이용하기로 했습니다.
- json파일을 확인하고 컴퓨터공학에 해당하는 id값을 가져와 변수로 사용했다가 문제에서 요구하는 것이 이것이 아니고 categorie를 활용해서 컴퓨터 공학이라는 이름을 가진 id를 요구하는 것이라고 생각해 for문을 돌려 먼저 cs_id를 뽑아냈습니다.
- 그 후 cs_id와 일치되는 book_list['categoryId']를 찾기위해 if문 for문을 돌려도 list인 경우와 int인 경우가 있어서 확실히 해결되지 않았습니다. 그래서 GPT의 힘을 빌려서 isinstance라는 내장함수를 찾아내서 문제를 해결하였습니다.
- 마지막으로 sort를 하는 방법을 몰라서 여러번의 검색결과 lambda를 활용하면 내가 원하는 인덱스값을 기준으로 내림차순을 할 수 있어서 문제를 해결 할수 있었습니다.


### 느낀점
- API활용을 하는 것이 어렵다고 늘 생각해왔는데 이번 프로젝트를 통해서 조금이나마 API활용하는 실력이 늘었다고 생각합니다.