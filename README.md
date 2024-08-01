# API Documentation (Django)

使用者註冊

## **使用者註冊：POST api/user_register/**

- params：NO
- Requst：JSON格式
- Response：JSON格式
- Request Body:

```jsx
{
    "username":"jimmy",
    "user_password":"home1234",
    "user_check_password":"home1234",
    "user_email":"jimmybob850513@gmail.com"
}
```

- Response 200

```jsx
{
    "msg": "帳號註冊成功",
    "status_code": 200
}
```

- Response 500

帳號已存在的狀況下：

```jsx
{
    "msg": "該帳號已存在",
    "status_code": 500
}
```

未輸入使用者帳號：

```jsx
{
    "msg": "使用者帳號不得為空！",
    "status_code": 500
}
```

密碼跟確認密碼不符合：

```jsx
{
    "msg": "密碼跟確認密碼不符合！",
    "status_code": 500
}
```

email輸入錯誤：

```jsx
{
    "msg": "email輸入格式錯誤！",
    "status_code": 500
}
```

## **使用者登入：POST api/user_login/**

- params：NO
- Requst：JSON格式
- Response：JSON格式
- Request Body:

```jsx

{
    "username":"jimmy",
    "password":"home1234"
}
```

- Response 200

```sql
{
    "username": "jimmy",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMTk2MTgyOSwiaWF0IjoxNzIxODc1NDI5LCJqdGkiOiIxMjQxMjA1ZDE3ZWI0NTllYTA0ZDZhY2M3ZmYwY2NmOSIsInVzZXJfaWQiOjN9.-eh5yYk3cG6X1WJSUim3IRjsD1nfIQ7h4xlXaydjIFc",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg"
}
```

- Response 500

```sql
{
    "msg": "帳號密碼錯誤或是要先去註冊！"
}
```

## **取得當前登入使用者的資料： GET api/user_profile**

- params：NO
- Requst：JSON格式
- Response：JSON格式
- Request Head：

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body:

```sql
{
	"username":"jimmy"
}
```

- Response 200

```sql
{
    "user_id": 2,
    "user_name": "jimmy",
    "user_email": "jimmybob850513@gmail.com",
    "user_birthday": null,
    "tel": null,
    "mobile": null,
    "city": null,
    "district": null,
    "zip": null,
    "addr": null
}
```

- Response 404

```sql
{
    "msg": "使用者的資料找不到",
    "status":404
}
```

- Response 401 不是有效的token

```sql
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```

- Response 401 未提供身份令牌：

```sql
{
    "detail": "Authentication credentials were not provided."
}
```

## 更新使用者的資訊  **PUT api/user_profile/**

- params：NO
- Requst：JSON格式
- Response：JSON格式
- Request Head：

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body:

```sql
{
    "user_birthday": null,
    "tel": null,
    "mobile": null,
    "city": null,
    "district": null,
    "zip": null,
    "addr": null
}
```

- Response 200

```sql
{
    "user_id": 1,
    "user_name": "jimmy",
    "user_email": "jimmybob850513@gmail.com",
    "user_birthday": "1996-05-13",
    "tel": "0975783566",
    "mobile": "0975783566",
    "city": "新北市",
    "district": "板橋區2",
    "zip": "220",
    "addr": "莒光路205號",
    "msg": "更新成功"
}
```

- Response 401

```sql
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```

- Response 500

```sql
{"msg":"找不到使用者！",'status':status.HTTP_404_NOT_FOUND}
```

## 查看所有文章 GET /api/post_views/

- params：NO
- Requst
- Response 200

```sql
[
    {
        "post_id": 1,
        "user_name": "jimmy",
        "user_id": 1,
        "post_title": "今天天氣真好",
        "post_content": "api測試用的",
        "created_at": "2024-07-25",
        "updated_at": "2024-07-25"
    },
    {
        "post_id": 2,
        "user_name": "jimmy",
        "user_id": 1,
        "post_title": "今天天氣真好",
        "post_content": "api測試用的",
        "created_at": "2024-07-25",
        "updated_at": "2024-07-25"
    }
]
```

如果裡面沒有文章的話：

```sql
{
    "msg": "目前無文章",
    "status": 200
}
```

## 新增文章 POST /api/post_views/

- params：NO
- Requst：JSON格式
- Response：JSON格式
- Request Head：

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body:

