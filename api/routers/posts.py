from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response

from schemas.posts import PostCreateSchema, PostResponseSchema
from services.post_service import PostService

router = APIRouter()
post_service = PostService()

@router.get('/posts', response_model=list[PostResponseSchema])
async def get_posts():
    posts = await post_service.get_all()
    return posts


@router.get('/posts/{id}')
async def get_post(id: int, response: Response):
    post = await post_service.get_one(id)

    if post:
        return post

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')


@router.post('/posts', status_code=status.HTTP_201_CREATED, response_model=PostResponseSchema)
async def create_posts(post: PostCreateSchema):
    new_post = await post_service.create(post)

    return new_post


@router.put('/posts/{id}')
async def update_post(id: int, post: PostCreateSchema):
    post_updated = await post_service.update(id, post)

    if not post_updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exist')

    return post_updated


@router.delete('/posts/{id}')
async def delete_post(id: int):
    deleted = await post_service.delete(id)

    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exist')

    return Response(status_code=status.HTTP_204_NO_CONTENT)
