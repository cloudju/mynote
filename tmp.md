# ブランチ戦略
git flowを利用する

## イメージ
![avatar](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F542703%2F2d2102cc-0f0e-922a-1e08-f0694413f060.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=6106f0e64268c6316b317fa272a23c20)

## 各ブランチの役割
|ブランチ名|説明|
|--|--|
|master|メジャーバージョン管理|
|release|Sprint納品用|
|develop|レビュー完了ソースコード格納用|
|feature リモート|レビュー用ブランチ、レビューしてから、developにマージする。<br>マージ完了したら、ブランチを削除する。<br>命名規則：#[taskID]_feat_[分かり易い対応内容]|
|feature local|開発用、タスク毎作成する|