```sql
{   
    "post_title":"今天天氣真好",
    "post_content":"api測試用的"
}
```

- Response 201

```sql
{
    "msg": "文章創建成功",
    "post_id": 3
}
```

- Response 400

```sql
{
	"msg":"無效用戶信息"
}
```

## 查看當前使用者的個人文章: GET api/post_views_personal/

- params：NO
- Response：JSON格式
- Request Head：

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Response 200

```sql
{
    "msg": "個人文章找到了",
    "post": [
        {
            "post_id": 4,
            "user_name": "judy",
            "user": 2,
            "post_title": "最近颱風天",
            "post_content": "颱風天真危險,只能在家吃泡麵！"
        },
        {
            "post_id": 5,
            "user_name": "judy",
            "user": 2,
            "post_title": "健身對身體的好處",
            "post_content": "健身可以增加基礎代謝率之外,還可以有增加肺活量"
        }
    ],
    "status": 200
}
```

```sql
{"msg":"目前還未張貼個人文章",
"status":status.HTTP_200_OK}
```

- Response 403

```sql
{
	"msg":"無效用戶,請先登入",
	"status":status.HTTP_403_FORBIDDEN
}
```

## 依據文章編號查找當前使用者的單一文章：GET /api/post_views_by_id/<int:id>/

- parameters :  id
- Request Head：

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Response 200

```sql
{
    "msg": "最近颱風天的文章找到了",
    "post_detail": {
        "post_title": "最近颱風天",
        "post_content": "颱風天真危險,只能在家吃泡麵！"
    },
    "status": 200
}
```

- Response 404

```sql
{
    "msg": "使用者無該文章",
    "status": 404
}
```

## 依據文章編號更新當前使用者的單一文章：PUT /api/post_views_by_id/<int:id>/

- parameters :  id
- Request Head：

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body:

```sql
{
    "post_title":"颱風天的文章更新",
    "post_content":"颱風天真危險,只能在家吃泡麵！更新文章,因為颱風天其實可以叫pizza"
}
```

- Response 200

```sql
{
    "msg": "更新成功",
    "post_detail": {
        "post_title": "颱風天的文章更新",
        "post_content": "颱風天真危險,只能在家吃泡麵！更新文章,因為颱風天其實可以叫pizza"
    },
    "status": 200
}
```

- Response 500

```sql
{
    "msg": "更新需要文章的title,不得為空",
    "status": 500
}
```

```sql
{
    "msg": "更新需要文章的content,不得為空",
    "status": 500
}
```

- Response 403

```sql
{
	"msg":"權限不足,無法訪問",
	"status":403
}
```

## 依據文章編號刪除當前使用者的單一文章：DELETE /api/post_views_by_id/<int:id>/

- parameters :  id
- Request Head：

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body:

```sql
{
    "is_check_delete":"Y"
}
```

- Response 202

```
{
    "msg": "刪除成功！",
    "status": 202
}
```

- Response 404

```sql
{
    "msg": "找不到該文章無法刪除",
    "status": 404
}
```

- Response 403

```sql
{
	"msg":"權限不足,無法訪問,請先登入",
	"status":403
}
```

## 查看指定的貼文 GET api/post_views_specific/<int:id>

- parameters :  id
- Request_head : No
- Request Body :No
- Response 200 :

```sql
{
    "post_id": 3,
    "user_name": "jimmy",
    "user": 1,
    "post_title": "今天天氣真好",
    "post_content": "api測試用的"
}
```

- Response 404

```sql
{
    "msg": "該文章已被刪除了,目前找不到該文章",
    "status": 404
}
```

## 在指定貼文下面留言 POST api/post_views_specific/<int:id>

- parameters :  id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body :

```sql
{
	"post_comment":"你說的對,API測試成功"
}
```

- Response 200

```sql
{
	"msg":"新增成功"
	"status":200
}
```

- Response 404 (找不到該文章)

```sql
{
    "msg": "目前找不到該文章,無法進行留言",
    "status": 404
}
```

- Response 500 （避免用戶輸入無效資料）

```sql
{
    "msg": "要輸入comment進行留言",
    "status": 500
}
```

- Response 403 (權限不足)

```sql
{
    "msg": "權限不足,請先登入取得token才可以留言",
    "status": 403
}
```

