# コーディング規約

## インデント

2スペース。

```dart
if (hoge) {
  someFunc();
}
```

継続インデントも2スペース。

```dart
someFunc(
  color: Colors.blue,
  fontSize: 16.0,
);
```

IntelliJの場合は Editor > Code Style > Dart > Tabs and Indent から設定する。

- Tab size: 2
- Indent: 2
- Continuation indent: 2
- Keep indents on empty lines: on


## 改行

引数が1つの場合は、1行で書いてもよい。
長くなる場合は改行して複数行で書いてもよい。

```dart
// 引数がchildの1つ
new Expand(child: new Text('Hello')),
```

引数が2つ以上のWidgetは複数行で書く。

```dart
// 引数がcolor, childの2つ
new Container(
  color: Colors.blue,
  child: new Text('Hello'), // Textは1行可
),
```

Widgetの引数が1つでも、その子Widgetが複数行の場合は、改行する。
つまり、1行でWidgetを書くのは、Widgetツリーの末端のみとなる。

```dart
// 引数が1つだがchildが複数行なので
// このWidget自身も複数行で書く
new Container(
  child: new Text(
    'Hello',
    style: const TextStyle(fontSize: 16.0),
  ),
),
```

例外的に、EdgeInsetsは複数の引数があっても1行でよい。

```dart
new Container(
  padding: const EdgeInsets.fromLTRB(1.0, 2.0, 3.0, 4.0),
),
```

## 括弧の位置

括弧の終了は、括弧の開始のあとに改行しない場合は、同じ行で閉じる。

```dart
new Container(child: Text('Hello')),
```

括弧の開始のあとに改行した場合、中身の最終行の次の行で括弧を閉じる。
なお、インデントはブロック開始時と同じにする。

```dart
new Container(
  color: Colors.blue,
  child: Text('Hello'),
), // good
```

```dart
new Container(
  color: Colors.blue,
  child: Text('Hello')), // bad
```

関数の呼び出しで「名前なし引数」で開始する場合、
同じ行でWidgetの括弧を開始する。
Widgetの閉じる括弧と関数呼び出しの閉じる括弧は同じ行。

```dart
someFunc(new Container(
  color: Colors.blue,
  child: new Text('Hello'),
));
```

このとき、Widget内の改行については、Widgetの規約に従う。

関数の呼び出しで「名前あり引数」の場合は、Widgetと同様に記述する。

```dart
someFunc(
  foo
  barOption: true,
  title: new Text(...), 
);
```

## カンマ

オブジェクトや関数呼び出しの引数で、末尾のカンマは省略せずに記述する。

```dart
new Text(
  "Hello, Flutter!",
  style: const TextStyle(
    fontSize: 14.0,
    fontWeight: FontWeight.bold, // trailing comma
  ), // trailing comma
),
```

## デフォルト引数

イコールで設定する。
※以前のDartではコロンだったが Deprecated のためイコールを使う

```dart
void someFunc({String text = 'Hello'}) {
  ...
}
```

Flutter内では以前からのコロンが使われており、
プロジェクト内でも以前に書かれた箇所はコロンを使っているが、
新しくコードを書く場合はイコールを使う。

## 文字列

文字列はシングルクォート、ダブルクォートのどちらを使ってもよい。

変数の文字列埋め込みでは、省略が可能な場合でも `{` `}` を記述する。

```dart
"Price is ${price} yen."
```

なお、文字列以外の変数は自動で `toString()` されるので、
`toString()` は記述しない。

## コメント

`//` と `/* ... */` はどちらを使ってもよい。

コメント開始 `//` とコメント本文の間は半角スペースひとつ開ける。
コメントの末尾にはピリオドや句点はつけない。

```dart
// 前回の読み込みから一定時間が経過していたら
// 自動で再読み込みを行い、最上部へスクロールする
```

## import

import は以下のグループごとにブロックを分ける。

- Dartコア
- サードパーティのパッケージ
- プロジェクト内の他のパッケージ
- 同じパッケージ

```dart
// dart
import 'dart:core';
import 'dart:async';

// third party
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

// app
import 'package:yourapp/widget.dart';
import 'package:yourapp/text.dart';

// same package
import 'foo.dart';
import 'bar.dart';
```

## クラス

インスタンス変数へのアクセスは、不要な場合は this を使わない。

```dart
// titleはインスタンス変数
new Text(title), // OK
new Text(this.title), // NG
```

### new/const

オブジェクトの生成で、constを選択できる場合は、constを選択する。


## 三項演算子

2つの値のどちらかを得るだけの場合など、単純な場合は使用してよい。
結果にさらに式を含まないようにすること。

```dart
// OK
color: android ? Colors.white : Colors.red,

// NG
color: android ? new Text(...) : new Text(...),
```

三項演算子のなかで使うものをあらかじめ計算するか、別のメソッドなどに切り分ける。

```dart
color: android ? _buildTitleForMaterial() : _buildTitleForCupertino(),
```



