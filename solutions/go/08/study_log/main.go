package main

import "fmt"

const studyTemplate = `# 問題 ID:
# 日付:
## 制約メモ
## サンプル trace
## 解法候補 (最大3)
## 実装メモ (テンプレ名)
## 公式解説後の diff
`

func main() {
	fmt.Print(studyTemplate)
}
