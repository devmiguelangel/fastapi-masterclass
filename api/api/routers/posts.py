from fastapi import APIRouter

from api.schemas.posts import PostCreateSchema

router = APIRouter(
    prefix='/posts',
    tags=['posts'],
)

@router.get('/')
def get_posts():
    return {'data': 'blog posts'}

@router.post('/')
def create_post(new_post: PostCreateSchema):
    return {'data': new_post}
