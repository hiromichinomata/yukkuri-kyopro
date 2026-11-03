from collections import deque


class AhoCorasick:
    def __init__(self) -> None:
        self.next = [{}]
        self.fail = [0]
        self.out = [[]]  # そのノードで終わるパターン番号（失敗リンク先の分も含む）
        self.words = []

    def add(self, s: str) -> None:
        node = 0
        for ch in s:
            if ch not in self.next[node]:
                self.next[node][ch] = len(self.next)
                self.next.append({})
                self.fail.append(0)
                self.out.append([])
            node = self.next[node][ch]
        self.out[node].append(len(self.words))
        self.words.append(s)

    def build(self) -> None:
        q = deque(self.next[0].values())
        while q:
            v = q.popleft()
            for ch, nxt in self.next[v].items():
                f = self.fail[v]
                while f and ch not in self.next[f]:
                    f = self.fail[f]
                self.fail[nxt] = self.next[f].get(ch, 0)
                # 失敗リンク先で終わるパターンも、ここで終わっている
                self.out[nxt] = self.out[nxt] + self.out[self.fail[nxt]]
                q.append(nxt)

    def search(self, text: str) -> list:
        """(終了位置, パターン) のリストを返す"""
        node = 0
        hits = []
        for i, ch in enumerate(text):
            while node and ch not in self.next[node]:
                node = self.fail[node]
            node = self.next[node].get(ch, 0)
            for k in self.out[node]:
                hits.append((i, self.words[k]))
        return hits


def main() -> None:
    ac = AhoCorasick()
    for w in ["he", "she", "his", "hers"]:
        ac.add(w)
    ac.build()
    for end, word in ac.search("ushers"):
        print(end, word)


if __name__ == "__main__":
    main()
