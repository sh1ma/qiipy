from apywrapper import Apy, get, delete
from ._models import Comment


class Qiipy(Apy):
    def __init__(self, access_token: str, host: str = "https://qiita.com"):
        super().__init__(host=host, headers={"Authorization": f"Bearer {access_token}"})

    @get("/api/v2/comments/{comment_id}")
    def get_comment(self, comment_id: str):
        """コメントを取得する

        Args:
            comment_id: コメントid
        Returns:
            Commentオブジェクト
        """
        return Comment, {"comment_id": comment_id}

    @delete("/api/v2/comments/{comment_id}")
    def delete_comment(self, comment_id: str):
        """コメントを削除する

        Args:
            comment_id: コメントid
        Returns:
            None
        """
        return None, {"comment_id": comment_id}
