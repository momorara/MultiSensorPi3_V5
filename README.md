# MultiSensorPi3_V5
MultiSensorPi3 for Pi5

<h4><<概要>></h4>
　ラズパイを手に入れて、Ｌチカとかやってみたけれど、さて次は何をしようと悩んでいたら、センサーをやってみましょう。<br>
　部品から揃えてやるのもいいですが、サクッと初めてpythonでセンサーを試してみたいならこの基板が良いです。<br>
　センサーを個別に買うより、簡単に使えて、色々ノウハウが手に入ります。
 
  ・気象観測関係　気温、湿度、気圧センサー<br>
  ・距離測定　　　超音波による測距センサー<br>
  ・環境測定　　　明るさセンサー、傾きセンサー<br>
  ・その他　　　　LED 2個、SW 2個、赤外線センサー<br>
  
  以上のセンサー類をpythonで制御できます。<br>
　すべてのソースプログラムを開示いたします。<br>

・LEDの色等指定はできません。<br>
・部品の仕様、有無等変わる場合があります。 <br>
・基板のバージョンが変わる場合がありますが、機能等に違いはありません。<br>
・回路に関しても随時変更しますが、機能等に違いはありません。<br>
・ラズパイは付属しません。<br>
<br>
*MultiSensorPi3_V5の位置付け<br>
ラズパイ4までは、
git clone https://github.com/momorara/MultiSensorPi3 sensorHAT<br>
にてNode-REDで動作しますが、<br>
ラズパイ5(Bookworm)ではNode-Red未対応です。<br>
python3ベースのプログラムでラズパイ5対応としています。<br>
ただし、Bullseye、Busterでも動作します。<br>
説明資料は
https://github.com/momorara/MultiSensorPi3
を見てください。

<h4><<使用方法>></h4>
git clone https://github.com/momorara/MultiSensorPi3_V5 sensorHAT<br>
でラズパイにダウンロードしてください。<br>
インストールについては、インストール文書に従いインストールを行ってください。<br>

<h4><<動作環境>></h4>  作成中
2024/3/5 対応OS：Bullseye版11.9、BookWorm版12.5(一部機能)での動作を確認しています。<br>
2024/3/7 対応OS：Buster版10.13での動作を確認しています。<br>
   
<h4><<使用説明資料>></h4>  作成中
説明書類の中の資料を確認ください。
お問い合わせに関しては、サポート.txtを参照ください。

<h4><<ライセンス>></h4>
使用しているライブラリについては、ライブラリ制作者のライセンス規定を参照ください。
オリジナル部分については、オープソースとさせていただきます。
Released under the MIT license です。
プログラム自体はサンプルプログラムです。

<h4><<アップデート>></h4>
no data<br>

<h4><<サポート窓口>></h4>
  メールアドレスが　tkj-works@mbr.nifty.com に変更になっています。<br>
  資料等を修正中ですが、ご注意ください。<br>
