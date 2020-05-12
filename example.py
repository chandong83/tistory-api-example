import socket
import requests 
import json
from bs4 import BeautifulSoup

import app_config
import utils

origin = 'out'
output_type = 'json' #'xml' xml 기능 구현 안됨
# https://tistory.github.io/document-tistory-apis/  # api 설명서

# https://limsee.com/325 토큰 얻는 방법

def json_parsing(response_json):
    json_text = json.dumps(response_json, indent=4, ensure_ascii=False)
    return json_text

def write_json_file(file_name, json_text):
    with open(origin + '/' + file_name,  "w", encoding='utf-8') as fp:
        fp.write(json_text)
'''
블로그 정보 얻기
'''
def blog_info():    
    '''        
    GET https://www.tistory.com/apis/blog/info?
    access_token={access-token}
    &output={output-type}

    응답
    id: 사용자 로그인 아이디
    userId: 사용자 id
    blogs
        url: 티스토리 기본 url
        secondaryUrl: 독립도메인 url
        title: 블로그 타이틀
        description: 블로그 설명
        default: 대표블로그 여부 (Y/N)
        blogIconUrl: 블로그 아이콘 URL
        faviconUrl: 파비콘 URL
        profileThumbnailImageUrl: 대표이미지 썸네일 URL
        profileImageUrl: 대표이미지 URL
        blogId: 블로그 아이디
        nickname: 블로그에서의 닉네임
        role: 블로그 권한
        statistics: 블로그 컨텐츠 개수
        post: 글 수
        comment: 댓글 수
        trackback: 트랙백 수
        guestbook: 방명록 수
        invitation: 초대장 수
    '''
    url = 'https://www.tistory.com/apis/blog/info'
    data = {'access_token': app_config.access_token, 'output': output_type}
    res = requests.get(url, params=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())        
        print(json_text)
        write_json_file('blog_info.json', json_text)

    else:
        json_text = json_parsing(res.json())
        print(json_text)

'''
해당 블로그의 카테고리 리스트 얻기
'''
def blog_category_list(blog_name):   
    '''
    GET https://www.tistory.com/apis/category/list?
    access_token={access-token}
    &output={output-type}
    &blogName={blog-name}

    blogName: Blog 이름
    '''
    url = 'https://www.tistory.com/apis/category/list' 
    data = {'access_token': app_config.access_token, 'output': output_type, 'blogName': blog_name}
    res = requests.get(url, params=data)
    
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
        write_json_file('blog_category_list_' + blog_name + '.json', json_text)
    else:        
        json_text = json_parsing(res.json())
        print(json_text)

'''
해당 블로그의 리스트 얻기
'''
def blog_list(blog_name, page):
    url = 'https://www.tistory.com/apis/post/list'
    '''
    GET https://www.tistory.com/apis/post/list?
        access_token={access-token}
        &output={output-type}
        &blogName={blog-name}
        &page={page-number}

    blogName: Blog 이름
    page: 불러올 페이지 번호입니다. 1부터 시작    
    '''
    data = {'access_token': app_config.access_token, 'output': output_type, 'blogName': blog_name, 'page': page}
    res = requests.get(url, params=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
        write_json_file('blog_list_' + blog_name + '_' + str(page) + '.json', json_text)
    else:        
        json_text = json_parsing(res.json())
        print(json_text)

'''
해당 블로그의 지정 포스트 글 읽어오기
'''
def blog_read(blog_name, post_id):
    url = 'https://www.tistory.com/apis/post/read'    
    '''
    blogName: Blog 이름
    postId: 글 ID - 리스트 얻기로 알 수 있음
    '''
    data = {'access_token': app_config.access_token, 'output': output_type, 'blogName': blog_name, 'postId': post_id}
    res = requests.get(url, params=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
        write_json_file('blog_read_' + blog_name + '_' +str(post_id) + '.json', json_text)
    else:        
        json_text = json_parsing(res.json())
        print(json_text)

'''
해당 블로그에 글 쓰기
'''
def blog_write(blog_name, category_id, title, content, tag):
    url = 'https://www.tistory.com/apis/post/write'
    visibility = 3    
    published = ''
    slogan = ''
    acceptComment = 1 
    password = ''
    '''
    blogName: Blog Name (필수)
    title: 글 제목 (필수)
    content: 글 내용
    visibility: 발행상태 (0: 비공개 - 기본값, 1: 보호, 3: 발행)
    category: 카테고리 아이디 (기본값: 0)
    published: 발행시간 (TIMESTAMP 이며 미래의 시간을 넣을 경우 예약. 기본값: 현재시간)
    slogan: 문자 주소
    tag: 태그 (',' 로 구분)
    acceptComment: 댓글 허용 (0, 1 - 기본값)
    password: 보호글 비밀번호
    '''
    data = {'access_token': app_config.access_token, 'output': output_type, 'blogName': blog_name, 'title': title, 
        'content': content, 'visibility': visibility, 'category': category_id, 'published': published, 
        'slogan': slogan, 'tag': tag, 'acceptComment': acceptComment, 'password': password}
    res = requests.post(url, data=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
        write_json_file('blog_write_'+ blog_name + '_' + category_id + '_' + title + '.json', json_text)
    else:        
        json_text = json_parsing(res.json())
        print(json_text)


'''
해당 블로그에 파일 첨부
'''
def blog_upload(blog_name, uploadedfile_path):
    '''
        POST https://www.tistory.com/apis/post/attach?
        access_token={access-token}
        &blogName={blog-name} 
        [uploadedfile]
        blogName: Blog Name 입니다.
        uploadedfile: 업로드할 파일 (multipart/form-data)
    '''
    files = {"uploadedfile": open(uploadedfile_path, 'rb')}
    url = 'https://www.tistory.com/apis/post/attach'
    data = {'access_token': app_config.access_token, 'blogName': blog_name}
    res = requests.post(url, params=data, files=files)
    print(res.url)
    if res.status_code == 200:
        print(res.text)
        
        # 업로드된 URL 주소
        soup = BeautifulSoup(res.text, 'lxml')
        url = soup.select_one('url')   
        print(url.text)

        write_json_file('blog_upload_' + blog_name + '_' + uploadedfile_path + '.txt', url.text)
    else:        
        json_result, json_text = json_parsing(res.text)
        print(json_text)



if __name__ == '__main__':

    utils.check_folder(origin)
    # 계정 블로그 정보들 읽기
    blog_info()

    # 블로그 리스트 읽기
    #blog_list('chandong83', 1)

    # 블로그 카테고리 읽기
    #blog_category_list('chandong83')

    # 게시물 작성
    #blog_write('chandong83', '0', 'title', 'test content', 'tag')

    # 게시물 읽기
    #blog_read('chandong83', 200)

    # 파일 첨부
    #blog_upload('chandong83', 'oroca.png')
