from git import Repo
import queue

result = []


def main():
    # repo = Repo(r'/Users/liuzhipeng/Downloads/学习/git操作/lzplovez')
    repo = Repo(r'/Users/liuzhipeng/Downloads/学习/git操作/git_operat')
    head_commit = repo.head.commit
    bfs(head_commit)


def bfs(start):
    visited = set()
    q = queue.Queue()
    q.put(start)  # 把起始点放入队列
    while not q.empty():
        u = q.get()
        # print(u.author.name)
        res = {'author': u.author.name, 'ID': u.hexsha, 'committer': u.committer.name}
        result.append(res)
        if u.hexsha == 'f5cd8b0902b1dd0b71549d3e918955cb10893004':
            break
        for v in u.parents:
            if v not in visited:
                visited.add(v)
                q.put(v)


if __name__ == '__main__':
    main()
    print(result)
