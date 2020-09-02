from typing import Literal, Optional

from apywrapper import Apy, delete, get, patch, post, put
from httpx import HTTPStatusError

from ._models import Comment, Tag


class Qiipy(Apy):
    def __init__(self, access_token: str, host: str = "https://qiita.com/api/v2"):
        super().__init__(host=host, headers={"Authorization": f"Bearer {access_token}"})

    @get("/comments/{comment_id}")
    def get_comment(self, comment_id: str):
        """コメントを取得する

        Args:
            comment_id: コメントid
        Returns:
            Comment
        """
        return Comment, {"comment_id": comment_id}

    @delete("/comments/{comment_id}")
    def delete_comment(self, comment_id: str):
        """コメントを削除する

        Args:
            comment_id: コメントid
        Returns:
            None
        """
        return None, {"comment_id": comment_id}

    @patch("/comments/{comment_id}")
    def update_comment(self, comment_id: str, comment_text: str):
        """コメントを更新する

        Args:
            comment_id: コメントid
            comment_text: コメントの本文
        Returns:
            Comment
        """
        return Comment, {"comment_id": comment_id, "body": comment_text}

    @get("/items/{item_id}/comments")
    def get_all_comments(self, article_id: str):
        """記事についているコメントをすべて取得する

        Args:
            article_id: 記事id(item_id)
        Returns:
            List[Comment]
        """
        return Comment, {"item_id": article_id}

    @post("/items/{item_id}/comments")
    def send_comment(self, article_id: str, comment_text: str):
        """記事にコメントを投稿する

        Args:
            article_id: 記事id(item_id)
        Returns:
            Comment
        """
        return Comment, {"item_id": article_id, "body": comment_text}

    @get("/tags")
    def get_tags(
        self,
        page: int = 1,
        per_page: int = 20,
        sort: Optional[Literal["count", "name"]] = None,
    ):
        """タグ一覧を取得する

        Args:
            page: ページ数
            per_page: 1ページあたりのタグ数
            sort: 並び順
        Returns:
            List[Tag]
        """
        return Tag, {"page": page, "per_page": per_page, "sort": sort}

    @get("/tags/{tag_id}")
    def get_tag(self, tag_id: str):
        """タグの詳細を取得する

        Args:
            tag_id: タグ名
        Returns:
            Tag
        """
        return Tag, {"tag_id": tag_id}

    @get("/users/{user_id}/following_tags")
    def get_following_tags(self, user_id: str, page: int = 1, per_page: int = 20):
        """ユーザがフォローしているタグ一覧を取得

        Args:
            user_id: ユーザーID
            page: ページ数
            per_page: 1ページあたりのタグ数
        Returns:
        """
        return Tag, {"user_id": user_id, "page": page, "per_page": per_page}

    @delete("/tags/{tag_id}/following")
    def delete_following_tag(self, tag_id: str):
        """タグのフォローを外します。

        Args:
            tag_id: タグ名
        Returns:
            None
        """
        return None, {"tag_id": tag_id}

    @get("/tags/{tag_id}/following")
    def _is_following_tag(self, tag_id: str):
        """

        Args:
            tag_id: タグ名
        Returns:
            None
        Raises:
            httpx.HTTPStatusError: フォローしていないタグを指定した場合に発生
        """
        return None, {"tag_id": tag_id}

    def is_following_tag(self, tag_id: str) -> bool:
        """タグをフォローしているか返します

        Args:
            tag_id: タグ名
        Returns:
            bool
        """
        try:
            self._is_following_tag(tag_id)
        except HTTPStatusError:
            return False
        return True

    @put("/tags/{tag_id}/following")
    def follow_tag(self, tag_id: str):
        """
        Args:
            tag_id: タグ名
        Returns:
            None
        Raises:
            httpx.HTTPStatusError: 既にフォローしたいた場合に発生
        """
        return None, {"tag_id": tag_id}
