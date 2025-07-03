# yamlgenpp
YAML to C++ struct generator

yamlファイルの構造を再現するstructとそのファイルを自動的に読み込むC++コードを生成します。
生成されたコードをリンクすることで、実行時にそのyamlファイルのデータが改めて読み込まれ、C++からはグローバル変数としてアクセスできるようになります。
C++を再コンパイルすることなくパラメータを変えるのに使えます。

## 使い方

このリポジトリをsubmoduleで入れるなどして、 [example/CMakeLists.txt](example/CMakeLists.txt) のようにすると、 [example/main.cpp](example/main.cpp) のようにyamlファイルの内容にアクセスすることができます
