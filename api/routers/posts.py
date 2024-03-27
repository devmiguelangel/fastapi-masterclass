from random import randrange

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response

from schemas.posts import PostSchema

router = APIRouter()

my_posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the content of the first post'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the content of the second post'},
    {'id': 3, 'title': 'Third Post', 'content': 'This is the content of the third post'},
]

@router.get('/posts')
async def get_posts():
    return {'data': my_posts}


@router.get('/posts/{id}')
async def get_post(id: int, response: Response):
    post = list(filter(lambda x: x['id'] == id, my_posts))

    if post:
        return {'detail': post[0]}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')


@router.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_posts(post: PostSchema):
    data = post.model_dump()
    data['id'] = randrange(1, 1000000)
    my_posts.append(data)

    return {'data': data}


@router.put('/posts/{id}')
async def update_post(id: int, post: PostSchema):
    post_index = None

    for i, p in enumerate(my_posts):
        if p['id'] == id:
            post_index = i
            break

    if post_index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exist')

    my_posts[post_index] = post.model_dump()
    my_posts[post_index]['id'] = id

    return {'data': my_posts[post_index]}


@router.delete('/posts/{id}')
async def delete_post(id: int):
    post_index = None

    for i, post in enumerate(my_posts):
        if post['id'] == id:
            post_index = i
            break

    if post_index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exist')

    my_posts.pop(post_index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
