// mood_tracker.go
// 2025-11-14 - 気分トラッカー with ランダムなアドバイス

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	var mood string
	fmt.Print("今日の気分どう？（良い/普通/悪い）：")
	fmt.Scan(&mood)

	goodAdvice := []string{
		"その調子！今日も最高の1日にしよう！" ,
		"素晴らしい!そのエネルギーを大切にね！",
		"いいね！その気分のまま突っ走ろう！",
	}

	normalAdvice := []string{
		"まあまあだね。小さな楽しみを見つけてみよう！",
		"普通の日も大切。無理せず行こう！",
		"ぼちぼちでいいんだよ。焦らずにね！",
	}

	badAdvice := []string{
		"辛い日もあるよね。一歩ずつでいいから。",
		"そんなときもあるさ。明日はきっと良くなるよ！",
		"大丈夫、私が応援してるからね！",
	}

	switch mood {
	case "良い":
		fmt.Println(goodAdvice[rand.Intn(len(goodAdvice))])
	case "普通":
		fmt.Println(normalAdvice[rand.Intn(len(normalAdvice))])
	case "悪い":
		fmt.Println(badAdvice[rand.Intn(len(badAdvice))])
	default:
		fmt.Println("ん？よくわからなかったけど、とにかく頑張ろう！")
	}
}