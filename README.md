# 画像検索システム

 - [画像検索システムについて](https://docs.google.com/presentation/d/1U4psmf68yDAdP2JqvPPsFet1yPFiDGlB-ur5pJu-txs/edit#slide=id.ga3b140dff1_0_4)

## 実行方法
### 1. バッチ
```bash
$ python batch/train_estimator.py <モデルの保存先> <モデル名> <バージョン>
$ python batch/make_index.py <Indexパス> <次元数> <学習済みモデルのディレクトリパス> <学習済みモデル名> <学習済みモデルのバージョン>

# 実行例
$ python batch/train_estimator.py ./ CNNモデル 1.0
$ python batch/make_index.py ./cifarインデックス.index 64 ./ CNNモデル 1.0
```

### 2. API
```bash
$ python api/start_flask.py

# 画像URL指定で類似する画像を取得する
$ curl -XPOST "http://127.0.0.1:5000/image/search" \
    -H "Content-Type: application/json" \
    -d '{
        "image_url": "https://car.watch.impress.co.jp/img/car/docs/1256/450/01_l.jpg",
        "k": 5
    }'
```

---
## 参考文献
 - [Chainer とAnnoyを使った 類似画像検索 【入門】 - Qiita](https://qiita.com/ta7uw/items/9301eef7dd74a249d5ea)
 - [ヤフーの類似画像検索技術と特徴量モデル 〜 Yahoo!ショッピングの事例紹介 #機械学習  - Yahoo! JAPAN Tech Blog](https://techblog.yahoo.co.jp/entry/2020081130014621/)
 - [BASEアプリにおける類似画像検索の裏側　機械学習における画像とテキストの使い分け ログミーTech](https://logmi.jp/tech/articles/322876)
