# 変数、引数 小文字のみ。スネークケースで書く(例: foo_)
# 関数,メソッド スネークケースで書く(例: foo_snake)。真偽値を返すメソッドであれば、最後に?をつける(例: foo_hoge?)
# 破壊的なメソッドはメソッドの最後に"!"をつける。(例: update!)
# 定数	大文字のみ、単語をアンダースコアで区切る。(例: MAX_SIZE).通常、モジュールレベル（関数の外側）に書く
# クラス (アッパーキャメルケースで書く 例: GetUser)
# ファイル名、ディレクトリ名。 スネークケースで書く(例: foo_class)
# 1文字変数は使わない。iとかoは1と0で間違ったりするから


module Test
  def hoge
    puts "Testmoduleが呼び出されている"
  end
end

class User
  # Test moduleを読み込んでいる
  include Test

  def get_user
    # Testモジュールをincludeしているので、hogeメソッドが使える
    hoge()
    puts "get_userが呼び出されている"
  end
end

# Userインスタンスの作成
user = User.new
# Userクラスのget_userメソッドを呼び出す。
# Userクラスで、Testモジュールをincludeしているので、hogeメソッドが使える
user.get_user
