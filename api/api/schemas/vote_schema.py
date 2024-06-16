
from pydantic import UUID4, BaseModel, conint


class VoteSchema(BaseModel):
    post_id: UUID4
    dir: conint(ge=0, le=1)
