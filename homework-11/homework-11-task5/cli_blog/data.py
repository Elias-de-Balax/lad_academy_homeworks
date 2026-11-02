_posts: list[dict] = []

def create_post(title: str, author: str, text: str) -> dict:
    post = {"title": title, "author": author, "text": text}
    _posts.append(post)

    return post

def list_posts() -> list[dict]:
    return list(_posts)

def find_post(title: str) -> dict | None:
    for post in _posts:
        if title in post["title"]:
            return post

    return None