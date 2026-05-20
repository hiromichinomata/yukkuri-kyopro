from collections import deque


class AhoCorasick:
    def __init__(self) -> None:
        self.next = [{}]
        self.fail = [0]

    def add(self, s: str) -> None:
        node = 0
        for ch in s:
            if ch not in self.next[node]:
                self.next[node][ch] = len(self.next)
                self.next.append({})
                self.fail.append(0)
            node = self.next[node][ch]

    def build(self) -> None:
        q = deque()
        for ch, nxt in self.next[0].items():
            q.append(nxt)
        while q:
            v = q.popleft()
            for ch, nxt in self.next[v].items():
                f = self.fail[v]
                while f and ch not in self.next[f]:
                    f = self.fail[f]
                self.fail[nxt] = self.next[f].get(ch, 0)
                q.append(nxt)

    def search(self, text: str) -> list:
        node = 0
        hits = []
        for i, ch in enumerate(text):
            while node and ch not in self.next[node]:
                node = self.fail[node]
            node = self.next[node].get(ch, 0)
            if node:
                hits.append(i)
        return hits


def main() -> None:
    ac = AhoCorasick()
    for w in ["he", "she", "his"]:
        ac.add(w)
    ac.build()
    print(ac.search("ushers"))


if __name__ == "__main__":
    main()