## 更新指定貼文下,當前使用者的留言 PUT api/post_views_comment/<int:comment_id>

- parameters :  comment_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body :

```sql
{
    "post_comment":"我要更新jimmy的留言！update by jimmy"
}
```

- Response 200

```sql
{
    "msg": "更新成功",
    "status": 200
}
```

```sql
{
    "post_id": 5,
    "user_name": "judy",
    "user": 2,
    "post_title": "健身對身體的好處",
    "post_content": "健身可以增加基礎代謝率之外,還可以有增加肺活量",
    "post_comments": [
        [
            {
                "comment_id": 2,
                "user_name": "judy",
                "user_id": 2,
                "comment": "我要更新我自己的留言！update by judy",
                "post_id": 5,
                "created_at": "2024-07-28",
                "update_at": "2024-07-28"
            },
            {
                "comment_id": 4,
                "user_name": "jimmy",
                "user_id": 1,
                "comment": "我要更新jimmy的留言！update by jimmy",
                "post_id": 5,
                "created_at": "2024-07-28",
                "update_at": "2024-07-28"
            }
        ]
    ]
}
```

- Response 403

```sql
{
    "msg": "請選擇你自己的留言進行更新,無權限更新他人的留言",
    "status": 403
}
```

- Response 500

```sql
{
    "msg": "更新失敗,要輸入要更新的內容！",
    "status": 500
}
```

- Response 403

```sql
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired",
            "message_customer": "不是有效的token,請重新登入獲取新的token！"
        }
    ]
}
```

## 刪除指定貼文下,當前使用者的留言 DELETE api/post_views_comment/<int:comment_id>

- parameters :  comment_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 200

```sql
{
    "msg": "刪除成功",
    "status": 200
}
```

- Response 403

```sql
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired",
            "message_customer": "不是有效的token,請重新登入獲取新的token！"
        }
    ]
}
```

## 追隨使用者 POST api/user_follow/<int:user_id>

- parameters :  comment_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 200

```sql
{"msg":"追隨成功",
"status":201}
```

- Response 404

```sql
{
	"msg":"追蹤的使用者不存在",
	"status":404
}
```

- Response 403

```sql
{
"msg":"權限不足請先登入",
"status":403
}
```

- Response 500

```sql
{
"msg":"你不能追隨你自己",
"status":500
}
```

```sql
{
"msg":"目前已追隨該使用者了",
"status":500
}
```

## 查看你追隨的使用者的資料跟貼文 GET api/user_follow/<int:user_id>

- parameters :  comment_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 200

```sql
{
    "msg": "查看該使用者的資料成功",
    "user_profile": {
        "user_id": 1,
        "user_name": "jimmy",
        "user_email": "jimmybob850513@gmail.com"
    },
    "user_post": [
        {
            "post_id": 3,
            "user_name": "jimmy",
            "user_id": 1,
            "post_title": "今天天氣真好",
            "post_content": "api測試用的",
            "created_at": "2024-07-25",
            "updated_at": "2024-07-25"
        }
    ]
}
```

- Response 403

```sql
{
"msg":"使用者尚未追隨,請先追隨,在查看他的貼文跟資料",
"status":403
}
```

- Response 500

```sql
{
	"msg":"查看你個人的訊息可以到自己的主頁查看喔！！",
	"status":500
}
```

- Response 404

```sql
{
"msg":"找不到該位追隨使用者的資料",
'status':404
}
```

## 取消追隨使用者 PATCH api/user_follow/<int:user_id>

- parameters :  comment_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 202

```sql
{
"msg":"取消追蹤成功",
"status":202
}
```

- Response 404

```sql
{
    "msg": "尚未追蹤該位使用者",
    "status": 404
}
```

- Response 500

```sql
{"msg":"取消追蹤操作失敗","status":500}
```

- Response 403

```sql
{
"msg":"權限不足請先登入",
"status":403
}
```

查看當前使用者有追隨的對象 api/user_follow_all/

- parameters :  comment_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 200

```sql
{
    "msg": "你的追隨的名單已找到",
    "status": 200,
    "追隨的名單": [
        {
            "user_id": 2,
            "user_name": "judy"
        },
        {
            "user_id": 1,
            "user_name": "jimmy"
        }
    ]
}
```

```sql
{
    "msg": "目前你暫無追隨的使用者",
    "status": 200
}
```

- Response 403

```sql
{
"msg":"權限不足請先登入",
"status":403
}
```

## 查看當前使用者喜歡所有的貼文 GET api/user_follow_post/

- parameters :  NO
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 200

```powershell
{
    "msg": "adam所喜歡的文章",
    "data": [
        {
            "id": 2,
            "post_id": 2,
            "user_id": 4,
            "user_name": "adam",
            "like_post": true,
            "like_post_start_date": "2024-08-01",
            "cancel_start_date": "2024-08-01"
        },
        {
            "id": 3,
            "post_id": 1,
            "user_id": 4,
            "user_name": "adam",
            "like_post": true,
            "like_post_start_date": "2024-08-01",
            "cancel_start_date": "2024-08-01"
        },
        {
            "id": 4,
            "post_id": 3,
            "user_id": 4,
            "user_name": "adam",
            "like_post": true,
            "like_post_start_date": "2024-08-01",
            "cancel_start_date": "2024-08-01"
        },
        {
            "id": 5,
            "post_id": 4,
            "user_id": 4,
            "user_name": "adam",
            "like_post": true,
            "like_post_start_date": "2024-08-01",
            "cancel_start_date": "2024-08-01"
        }
    ],
    "status": 200
}
```

如果當前無喜歡的貼文的話：

```powershell
{
"msg":"目前無喜歡的文章",
"status":200
}
```

- Response 403

```powershell
{
"msg":"權限不足請先登入",
"status":403
}
```

- Response 500

```powershell
{
"msg":"伺服器發生錯誤",
"status":500
}
```

## 新增當前使用者喜歡的貼文 POST api/user_follow_post/

- parameters :  NO
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body :

```powershell
{"post_id":post_id}
```

- Response 200

```powershell
{
"msg":"Adam喜歡文章1成功",
"status":200
}
```

- Response 400

```powershell
{
"msg":"請輸入你要追蹤的文章編號！",
"status":400
}
```

- Response 404

```powershell
{
"msg":"找不到該篇文章,文章主人可能已經刪除了",
"status":404
}
```

- Response 500

```powershell
{
"msg":"伺服器發生錯誤",
"status":500
}
```

- Response 403

```powershell
{
"msg":"權限不足請先登入",
"status":403
}
```

查看當前使用者特定的喜歡貼文 GET api/user_liked_post_spec/<int:post_id>/

- parameters :  post_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 200

```powershell
{
    "msg": "找到該文章成功",
    "data": {
        "post_id": 3,
        "user_name": "judy",
        "user": 2,
        "post_title": "我是judy使用者,目前測試API",
        "post_content": "API測試可以正常建立貼文,後續進行喜歡貼文的追蹤"
    },
    "status": 200
}
```

- Response 400

```powershell
{
    "msg": "該文章文自己的文章",
    "status": 400
}
```

```powershell
{
    "msg": "尚未喜歡該文章,要先去喜歡才可以查看",
    "status": 400
}
```

- Response 404

```powershell
{
    "msg": "找不到該文章,可能已經被刪除了",
    "status": 404
}
```

- Response 403

```powershell
{
"msg":"權限不足請先登入",
"status":403
}
```

## 取消當前使用者的文章追蹤 PATCH api/user_liked_post_spec/<int:post_id>/

- parameters :  post_id
- Request_head :

```sql
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxODc3MjI5LCJpYXQiOjE3MjE4NzU0MjksImp0aSI6IjUxYzg5MDVlZTFlYjRhNzc5NzczZjg1Yjk3Y2ZlMWVmIiwidXNlcl9pZCI6M30.lAuO6MV7NGwLg60BBkks-mT3ufzdRmWMPE0FBqQTLQg
```

- Request Body : NO
- Response 200

```powershell
{
"msg":"取消追蹤成功",
"status":200
}
```

- Response 400

```powershell
{
"msg":"該文章文自己的文章,不可以取消追蹤",
"status":400
}
```

```powershell
{
"msg":"尚未喜歡該文章,無法執行取消追蹤",
"status":400
}
```

- Response 404

```powershell
{
"msg":"找不到該文章,可能已經被刪除了",
"status":404
}
```

- Response 403
```powershell
{
"msg":"權限不足請先登入",
"status":403
}
```
